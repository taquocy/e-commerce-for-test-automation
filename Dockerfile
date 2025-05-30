FROM python:3.13

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY resources/chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

CMD ["python", "tests/run_tests.py"]