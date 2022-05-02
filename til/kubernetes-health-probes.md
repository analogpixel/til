# Kubernetes health probes

## Liveness Probe

Constatnly run to check if your service is still healthy

```yaml
livenessProbe:
  httpGet:
    path: /actuator/health
    port: 8000
  initialDelaySeconds: 30
```

## Readiness Probe

Run once at startup, used to wait for service to become available

```yaml
readinessProbe:
  exec:
    command: ["stat", "/var/run/myapp.ready"]
```

## links
* https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
