# Slack bolt python ack a message

You have 3 seconds to respond to a message before slack times out.  So you need
to send an `ack()` before you do any heavy processing.  Unfortunately slack refuses 
to publish how to do this because they hate people.  this is how you ack() a message
caught using `@app.message...`

```
@app.message(re.compile("match message",re.IGNORECASE) )
def get_rally_story(message,say,ack):
     ack()
```
