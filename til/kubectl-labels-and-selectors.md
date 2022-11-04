# kubectl labels and selectors

You can NOT use pattern matching to select pods, but you can use labels

`kubectl get pods -l name=my-pod-name`  

look in the metadata section of your app to see what labels it has you can select from.

https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
