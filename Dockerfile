FROM python:3.13

WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y chromium chromium-driver
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/usr/lib/chromium-browser:${PATH}"
CMD ["pytest", "tests/", "-v", "--html=report.html"]