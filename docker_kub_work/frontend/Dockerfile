# Section 1 - Build Phase
FROM node:16-alpine as builder

WORKDIR '/app'

COPY package.json ./
RUN npm install
COPY . .

RUN npm run build

# Section 2 - Run Phase
FROM nginx as runner  
COPY --from=builder /app/build /usr/share/nginx/html
