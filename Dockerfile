FROM python:3.9

WORKDIR /app

COPY requirements.txt .

# dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY imgtotext.py .

EXPOSE 6000

CMD ["python", "app.py"]


