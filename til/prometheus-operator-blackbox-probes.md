# prometheus operator blackbox probes

This document explains how to setup checks that will login to a service 
requiring an api key to make sure it's returning valid data (200 status code)  

**This document version:** 1.0.0 
**Last updated:** 2022-08-24

## Authenticating to services
- the `Authorization: Bearer <token>` http header can be used to auth to a service

Once you have an API key for a service , there are a few ways to pass it to the application, but 
the easiest is just including it in the `Authorization: Bearer <token>` http header.

On you blackbox configuration, this looks like this:
```
  http_2xx_api:
    prober: http
    http:
      tls_config:
        insecure_skip_verify: true
      bearer_token_file: /var/api-key/api-key
```


## Probing a Service from prometheus operator (PO)
- the `Probe` CRD is used to call blackbox checks from prometheus operator.

To Create a blackbox check in PO, you use the Probe CRD.  Here is an example of
what that would look like:

```yaml
kind: Probe
apiVersion: monitoring.coreos.com/v1
metadata:
  name: running-check
  namespace: my-app
spec:
  interval: 60s
  module: http_2xx_api
  prober:
    url: blackbox.default.svc.cluster.local
  targets:
    staticConfig:
      static:
      - "https://myapp.namespace.svc.cluster.local/check
```

note that the module is set to `http_2xx_api` which is our pre-defined module that
has the api key already embedded in it, and `prober` points to the local
blackbox service running in the cluster.

The static urls, are the urls blackbox will try to get to and return the status. The
Status will be returned in the metric `probe_http_status_code` and you are probably
looking for a status of 200.

The static url above is using the [kubernetes dns names](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) to connect to the service local to the
blackbox check on the cluster. 

A sample prometheus query for the above config would look like: `probe_http_status_code{job="probe/default/running-check"}`

## Debugging prometheus operator probes
- `kubectl get probes -A`
- prometheus ui->targets->your probe name

There are a few places you can check to see if your probe is working. `kubectl get probes -A` should 
list all the probes in the cluster you are pointing to (or :probes in k9s will pull them up).  You can use
this to make sure your probe is configured the way you want.

You can also go to the prometheus http ui and go to targets and then search for your probe name and see if prometheus
is running it correctly.

## Alerting on your probes
- the `PrometheusRule` CRD is used to setup alerts 
  
Once you are checking your service, you'll probably want to alert on it.  This is done by creating a PrometheusRule:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    app: myapp
  name: myapp-check-app
spec:
  groups:
  - name: myapp-check-login
    rules:
    - alert: "myapp service returning non 200 return code"
      for: 5m
      labels:
        app: myapp
      expr: "probe_http_status_code{job=\"probe/default/myapp-running-check\"} != 200"
```

## Links
- [black box config syntax](https://github.com/prometheus/blackbox_exporter/blob/master/CONFIGURATION.md)
- [prometheus operator blackbox docs](https://prometheus-operator.dev/docs/kube/blackbox-exporter/)
- [prometheus operator blackbox probe syntax](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md#probe)
- `kubectl explain probe` (or install the [explore plugin](https://github.com/keisku/kubectl-explore) and use that)
- [kubernetes dns names](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

