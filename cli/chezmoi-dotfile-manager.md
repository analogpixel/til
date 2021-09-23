# Chezmoi dotfile manager

you can use [chezmoi](https://github.com/twpayne/chezmoi/blob/master/docs/QUICKSTART.md)  to manage your dot files across multiple machines.


## Common commands
* `chezmoi edit` ~/.vimrc  ( edit a file in the repo )
* `chezmoi apply`  ( apply files in repo to your local filesystem ) 
* `chezmoi update` ( pull changes from git and apply them )

## Autopush changes to git
add this:

```
[git]
    autoCommit = true
    autoPush = true
```

to your `~/.config/chezmoi/chezmoi.toml`

