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


TODO:
1. work on prompt engineering
2. Enable multiple suggestions from open ai
3. Enable slider for multiple suggestions in UI
4. Error handling for failed request