FROM python:3.11.6

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY .local/pip.conf /root/.config/pip/pip.conf
COPY requirements.txt requirements_dev.txt ./
RUN cat requirements.txt requirements_dev.txt > requirements_install.txt

RUN pip install -r requirements_install.txt

RUN apt update && apt install -y awscli