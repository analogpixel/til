# JSON gron the grepper for json

[gron](https://github.com/tomnomnom/gron)  can take something that looks like this:

```json
[
  {
    "commit": {
      "author": {
        "date": "2016-07-02T10:51:21Z",
        "email": "mail@tomnomnom.com",
        "name": "Tom Hudson"
      }
    }
  }
]
```

and turn it into something that looks like this:

```
json = [];
json[0] = {};
json[0].commit = {};
json[0].commit.author = {};
json[0].commit.author.date = "2016-07-02T10:51:21Z";
json[0].commit.author.email = "mail@tomnomnom.com";
json[0].commit.author.name = "Tom Hudson";
```

which allows you to see exactly where certiain elements fall in a json document.
