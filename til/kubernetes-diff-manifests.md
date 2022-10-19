# kubernetes diff 2 manifest files

Dump the manifest with: `kubectl get pods .... -o json > manifest.json`

and then diff them with: `difft <(jq --sort-keys . manifest1.json ) <(jq --sort-keys . manifest2.json )`

## Links
- https://github.com/Wilfred/difftastic or `brew install difftastic`

