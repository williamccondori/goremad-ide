FROM node:lts-alpine AS build

ENV NODE_OPTIONS=--openssl-legacy-provider

WORKDIR /src

COPY package*.json ./

RUN npm install

COPY . .

ARG BASE_URL
ENV BASE_URL=$BASE_URL

RUN npm run generate

FROM node:lts-alpine AS production

RUN npm install -g http-server

WORKDIR /app

COPY --from=build /src/dist /app/dist

EXPOSE 8080

CMD [ "http-server", "dist" ]
