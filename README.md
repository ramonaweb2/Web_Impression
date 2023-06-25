# Web Impression Mockup

## Beginning:
> sudo apt install docker-compose

Build a Docker image:
> sudo docker build -t ramonagospodinova/web_impression .

* Docker post install:
> https://docs.docker.com/engine/install/linux-postinstall/

Run specific docker-compose file
> sudo docker-compose -f docker-compose.prod.yml up -d

Run specific 'service' from 'docker-compose' file, i.e. 'nginx'
> sudo docker-compose -f docker-compose.prod.yml run nginx

View service logs for 'web' service:
> sudo docker-compose logs -f web

To rebuild:
> sudo docker-compose -f docker-compose.prod.yml -up -d --build

To push docker image to Docker hub
> sudo docker-compose -f docker-compose.prod.yml push web

### Troubleshooting
Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use
# List who's using the port
> sudo lsof -i -P -n | grep 80
> sudo kill <process id>