FROM python:3.8

ENV DISPLAY=:0

WORKDIR /Landing

RUN apt-get update -y
RUN pip install --upgrade pip
RUN apt-get install -y git
RUN git clone https://github.com/AshGw/AES-256.git

WORKDIR /Landing/AES-256

RUN pip install -r important/requirements.txt
RUN python setup.py develop

WORKDIR /Landing/AES-256/AshCrypt

CMD ["python", "-m", "CliCrypt"]
