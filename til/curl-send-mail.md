# Curl sending emails

Sometimes curl is all you have to test with on a pod, and you want to send/test email.
Well curl has the ability to connect to a mail server and send an email like telnet
does.

```
curl -vv smtp://<mail-server>:25 --mail-from '<from-email>' --mail-rcpt '<to-email>'
```

then paste in:

```
From: <from-email>
To: <to-email>
Subject: This is a test email

Test
```

then `ctrl-d` to save and send.
