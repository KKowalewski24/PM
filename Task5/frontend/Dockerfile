FROM node:14.16

WORKDIR /usr/coding/frontend-app
COPY source/package*.json ./
RUN npm install
COPY . .

EXPOSE 8080
CMD [ "npm", "run", "serve" ]
