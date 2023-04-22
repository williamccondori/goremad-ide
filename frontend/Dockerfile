# Use a multi-stage build to reduce image size
FROM node:lts-alpine AS build

ENV NODE_OPTIONS=--openssl-legacy-provider

# Create a dedicated build folder
WORKDIR /build

# Copy package.json and package-lock.json first for better caching
COPY package*.json ./

# Install only production dependencies
RUN npm ci --only=production

# Copy the rest of the application
COPY . .

# Build the application
ARG BASE_URL
ENV BASE_URL=$BASE_URL

RUN npm run generate

# Use a separate stage for production
FROM node:lts-alpine AS production

# Install the 'serve' package globally
RUN npm install -g serve

# Create a dedicated app folder
WORKDIR /app

# Copy the build output from the previous stage
COPY --from=build /build/dist /app/dist

# Expose the port for the application
EXPOSE 5000

# Run 'serve' to serve the application
CMD [ "serve", "-s", "dist", "-l", "5000" ]
