# Python set theory

working on sets in python:

* `|` or `.union(set2)` :  the set consisting of all elements from set 1 and set 2
* `&` or `.intersection(set2)`: the set of items that are shared between set 1 and set 2
* `-` or `.difference(set2)` : all the elements that are in set 1 but not in set 2
* `^' or '.symmetric_difference(set2)` : all the elements that are in set 1 and set 2, but not both.
* `.isdisjoint(set2)` : return True if set 1 and set 2 have no elements in common.
* `<` or `.issubset(set2)` : return True if all of set 1 is included in set 2.
* `>=` or `.issuperset(set2)` : return True if set 1 contains all the elements of set 2.
