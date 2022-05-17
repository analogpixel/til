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



## Order
- `conj` and `into` add to the front of lists
- `conj` and `into` add to the back of vectors
