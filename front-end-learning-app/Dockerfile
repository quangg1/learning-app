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
ENV PORT=10000
ENV PYTHONPATH=/app
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1
ENV FLET_SERVER_PORT=10000
ENV FLET_FORCE_WEB_VIEW=true

# Expose the port
EXPOSE 10000

# Create a script to start Xvfb and the application
RUN echo '#!/bin/bash\n\
# Remove any existing X server lock files\n\
rm -f /tmp/.X*-lock\n\
rm -f /tmp/.X11-unix/X*\n\
\n\
echo "Starting Xvfb..."\n\
Xvfb :99 -screen 0 1024x768x16 &\n\
sleep 2\n\
\n\
echo "Starting Flet application on port $PORT..."\n\
echo "Current working directory: $(pwd)"\n\
echo "Contents of current directory:"\n\
ls -la\n\
\n\
python3 main.py\n\
' > /app/start.sh && \
    chmod +x /app/start.sh

# Run the application
CMD ["/app/start.sh"] 