FROM node:14.16

WORKDIR /usr/coding/backend-app
COPY src/package*.json ./
RUN npm install
COPY . .

EXPOSE 8081
CMD [ "node", "src/server.js" ]
