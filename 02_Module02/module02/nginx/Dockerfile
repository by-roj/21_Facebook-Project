FROM nginx:stable

RUN apt-get update
RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/