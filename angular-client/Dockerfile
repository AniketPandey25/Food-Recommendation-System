FROM node:lts-alpine3.14 as build-step

RUN mkdir -p /app

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

RUN npm run build --prod

FROM nginx:mainline-alpine

COPY --from=build-step /app/dist/angular-client /usr/share/nginx/html

EXPOSE 80
