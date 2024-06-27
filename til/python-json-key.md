# Python get nested JSON/dict key from path

Sample code to get a nested value from a dict or json blob.  This will return an array
since some values could be inside of lists.

```
def getPath(json_data, path):
    """
    given json data in a python dict, and a path into that data, recurse into the 
    data and return the result(s).  If nothing is found
    at that path, return [] otherwise return a list of results.
    """
    keys = path.split('.')

    def traverse(json_data, keys):

        if not keys:
            return [json_data]

        key = keys[0]

        if key in json_data:
            t = type(json_data[key])
            if t == dict:
                return traverse(json_data[key], keys[1:])
            elif t == list:
                r = []
                for item in json_data[key]:
                    r.extend( traverse(item, keys[1:]) )
                return r
            else:
                return [json_data[key]]
        else:
            return []

    return traverse(json_data, keys)

```
