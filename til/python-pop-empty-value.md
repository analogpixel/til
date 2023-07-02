# Python return value when list is empty during pop

Retutrn an empty string when you try to pop from a list and there
are no values on it:

```
j = l.pop() if l else ""
```

`if l`: checks for an empty list  
