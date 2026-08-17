FROM node:16-bullseye

RUN apt-get update \
    && apt-get install -y python3 python3-pip make g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

ENV PORT=10000

CMD ["node", "index.js"]
