# Web Impression Mockup

## Beginning:
> sudo apt install docker-compose

Build a Docker image:
> sudo docker build -t ramonagospodinova/web_impression .

* Docker post install:
> https://docs.docker.com/engine/install/linux-postinstall/


Down docker services:
> docker-compose down --remove-orphans

Stop all running containers
> docker ps -q | xargs docker stop

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
Clearing static files:
Remove static files:
# 1.
> python3 manage.py collectstatic --noinput --clear
# 2.
> cd /staticfiles/
> sudo rm -rf /staticfiles/*
# 3.
> sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic

Start bash in container:
> docker exec -it fee20678f998 bash

### Troubleshooting
Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use
# List who's using the port
> sudo lsof -i -P -n | grep 80
> sudo kill <process id>

# Reload NGINX using docker
> docker-compose exec nginx nginx -s reload

# Force recreate NGINX:
> docker-compose -f docker-compose.prod.yml up -d --force-recreate nginx

# Purging All Unused or Dangling Images, Containers, Volumes, and Networks
## (For Docker error: "no space left on device")
> docker system prune -a
> docker image prune -a

# SSL Certificate:
# {!!!
# > docker-compose -f docker-compose.prod.yml up -d --force-recreate nginx
# remove directory 'certbot' !!! This will remove the certificate!!!

# web.conf file in v1. (ssl_certificate/web-without-certificate.conf)
# 1. You can now test that everything is working by running
# docker-compose -f docker-compose-certbot.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d web-impression.net
# You should get a success message like "The dry run was successful".

# web.conf in v2. (ssl_certificate/web-with-certificate.conf)
# 2. You can now generate certificate (without --dry-run) by running
# docker-compose -f docker-compose-certbot.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d web-impression.net
# docker-compose -f docker-compose.prod.yml up -d --force-recreate nginx

### Git commands:
Reset (override) local changes:certbot certonly --webroot -w /path/to/website1 -d example.com
> git reset --hard

Pull from master branch:
> git pull origin master
