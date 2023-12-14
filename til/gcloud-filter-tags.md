# gcloud container registry list images filter by tag name

## list all images that don't have the latest tag.
`gcloud container images list-tags <image-name> --format=json --filter "tags != latest"`
