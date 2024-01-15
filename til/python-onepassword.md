# Get password from onepassword in python

use the one password cli to get a password in python:

Install the Cli:
```
brew install 1password-cli
```

Call the Cli from python:
```
import subprocess

# call out to one password to get the token
output = subprocess.run(["op","read" , "op://VaultName/SecretName/notes"], capture_output=True)
token = output.stdout.decode('utf-8').strip()
```
