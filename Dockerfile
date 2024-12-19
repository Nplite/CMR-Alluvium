# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Install system dependencies required for OpenCV and other libraries
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip  # Ensure pip is updated
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Ensure Python outputs everything to the terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "trial:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Cammand for running:
#docker build -t metaltheft-app .
#docker run -d -p 8000:8000 --name metaltheft-container metaltheft-app
# sudo systemctl status docker
# sudo systemctl start docker




# View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/ld308cxf0c77ddube78ayz4xy