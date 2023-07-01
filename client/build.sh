git pull origin main

sudo docker build -t webvault:$1 .

aws ecr get-login-password --region us-west-2 | sudo docker login --username AWS --password-stdin 277357190350.dkr.ecr.us-west-2.amazonaws.com/webvault:$1

sudo docker tag webvault:$1 277357190350.dkr.ecr.us-west-2.amazonaws.com/webvault:$1
sudo docker push 277357190350.dkr.ecr.us-west-2.amazonaws.com/webvault:$1
