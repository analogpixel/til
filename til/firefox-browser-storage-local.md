# Firefox browser.storage.local

## Put value in local storage
`[key]`  is a [computed property name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)  if you had just `key`  it would just use the string `key` for the key,  but if you want it to resolve to the variable stored in `key` then you need to use computed property names.
```javascript
  var storingNote = browser.storage.local.set({ [key] : value });
  storingNote.then(() => {
     console.log("Note stored");
  }, onError);
```


## get a value and check if it exists
```javascript
rating =  (await browser.storage.local.get(key));

if (key in rating) {
  console.log("Found it");
} else {
  console.log("Not found");
}
```

## links
- https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage
