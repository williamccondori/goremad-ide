# Utilizamos una versión de Node.js basada en Alpine para la etapa de construcción,
# ya que es más ligera y segura que otras imágenes de Node.
FROM node:14-alpine as build-stage

# Establecemos /app como el directorio de trabajo dentro del contenedor.
WORKDIR /app

ARG BASE_URL
ENV BASE_URL=$BASE_URL


# Copiamos solo los archivos de configuración de npm para instalar las dependencias.
# Esto permite aprovechar la caché de Docker para no reinstalar las dependencias
# si estos archivos no han cambiado.
COPY package*.json ./

# Instalamos las dependencias del proyecto.
RUN npm install

# Copiamos el resto de los archivos del proyecto.
# Se hace después de instalar las dependencias para aprovechar la caché de Docker.
COPY . .

# Generamos la versión de producción de la aplicación utilizando nuxt generate.
RUN npm run generate

# Para la etapa de producción, utilizamos otra imagen de Node.js basada en Alpine.
FROM node:14-alpine as production-stage

# Instalamos el paquete 'serve' para servir la aplicación en producción.
RUN npm install -g serve

# Copiamos los archivos generados en la etapa de construcción a la etapa de producción.
# Esto minimiza el tamaño del contenedor final ya que solo incluye los archivos necesarios.
COPY --from=build-stage /app/dist /app/dist

# Exponemos el puerto 80 para que la aplicación sea accesible.
EXPOSE 80

# Comando para iniciar 'serve' en el puerto 80 y servir la aplicación.
CMD ["serve", "-s", "/app/dist", "-l", "80"]
