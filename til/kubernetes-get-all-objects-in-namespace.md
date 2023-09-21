# kubernetes get all objects in a namespace

`kubectl get all -A` or `kubectl get all -n` only does a very small subset of things, and doesn't include CRDs.  The following
bash function will list all objects in a namespace:

```
function kubectlgetall {
  for i in $(kubectl api-resources --verbs=list --namespaced -o name | grep -v "events.events.k8s.io" | grep -v "events" | sort | uniq); do
    z=$(kubectl -n ${1} get --ignore-not-found ${i})
    if [[ -n "$z" ]] ; then
      echo "Resource:" $i
      echo -e "$z"
      echo "----"
    fi
  done
}
```
