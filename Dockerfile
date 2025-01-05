FROM python:3.11-slim

WORKDIR /air-quality-index-analysis

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "run.py"]

