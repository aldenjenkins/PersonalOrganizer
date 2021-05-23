FROM python:3.7-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
COPY . /app/
ENV DJANGO_SETTINGS_MODULE="organizer.settings.production"

