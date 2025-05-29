FROM debian:bullseye-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-dev \
    python3-pip \
    build-essential \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libglib2.0-0 \
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    gstreamer1.0-plugins-base \
    libmpv1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV API_BE=learning-app
ENV DOMAIN_BE=https://learning-app-backend-0gfg.onrender.com
ENV SENTIMENT_API_DOMAIN=''
ENV TURN_ON_SCREEN=False
ENV PORT=8080
ENV PYTHONPATH=/app
ENV DISPLAY=:99

# Expose the port
EXPOSE 8080

# Create a script to start Xvfb and the application
RUN echo '#!/bin/bash\nXvfb :99 -screen 0 1024x768x16 &\nsleep 1\nflet run --port $PORT --host 0.0.0.0 main.py' > /app/start.sh && \
    chmod +x /app/start.sh

# Run the application
CMD ["/app/start.sh"] 