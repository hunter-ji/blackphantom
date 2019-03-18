FROM nginx

LABEL maintainer "Kuari <kuari@justmylife.cc>"

ADD ./web.tar.bz2 /usr/share/nginx/

RUN mv /usr/share/nginx/web/* /usr/share/nginx/html
