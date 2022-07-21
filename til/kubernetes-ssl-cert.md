# Kubernetes load a ssl cert into secrets

To add an ssl cert to a secret you can run this:

`kubectl create secret tls release_name-ingress-tls-secret --cert=./certificate.pem --key=./key.pem [--namespace namespace]`

