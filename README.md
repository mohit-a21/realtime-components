Run docker compose for server
```shell
sudo /usr/local/bin/docker-compose up --build
```

Run docker compose for web
```shell
cd client
sudo /usr/local/bin/docker-compose up --build
```

Run nginx as connector
```shell
sudo nginx -c $PWD/nginx.conf -g "daemon off;"
```