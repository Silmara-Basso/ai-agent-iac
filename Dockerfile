#=================================================
# Dockerfile
#=================================================
# Base image
FROM python:3.12-slim

# Defines the working directory within the container.
WORKDIR /usr/src/app

#  Copy and install the Python dependencies.
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files.
COPY ./app .

# It exposes the Streamlit.
EXPOSE 8501

# Command to start the Streamlit application
CMD ["streamlit", "run", "iac.py", "--server.port=8501", "--server.address=0.0.0.0"]