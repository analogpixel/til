# kubernetes roll out new image

to have your kubernetes deployment roll out a new image, first make sure your
manifest is configured correctly:

```yaml
imagePullPolicy: Always
```

and Using images tagged `:latest`

then you can either delete the pod and have it recreate, or:

```sh
kubectl rollout restart deployment/<name>  
```

if you want to do this across multiple clusters with the kubectl mc plugin,
then you could delete the pods using a label selector:

```
kubectl delete pod -l app=myapp
```

or you could use the above rollout syntax
