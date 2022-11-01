# kubernetes list cluster versions

`kubectrl version --short` will list out the cluster versions:

if you have the multicluster plugin installed, you can view all your clusters:
`kubectl mc -r prod_us -- version --short`
