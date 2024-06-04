# Regex named character sets

```
[:digit:]	[0-9]
[:lower:]	[a-z]
[:upper:]	[A-Z]
[:alpha:]	[a-zA-Z]
[:alnum:]	[0-9a-zA-Z]
[:xdigit:]	[0-9a-fA-F]
[:cntrl:]	control characters — first 32 ASCII characters and 127th (DEL)
[:punct:]	all the punctuation characters
[:graph:]	[:alnum:] and [:punct:]
[:print:]	[:alnum:], [:punct:] and space
[:blank:]	space and tab characters
[:space:]	whitespace characters, same as \s
```

character classes need to be in a regex character class [] , `[[:space:]]`

