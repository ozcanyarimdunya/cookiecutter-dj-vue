FROM node:alpine as builder

WORKDIR /app

COPY ./frontend/package.json .

RUN npm install

COPY ./frontend .

RUN npm run build

# ============================== #

FROM python:3.6

WORKDIR /app

RUN apt-get -qq update && apt-get -qq -y upgrade

RUN apt-get install -qq -y vim curl libpq-dev build-essential nginx

RUN rm /etc/nginx/sites-enabled/default

RUN rm /etc/nginx/sites-available/default

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY {{cookiecutter.project_name}}.conf /etc/nginx/conf.d

COPY . .

COPY --from=builder /app/dist/index.html /app/templates/index.html

COPY --from=builder /app/dist/static /app/assets/static

