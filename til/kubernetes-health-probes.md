# Kubernetes health probes

## Liveness Probe

Indicates whether the container is running. If the liveness probe fails, the kubelet kills the container

```yaml
livenessProbe:
  httpGet:
    path: /actuator/health
    port: 8000
  initialDelaySeconds: 30
```

## Readiness Probe

Indicates whether the container is ready to respond to requests. If the readiness probe fails, the endpoints controller removes the Pod's IP address from the endpoints of all Services that match the Pod.

```yaml
readinessProbe:
  exec:
    command: ["stat", "/var/run/myapp.ready"]
```

## Startup Probe

Indicates whether the application within the container is started. All other probes are disabled if a startup probe is provided, until it succeeds. If the startup probe fails, the kubelet kills the container

``yaml
startupProbe:
  httpGet:
    path: /healthz
    port: liveness-port
  failureThreshold: 30
  periodSeconds: 10
```

## options
* failureThreshold: When a probe fails, Kubernetes will try failureThreshold times before giving up. 
* successThreshold: Minimum consecutive successes for the probe to be considered successful after having failed. 
* timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1
* periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
* initialDelaySeconds: Number of seconds after the container has started before liveness or readiness probes are initiated. Defaults to 0 seconds. Minimum value is 0.

## links
* https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
* https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes
