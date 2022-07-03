# GoogleCloud Logs

If you don't query correctly it'll go to slow to get any results.

## who deleted a secret from GKE
```
logName="projects/<PROJECT-TO-SEARCH>/logs/cloudaudit.googleapis.com%2Factivity" AND
resource.type="k8s_cluster" AND
resource.labels.cluster_name="<GKE-CLUSTER>" AND 
proto_payload.method_name=~"io.k8s.core.v1.secrets.*" AND
proto_payload.resource_name="core/v1/namespaces/splunk/secrets/splunk-admin-secret"
```
## Links
- https://cloud.google.com/logging/docs/view/logging-query-language
