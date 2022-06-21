# Prometheus alertmanager send test alert

Instead of sitting around waiting for an alert to happen if you happen
to be testing routing rules in alertmanager, you can can force an alert 
to happen:

```
#! /usr/bin/env sh

URL="http://<IP_TO_ALERT_MANAGER_SERVICE>/api/v1/alerts"

curl -si -X POST -H "Content-Type: application/json" "$URL" -d '
[
  {
    "labels": {
      "alertname": "INFO test alert",
      "instance": "localhost:8080",
      "job": "node",
      "severity": "INFO"
    },
    "annotations": {
      "summary": "Test an INFO level"
    },
    "generatorURL": "http://localhost:9090/graph"
  }
]
'
```

Alerts in alertmanager will clear automatically after a few minutes if it doesn't continue to get the alert.

## links
* https://blog.mafr.de/2020/09/13/testing-alertmanager/
