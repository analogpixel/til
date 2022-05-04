# Kubernetes pod life cycle

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


## links
* https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/
