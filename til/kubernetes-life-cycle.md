# Kubernetes pod life cycle start/stop hooks

## Start Hooks

Kubernetes sends the postStart event immediately after the Container is created. There is no guarantee, however, that the postStart handler is called before the Container's entrypoint is called. The postStart handler runs asynchronously relative to the Container's code, but Kubernetes' management of the container blocks until the postStart handler completes. The Container's status is not set to RUNNING until the postStart handler completes.

```yaml
lifecycle:
  postStart:
    exec:
      command:
        - sh
        - -c
        - sleep 30
```

## Stop Hooks

Kubernetes sends the preStop event immediately before the Container is terminated. Kubernetes' management of the Container blocks until the preStop handler completes, unless the Pod's grace period expires. For more details, see Pod Lifecycle.

```yaml
lifecycle:
  preStop:
    httpGet:
      port: 8080
      path: /shutdown
```

## Signals when stopping a pod
* when you stop a pod it first gets a SIGTERM signal
* 30 seconds after the SIGTERM  the process gets a SIGKILL signal

`.spec.terminationGracePerioudSeconds `  can set this time, but isn't always honored.


## Init Containers

* initContainers is an array; you can have many
* Init containers always run to completion.
* Each init container must complete successfully before the next one starts.
* If a Pod's init container fails, the kubelet repeatedly restarts that init container until it succeeds. However, if the Pod has a restartPolicy of Never, and an init container fails during startup of that Pod, Kubernetes treats the overall Pod as failed.

An example where the init container shares a volume with the other container 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-demo
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
    volumeMounts:
    - name: workdir
      mountPath: /usr/share/nginx/html
  # These containers are run during pod initialization
  initContainers:
  - name: install
    image: busybox:1.28
    command:
    - wget
    - "-O"
    - "/work-dir/index.html"
    - http://info.cern.ch
    volumeMounts:
    - name: workdir
      mountPath: "/work-dir"
  dnsPolicy: Default
  volumes:
  - name: workdir
    emptyDir: {}
```

## links
* https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/
* https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/#create-a-pod-that-has-an-init-container
