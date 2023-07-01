Run docker compose for server
```shell
docker-compose up --build
```

Run docker compose for web
```shell
cd client
docker-compose up --build
```

Run nginx as connector
```shell
nginx -c $PWD/nginx.conf -g "daemon off;"
```