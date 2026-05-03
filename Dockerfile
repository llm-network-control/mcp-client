FROM python:3.14-slim

RUN apt-get update && apt-get install -y build-essential
RUN pip install --upgrade pip
COPY requirements.txt dev-requirements.txt ./
RUN pip install -r requirements.txt && pip install -r dev-requirements.txt
COPY ./ ./

RUN mkdir -p /data

RUN ["alembic", "upgrade", "head"]
RUN ["python", "fill_db_with_fake_data.py"]
CMD ["python", "main.py"]
