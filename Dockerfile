FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN ["python3", "manage.py", "makemigrations"]
RUN ["python3", "manage.py", "migrate"]
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]