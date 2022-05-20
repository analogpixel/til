# Clojure working with sequences

- `first` : first element of a sequence 
- `next`  : everything after the first item
- `cons` : add to the front `(cons 0 [1 2 3])`
- `conj` : add an element `(conj '(1 2 3) :a)`
- `into` : add a list `(into [1 2 3] [:a :b :c])` 
- `reverse` : reverse the sequence
- `range` : create a sequence from start to end `(range start end step)`
- `repeate` : create a sequence of n Ys `(repeat n Y)`
- `take` : take n elements from a sequence `(take n sequence)`
- `iterate` : start with x and apply function f forever `(take n (iterate f x))`
- `cycle` : cycle through a collection infinitely `(take 5 (cycle [1 2 3]))` (return 1 2 3 1 2)
- `interleave` : interleaves multiple collections `(interleave whole-numbers ["a" "b" "c"])` (return (1 "a" 2 "b" 3 "c"))
- `interpose` : place a separator between each element `(interpose "," ["a" "b" "c"])` (returns "a" "," "b" "," "c") used with (apply str...)
- `filter` : filter a sequence `(filter #(> % 0) collection)`
- `take-while` : take elements while true `(take-while pred collection)`
- `drop-while` : drop while true `(drop-while pred collection)`
- `split-at`  : split at index `(split-at n collection)`
- `split-with` : split based on predicate `(split-with pred col)`
- `every?` : returns true if all elements in collection are true `(every? pred col)`
- `some` : returns true if one element in collection is true `(some pred col)`
  - `(some #{3} (range 20))` : checks if 3 is in collection
- `not-every?`
- `not-any?`
- `map` : run function on every item of collection `(map fn seq)`
  - map can take multiple collections as arguments `(map #(print %1 %2) col1 col2)`
- `reduce` : run function on first 2 items of collection, and then every item till collection is empty `(reduce + [1 2 3])`
- `sort` : sort a collection `(sort > [1 3 8 4])` (using optional comp?)
- `sort-by` : sort a collection by a function `(sort-by fn col)`
- `for` : `(for [var col filter-expr?] expr)`   `(for [n [1 2 3] :when (odd? n) n)` (:when :while)
  - multiple bindings: `(for [n [1 2 3 4] b "abcd" ] (format "%d%c" n b))` output `("1a" "1b" "1c" "1d" "2a" "2b" "2c" "2d" "3a" "3b" "3c" "3d" "4a" "4b" "4c" "4d"`
- `doall`  : forces clojure to walk all items in the list; no laziness
- `dorun` : force cloure to iterate through all items in a list but doesn't keep last items in memory
- `re-seq` : regex on string and return matches as sequence `(re-seq #"\w+" "the quick brown fox")` <- returns ("the" "quick" "brown" "fox") 
## Order
- `conj` and `into` add to the front of lists
- `conj` and `into` add to the back of vectors

## Other Examples
`(apply str (reverse "hello"))`  olleh

