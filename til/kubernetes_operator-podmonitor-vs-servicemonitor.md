# Prometheus-operator Pod Monitors vs. Service Monitors

in prometheus opertor, a service monitor will scrape ALL the pods behind the service (it does NOT just scrape from the kubernetes service once.)   So it works
kind of like the pod monitor, except pod monitor doesn't require a service to do the scraping.

# links
* https://github.com/prometheus-operator/prometheus-operator/issues/3119

