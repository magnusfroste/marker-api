# Marker API - Product Requirements Document (PRD)

> **Version:** 1.0  
> **Last Updated:** February 2026  
> **Status:** Active Development

---

## Executive Summary

**Marker API** is a simple REST API for PDF to Markdown conversion using [Marker](https://github.com/VikParuchuri/marker). Designed for Easypanel deployment, it provides a straightforward interface for converting PDF documents to Markdown format, making it easy to integrate into document processing workflows.

### Target Users

- **Primary**: Developers needing PDF to Markdown conversion
- **Secondary**: Document processing workflows
- **Tertiary**: Applications requiring document text extraction

### Unique Value Proposition

- **Simple API**: RESTful interface for easy integration
- **Easypanel Ready**: Optimized for Easypanel deployment
- **Docker Ready**: Containerized for production deployment
- **Fast Conversion**: Efficient PDF to Markdown conversion

---

## 1. Product Vision

Marker API aims to provide a simple, reliable API for PDF to Markdown conversion, making it easy for developers to integrate document processing into their applications with minimal setup.

### Success Metrics

- **API Reliability**: Uptime and response times
- **Conversion Accuracy**: Markdown output quality
- **Integration Ease**: Number of successful integrations
- **User Satisfaction**: Developer satisfaction with API

---

## 2. Core Features

### 2.1 PDF Conversion

**Priority:** P0 (Critical)

**Description:** Convert PDF files to Markdown format.

**Requirements:**
- POST endpoint for file upload
- Markdown output
- Error handling
- File validation

**User Stories:**
- As a developer, I want PDF to Markdown conversion so I can process documents
- As a user, I want error handling so I know if conversion fails
- As a user, I want file validation so I only process valid files

**Technical Notes:**
- Marker library for PDF processing
- Multipart form data handling
- Response formatting
- Error code system

---

### 2.2 Health Check

**Priority:** P0 (Critical)

**Description:** Health check endpoint for monitoring.

**Requirements:**
- GET endpoint for health checks
- Status response
- Simple response format

**User Stories:**
- As a devops engineer, I want health checks so I can monitor the API
- As a user, I want simple status so I can verify API availability

**Technical Notes:**
- Health check endpoint
- Status response format
- Error handling

---

## 3. Technical Architecture

### 3.1 Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend** | Python 3.11+ | Application runtime |
| **Framework** | FastAPI | API framework |
| **PDF Processing** | Marker | PDF to Markdown |
| **Container** | Docker | Deployment |
| **Platform** | Easypanel | Hosting platform |

### 3.2 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Marker API Backend                       │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  FastAPI Application (Python 3.11+)                        ││
│  │  - PDF Conversion Endpoint                              ││
│  │  - Health Check Endpoint                                ││
│  │  - Error Handling                                        ││
│  │  - File Validation                                     ││
│  └─────────────────────────────────────────────────────────┘│
│                            │                                 │
│                            ▼                                 │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Marker Library                                         ││
│  │  - PDF Processing                                        ││
│ │  - Markdown Generation                                   ││
│  │  - Text Extraction                                      ││
│  └─────────────────────────────────────────────────────────┘│
│                            │                                 │
│                            ▼                                 │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  HTTP Server (Port 8001)                                ││
│  │  - Request Handling                                     ││
│  │  - Response Formatting                                 ││
│  │  - Error Responses                                      ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Data Flow

**PDF Conversion Flow:**
1. User uploads PDF file
2. File validated (PDF format)
3. File processed by Marker
4. Markdown generated
5. Response returned to user

**Health Check Flow:**
1. Health check requested
2. API status verified
3. Status response returned
4. User notified of API health

---

## 4. User Experience

### 4.1 Onboarding

**First-Time User Experience:**

1. **API Documentation**
   - Endpoint documentation
   - Usage examples
   - Integration guide

### 4.2 Daily Use

**Typical Usage:**
1. Developer integrates API
2. User uploads PDF file
3. Markdown returned
4. Integration processes output

### 4.3 Error States

**Graceful Degradation:**
- Invalid file: "Ogiltig filformat. Vänligen ladda upp en PDF-fil."
- Conversion error: "Kunde inte konvertera filen. Försök igen."
- Server error: "Internt serverfel. Försök igen."

---

## 5. Roadmap

### Phase 1: MVP (Current)

- ✅ PDF to Markdown conversion
- ✅ Health check endpoint
- ✅ Easypanel deployment
- ✅ Docker containerization

### Phase 2: Enhanced Experience (Q1 2026)

- 🔄 Batch processing
- 🔄 Advanced options
- 🔄 Rate limiting
- 🔄 Usage analytics

### Phase 3: Advanced Features (Q2 2026)

- 📝 OCR integration
- 🔍 Metadata extraction
- 🏆 Performance optimization
- 🤖 API versioning

---

## 6. Success Criteria

### Technical

- [ ] API response time < 5 seconds
- [ ] File size support up to 10MB
- [ ] Conversion accuracy > 95%
- [ ] Uptime > 99%

### User Experience

- [ ] Conversion success rate > 95%
- [ ] API documentation clarity > 4.5/5
- [ ] Integration ease > 4/5
- [ ] Error handling effectiveness > 90%

### Business

- [ ] 100+ daily API calls
- [ ] 50+ successful conversions/day
- [ ] 99% uptime
- [ ] 0.5s average response time

---

## 7. Risks & Mitigations

### Risk 1: File Size Limits

**Risk:** Large PDF files causing performance issues

**Mitigation:**
- File size validation
- Memory management
- Error messages for oversized files

### Risk 2: Conversion Quality

**Risk:** Poor Markdown output quality

**Mitigation:**
- Marker library updates
- Quality testing
- User feedback mechanism

### Risk 3: API Reliability

**Risk:** API downtime or performance issues

**Mitigation:**
- Health monitoring
- Error handling
- Graceful degradation

---

## 8. Dependencies

### Libraries

- `marker`: PDF to Markdown conversion
- `fastapi`: API framework

### Platforms

- **Easypanel**: Deployment platform
- **Docker**: Containerization

---

## 9. Appendix

### A. Environment Variables

```env
# Device Configuration
TORCH_DEVICE=cpu  # Options: cpu, cuda
```

### B. Installation Instructions

```bash
# Clone the repository
git clone https://github.com/magnusfroste/marker-api.git
cd marker-api

# Install dependencies (if needed)
pip install -r requirements.txt

# Run locally
python main.py

# Build Docker image
docker build -t marker-api .

# Run container
docker run -p 8001:8001 marker-api
```

### C. Easypanel Deployment

1. Create new App in Easypanel
2. Connect to this GitHub repo
3. Build method: Dockerfile
4. Port: 8001
5. Memory: 4-8GB recommended
6. Deploy!

---

**Document History:**

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Feb 2026 | Initial PRD creation | Magnus Froste |

---

**License:** MIT - See LICENSE file for details
