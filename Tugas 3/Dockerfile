FROM python:3.12

# Select Directory
WORKDIR /mysite

# Copy atribut requirement
COPY requirements.txt .

# Up pip & Install library
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all asset
COPY mysite/ .

# LISTEN PORT 5000
EXPOSE 5000

# Run server manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
