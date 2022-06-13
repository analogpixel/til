# Python a functional decimal to hex conversion

Reading this months 2600, they had an article about the BACnet protocol, which 
uses UDP port 47808, since 47808 in HEX is BAC0.  Being rusty on my Decimal To Hex,
I wrote a little python program:

```python
a = 47808
while a > 0:
    (a,h) = divmod(a,16)
    print("{},{:x}".format(a,h))
```

But then I was wondering if there was a more "functional" way of doing this, and
found a code golf entry that looked like this:

`h = lambda x: (x > 15 and h(x//16) or '') + "0123456789abcdef"[x%16]`

What it's doing is building a recursive function that:

- h(47808)
  -  `47808 > 15`, so recurse in with `47808//16`  # // to strip off the remained and be left with an int.
    - `2988 > 15`, so recurse in with `2988//16`
      - `186 > 15`, so recurse in with `186//165`
        - `11` is not greater than `15`, so return an empty string '' appended to (+) the `11%16`th element (11) of `"0123456789abcdef"` which is b
      - `186 % 16` is `10` so append `"0123456789abcdef"[10]` (a)
    - `2988 % 16` is `12` so append `"0123456789abcdef"[12]` (c) 
  - `47808 % 16` is `0` so append `"0123456789abcdef"[0]` (0)
- return `bac0`

Digging into [Python's Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)  you can see that and is evaluated
first, so you can have ands all day `a and b and c`  and the final `or` won't be picked up until one of those `and`s fail.  

## Links
* https://codegolf.stackexchange.com/a/68249

