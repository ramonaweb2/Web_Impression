# Web Impression Mockup

## Beginning:
> sudo apt install docker-compose

Build a Docker image:
> sudo docker build -t ramonagospodinova/web_impression .

* Docker post install:
> https://docs.docker.com/engine/install/linux-postinstall/


Down docker services:
> docker-compose down --remove-orphans

Run specific docker-compose file (-f + <docker-compose filename)
> sudo docker-compose -f docker-compose.prod.yml up -d

Run specific 'service' from 'docker-compose' file, i.e. 'nginx'
> sudo docker-compose -f docker-compose.prod.yml run nginx

View all services logs:
> sudo docker-compose logs

View service logs for 'web' service:
> sudo docker-compose logs -f web

To rebuild:
> sudo docker-compose -f docker-compose.prod.yml up -d --build
(sudo docker-compose up --build)

Build specific service, i.e 'web'
> sudo docker-compose -f docker-compose.prod.yml up -d --build web

### Only production commands:
> sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic
(Result: 193 static files copied to '/tmp/webImpression/staticfiles'.)

Start bash in container:
> docker exec -it fee20678f998 bash

### Troubleshooting
Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use
# List who's using the port
> sudo lsof -i -P -n | grep 80
> sudo kill <process id>

# Reload NGINX
> sudo systemctl reload nginx
# Force recreate NGINX:
> docker-compose -f docker-compose.prod.yml up -d --force-recreate nginx

# Purging All Unused or Dangling Images, Containers, Volumes, and Networks
> docker system prune -a

# SSL Certificate:
# web.conf file in v1. (web-without-certificate.conf)
# 1. You can now test that everything is working by running
# docker-compose -f docker-compose-certbot.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d web-impression.net
# You should get a success message like "The dry run was successful".

# web.conf in v2. (web-with-certificate.conf)
# 2. You can now generate certificate (without --dry-run) by running
#  docker-compose -f docker-compose-certbot.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d web-impression.net


### Git commands:
Pull from master branch:
> git pull origin master

### GitHub
To push docker image to Docker hub
> sudo docker-compose -f docker-compose.prod.yml push web
