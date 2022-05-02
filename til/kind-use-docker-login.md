# Kind Using your Own docker login with Kind

when using kubernetes kind, sometimes you'll get a message along the lines of:

```
Failed to pull image "grafana/grafana:8.1.2" 
....
429 Too Many Requests - Server message: toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
```

to get around this you need to use your own docker credentials.  

when installing prometheus operator, grafana was having issues pulling the image, so I ended up passing `--set grafana.image.pullSecrets[0]=myregistrykey`  to the helm install command, and then had this script:

```sh
DOCKER_REGISTRY_SERVER=docker.io
DOCKER_USER=<DOCKERUSER>
DOCKER_EMAIL=<DOCKEREMAIL>

echo "Docker Password:"
read DOCKER_PASSWORD

kubectl create secret docker-registry myregistrykey \
  --docker-server=$DOCKER_REGISTRY_SERVER \
  --docker-username=$DOCKER_USER \
  --docker-password=$DOCKER_PASSWORD \
  --docker-email=$DOCKER_EMAIL
```

to create the secret in kubernetes.

## Consul
in the consul helm image the setting is:
```
global:
  imagePullSecrets:
    - name: myregistrykey
```

## Links
* https://newbedev.com/prometheus-operator-helm-chart-code-example
* https://kubernetes.io/docs/concepts/containers/images/#referring-to-an-imagepullsecrets-on-a-pod
