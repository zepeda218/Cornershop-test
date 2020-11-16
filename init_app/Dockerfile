FROM python:3.8.3-buster

ENV WORKDIR /cornershop

RUN mkdir -p $WORKDIR
WORKDIR ${WORKDIR}

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN cd ${WORKDIR}

EXPOSE 8000