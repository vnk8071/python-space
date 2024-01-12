FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ../../ /app/
WORKDIR /app/

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "src.api.app:app"]
