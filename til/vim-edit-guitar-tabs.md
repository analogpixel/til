# Editing Guitar Tabs in Vim

Add this to your .vimrc:

```
:autocmd BufNewFile  *.tab      0r ~/.vim/skeleton/tabs
:autocmd BufNew,BufEnter *.tab set virtualedit=all 
" use R (replace mode) to edit the tabs
```

and then create the file `~/.vim/skeleton/tabs` with this content:

```
e|-----------------|-----------------|-----------------|-----------------|
B|-----------------|-----------------|-----------------|-----------------|
G|-----------------|-----------------|-----------------|-----------------|
D|-----------------|-----------------|-----------------|-----------------|
A|-----------------|-----------------|-----------------|-----------------|
E|-----------------|-----------------|-----------------|-----------------|
```

Now instead of going into insert mode with `i`  go into replace mode with `R`
and make your edits

- by default vim doesn't allow you to move into locations that don't have
characters or spaces in them already, but `virtualedit=all`  changes that 
so you can navigate anywhere on the screen and put in text if you want.
- the above config only activates if the files ends in `.tab`  

## Common Tab Symbols

- `h` or `^` 	hammer on
- `p` or `^` 	pull off
- `b` bend string up
- `r` release bend
- `/` slide up
- `\` slide down
- `v` or `~` vibrato
- `t` right hand tap
- `x` play 'note' with heavy damping
