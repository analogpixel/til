# Kubectl specify context per command

If you want to specify the context on just the kubectl command
and not globally for the session, you can use `--context`

`kubectl --context kind  apply -f deploy.yml`
