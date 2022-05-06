# Kubernetes pod placement

## Node Selector

Pod can only be scheduled on nodes that match the node selector.

```yaml
nodeSelector:
  disktype: ssd
```

## Node Affinity

more robust syntax:

* requiredDuringSchedulingIgnoredDuringExecution
* preferredDuringSchedulingIgnoredDuringExecution

```yaml
affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/os
            operator: In
            values:
            - linux
```

## Pod Affiniity and Anitaffinity

* affinity: find pods with the matching labels and put them on the same node.
* antiaffinity: find pods with the match labels and don't put them on the same node.

prevent pods from scheduling on the same node  (should you use a deamonset?)
```yaml
podAntiAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
  - labelSelector:
      matchExpressions:
      - key: app
        operator: In
        values:
        - nginx
    topologyKey: kubernetes.io/hostname
```

## Tains and Tolerations

* First you taint the node
* Then you add a toleration on the pod to allow it to run on a tainted node.
* don't forget to use node selectors or something else, or the pod could go anywhere else, this just prevents pods without the tolerations from running on this node.

### Node

```sh
# add taint
kubectl taint nodes node1 key1=value1:NoSchedule

# remove tain
kubectl taint nodes node1 key1=value1:NoSchedule-
```

### Pod

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
```

## Links
* https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
* https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
