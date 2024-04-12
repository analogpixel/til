# Exercism download all from track


```bash
#!/usr/bin/env bash

set -e
set -u

export track="$1"

curl \
  --silent --fail \
  "https://exercism.org/api/v2/tracks/$track/exercises" \
  | sed 's/"slug":"/\n/g' \
  | sed 's/",.*$//' \
  | grep -v '"exercises":' \
  | while read -r slug; do
      exercism download --track="$track" --exercise="$slug"
    done
```

from here: https://github.com/exercism/cli/issues/718#issuecomment-1493221436
