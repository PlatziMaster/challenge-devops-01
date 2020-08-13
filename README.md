export DOMAIN=traefik.nicobytes.site

https == traefik.nicobytes.site

80
443

swarm
- flask.nicobytes.site == https
- express.nicobytes.site == https
- nicobytes.site == https (nginx 80)
- app.nicobytes.site == https (nginx 80)

add conf proxy

- proxy == nicobytes.site https (proxy)
  - /express == redirecion
  - /flask == redirecion
  - api.nicobytes.site/

- / == frontend (angular | react | vue)
  - nicobytes.site/list
  - nicobytes.site/courses
  - nicobytes.site/teachers

  - nicobytes.site/flask
