# Python play a sound in macos

`afplay` allows you to play sounds in macos from the commandline, so to play
a sound from python you would:

```python
import subprocess
subprocess.call(["afplay", "bell.mp3"])
```

