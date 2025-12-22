# Marker API

Simple REST API for PDF to Markdown conversion using [Marker](https://github.com/VikParuchuri/marker).

Designed for Easypanel deployment.

## Deployment (Easypanel)

1. Create new App in Easypanel
2. Connect to this GitHub repo
3. Build method: Dockerfile
4. Port: 8001
5. Memory: 4-8GB recommended

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `TORCH_DEVICE` | `cpu` | Device for ML models (`cpu` or `cuda`) |

## API Endpoints

### POST /convert

Convert PDF to Markdown.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (PDF file)

**Response:**
```json
{
  "markdown": "# Document Title\n\nContent...",
  "filename": "document.pdf"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{"status": "ok"}
```

## Usage with AutoVersio

Set in AutoVersio environment:
```
OCR_SERVICE_URL=http://marker-api:8001
```

Replace `marker-api` with the internal hostname from Easypanel.
