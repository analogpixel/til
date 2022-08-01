# kubectl forward a port to your local machine

If you have a service/pod running in kubernetes and you wanted
to connect to it from your local machine, you can `port-forward`
to proxy that connection locally to your machine:

`kubectl port-forward service/jenkins-operator-http-example 8080:8080`

`kubectl port-forward <pod-name> <locahost-port>:<pod-port>`

