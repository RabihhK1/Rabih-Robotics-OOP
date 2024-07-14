FROM python:3.9.19-slim

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
#CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "*.py"]