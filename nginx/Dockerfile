FROM nginx:alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf

COPY ./nsuem.key /etc/nginx/ssl/nsuem.key
COPY ./nsuem.ru.crt /etc/nginx/ssl/nsuem.ru.crt
COPY ./ca.crt /etc/nginx/ssl/ca.crt