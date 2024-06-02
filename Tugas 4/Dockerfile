FROM python:3.10-slim-buster

# Buat direktori kerja
WORKDIR /ferrenzatugas4

# Salin file requirements.txt dan instal dependensinya
COPY requirements.txt .

# Upgrade pip dan instal dependensi Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Salin seluruh konten dari direktori mysite lokal ke dalam kontainer
COPY ferrenzatugas4/ .

# Expose port 8000
EXPOSE 8000

# Jalankan server menggunakan manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]