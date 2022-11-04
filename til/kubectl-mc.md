# Kubectl mc (multicluster search)

If you need to run a command across multiple kubernetes clusters, this plugin will
allow you to do that:

## Install
```
kubectl krew install mc
```

## Using
- `-r` is a regex to select which contexts/clusters to select from your config
- `-l` just list out all of the contexts/clusters in your config

```
# using clusters with prod_us in their name search for pods in the my-namespace namespace
kubectl mc -r prod_us -- get pods -n my-namespace
```

```
# redeploy a daemonset across all clusters
k mc -r <cluster_match> -- rollout restart daemonset/<my-daemon-set>
```
