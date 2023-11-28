# gcloud check is oslogin is enabled.

Check which machines are running oslogin:

`gcloud compute instances list --filter=“metadata.items.key[‘enable-oslogin’][‘value’]=‘true’”`
