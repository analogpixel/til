# Sending a message to google chat in curl

```
url="<URL>"
curl "$url" -X POST -H "Content-Type: application/json" -d '{ "text": "Hello World!" }'
```

To get the URL/Key/Token go to the channel properties -> App & Integration -> Incoming Webhook -> Add Webhook -> Copy the URL and extract the key from it.





