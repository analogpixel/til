# JQ examples

- Sort an array and return the first object: `echo '["zzz", "xxx", "aaa"]' | jq 'sort[0]'`
- function to remove white space: `def trim: sub("^\\s+"; "") | sub("\\s+$"; "");`
- split a string on `]:` get the first item and then convert the case to lowercase: `split("]:")[0] | trim | .[1:] | ascii_downcase`
- add a default vaule if `.name` is null: `(.name // "default_name")`
- find values >= 5 and return the number of them: `. | map(select( . >=5)) | length `

