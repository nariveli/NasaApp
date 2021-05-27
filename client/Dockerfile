FROM python:rc-slim

COPY requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /home/client

RUN mkdir /home/client/data

VOLUME /home/client/data

COPY client.py database.py conf.json .

CMD ["python3", "./client.py"]