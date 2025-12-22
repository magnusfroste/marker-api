"""
Simple FastAPI server for Marker PDF to Markdown conversion.
Designed for Easypanel deployment.
"""
import os
import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="Marker API", description="PDF to Markdown conversion with OCR")


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):
    """
    Convert PDF to Markdown using Marker.
    
    Returns:
        JSON with 'markdown' field containing the converted text.
    """
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        # Save uploaded file to temp location
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        try:
            # Import marker and convert
            from marker.converters.pdf import PdfConverter
            from marker.models import create_model_dict
            
            # Create converter with models
            models = create_model_dict()
            converter = PdfConverter(artifact_dict=models)
            
            # Convert PDF to markdown
            result = converter(tmp_path)
            
            # Extract markdown from result
            if hasattr(result, 'markdown'):
                markdown = result.markdown
            elif isinstance(result, tuple) and len(result) > 0:
                markdown = result[0] if isinstance(result[0], str) else str(result[0])
            elif isinstance(result, str):
                markdown = result
            else:
                markdown = str(result)
            
            return JSONResponse(content={"markdown": markdown, "filename": file.filename})
            
        finally:
            # Clean up temp file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {str(e)}")


@app.get("/")
async def root():
    """Root endpoint with API info"""
    return {
        "name": "Marker API",
        "version": "1.0.0",
        "endpoints": {
            "/convert": "POST - Convert PDF to Markdown",
            "/health": "GET - Health check"
        }
    }
