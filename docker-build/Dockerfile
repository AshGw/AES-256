FROM python:3.7
LABEL name="AshCrypt-light"
LABEL maintainer="AshrefGw@pronton.me>"
LABEL version="1.0"
LABEL description="AES-256 for files/text"

ENV DISPLAY=:0

WORKDIR /Landing

RUN git clone https://github.com/AshGw/AES-256.git
WORKDIR /Landing/AES-256

RUN apt-get update -y
RUN apt-get install -y git
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv vvv
RUN /bin/sh -c ". vvv/bin/activate"
RUN pip install -r important/requirements.txt
WORKDIR /Landing/AES-256/src

RUN chmod +x CliCrypt.py
CMD ["python", "/Landing/AES-256/src/CliCrypt.py"]