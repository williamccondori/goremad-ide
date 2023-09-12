# Usar una imagen de Node más pequeña y segura como base
FROM node:14-alpine as build-stage

# Directorio donde se almacenará la aplicación
WORKDIR /app

# Copiar el package.json y package-lock.json primero para aprovechar el almacenamiento en caché de Docker
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código fuente de la aplicación
COPY . .

# Compilar la aplicación para producción
RUN npm run build

# Fase de producción
FROM nginx:stable-alpine as production-stage

# Copiar el script de configuración de nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar los archivos compilados desde la etapa de construcción
COPY --from=build-stage /app/.nuxt/dist/client /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Comando para iniciar nginx
CMD ["nginx", "-g", "daemon off;"]
