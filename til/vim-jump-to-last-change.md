# Vim Jump to your last change

- `'.` will jump to the last place you edited. So now when you open a file `g,` and `g;` will also work
- `g:` and `g,` will also move you around in the change list (forward and backwards)
- `gi` jumps to the last edit and puts you in insert mode.

## Just do it on every load
```vim
" Return to last edit position when opening files (You want this!)
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif
```

## links
- https://vi.stackexchange.com/questions/2001/how-do-i-jump-to-the-location-of-my-last-edit
