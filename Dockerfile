FROM python:3.9

EXPOSE 5000

WORKDIR /app

COPY requiriments.txt .

RUN pip install -r requiriments.txt

COPY app.py .

CMD ["python3", "app.py"]