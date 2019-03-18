FROM python


LABEL maintainer "Kuari <kuari@justmylife.cc>"

RUN pip install --upgrade pip
RUN pip install gunicorn eventlet pytest flask

ADD ./server.tar.bz2 /mnt

WORKDIR /mnt/server

CMD bash run.sh
