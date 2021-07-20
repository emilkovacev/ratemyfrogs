FROM nginx:1.19.0

RUN mkdir /code
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
WORKDIR /code
