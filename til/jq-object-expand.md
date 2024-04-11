# JQ object expansion 


When JQ encounters a stream (.[]) in an object, it will expand all possible
values of that object:

```
echo '{"a": 3, "b": [4, 5]}' | jq ' {"key": .b[], "value": .a}'
{
  "key": 4,
  "value": 3
}
{
  "key": 5,
  "value": 3
}
```

By using .b[], jq treats each element of the array b as a separate value in the stream and
breaks them out into separate objects.


an example of this can be seen [here](https://exercism.org/tracks/jq/exercises/etl/solutions/IsaacG)
