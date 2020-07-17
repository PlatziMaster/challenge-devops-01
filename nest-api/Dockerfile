FROM node:12.18.2 AS builder
WORKDIR /nest-api
COPY ./package.json ./
RUN npm install
COPY . .
RUN npm run build


FROM node:12.18.2-alpine
WORKDIR /nest-api
COPY --from=builder /nest-api ./
EXPOSE 3001
CMD ["npm", "run", "start:prod"]