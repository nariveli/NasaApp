FROM python:rc-slim

COPY requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/server

COPY server.py .

EXPOSE 5000

CMD ["python3", "./server.py"]