# Kind local docker registry

How to create and use a local docker registy with kind:

## Create the registy

### Cluser config
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
containerdConfigPatches:
- |-
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."localhost:5000"]
    endpoint = ["http://kind-registry:5000"]
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 8090
    hostPort: 8090
    listenAddress: "0.0.0.0"
    protocol: tcp
```

### Setup registry
```bash
#!/usr/local/bin/bash

# create registry container unless it already exists
if ! docker ps | grep kind-registry
then
  echo "Creating Local Registry"
  reg_name='kind-registry'
  reg_port='5000'
  running="$(docker inspect -f '{{{{.State.Running}}}}' "${reg_name}" 2>/dev/null || true)"
  if [ "${running}" != 'true' ]; then
    docker run \
      -d --restart=always -p "127.0.0.1:${reg_port}:5000" --name "${reg_name}" \
      registry:2
  fi
fi
```

## Using the registy
```bash
docker build -t localhost:5000/hello-app:1.0
docker push localhost:5000/hello-app:1.0
```


