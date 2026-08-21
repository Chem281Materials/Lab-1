# Use a Python image with apt access
FROM python:3.11-slim

# Update packages and install required tools
RUN apt-get update && apt-get install -y \
    vim \
    && apt-get clean

# Set working directory
WORKDIR /root

# Copy the Python GUI script
COPY app.py .

# Default command
CMD ["bash"]
