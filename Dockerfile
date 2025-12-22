# GPU version: Use CUDA base image
# CPU version: Change to python:3.11-slim
ARG BASE_IMAGE=nvidia/cuda:12.1.0-runtime-ubuntu22.04
FROM ${BASE_IMAGE}

WORKDIR /app

# Install Python and system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/python3.11 /usr/bin/python

# Install Python dependencies
# PyTorch with CUDA support
RUN pip install --no-cache-dir \
    torch torchvision --index-url https://download.pytorch.org/whl/cu121

RUN pip install --no-cache-dir \
    marker-pdf \
    fastapi \
    uvicorn \
    python-multipart

# Copy API server
COPY server.py /app/server.py

ENV TORCH_DEVICE=cuda

EXPOSE 8001

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]
