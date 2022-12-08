# Python read in a matrix

if you have data in a file like this:

```
30373
25512
65332
33549
35390
```

you can read it in with this:

```python
[ [int(y) for y in x] for x in [ list(x.strip()) for x in open("input").readlines() ]]
```

this will give you this:

```
[[3, 0, 3, 7, 3],
 [2, 5, 5, 1, 2],
 [6, 5, 3, 3, 2],
 [3, 3, 5, 4, 9],
 [3, 5, 3, 9, 0]]
 ```
