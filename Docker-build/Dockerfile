FROM python:3.8

ENV DISPLAY=:0

WORKDIR .

RUN pip install --upgrade pip

RUN pip install AshCrypt

CMD ["python", "-m", "AshCrypt.CliCrypt"]
