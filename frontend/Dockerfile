# build env
FROM node:14-alpine as build
WORKDIR /app
COPY package.json ./
COPY yarn.lock ./
RUN yarn
COPY . ./
RUN yarn build
CMD cp -r build result_build
