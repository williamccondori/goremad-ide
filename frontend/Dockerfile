FROM node:lts-alpine AS build

WORKDIR /src

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM node:lts-alpine AS production

RUN npm install -g http-server

WORKDIR /app

COPY --from=build /src/dist /app/dist

EXPOSE 8080

CMD [ "http-server", "dist" ]
