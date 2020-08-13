export DOMAIN=traefik.nicobytes.site

https == traefik.nicobytes.site

80
443

swarm
- flask.nicobytes.site == https
- express.nicobytes.site == https
- nicobytes.site == https (nginx 80)
- app.nicobytes.site == https (nginx 80)