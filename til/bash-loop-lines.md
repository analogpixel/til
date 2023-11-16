# Bash loop over lines and get columns

if you want to loop over data like this:

```
cluster-name        region-west1  1.25.10-gke.2700  IP   n2d-standard-16  1.25.10-gke.2700  6          RUNNING
```

and get certain columns, this loop will do that:

```bash
while read -r col1 col2 rest; do
  echo "$col1 col2"
done << `command to return data to parse`
```


## Script to login to all GKE clusters and login

```bash
while read -r cluster_name region rest; do
  gcloud container clusters get-credentials ${cluster_name} --region ${region} --project <PROJECT_NAME>
done <<< `gcloud container clusters list | grep -v STATUS`

```
