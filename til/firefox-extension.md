# Firefox extensios 

WIP

Reason: add functionality to firefox

## Logs
- `command-shift-j`  will show the browser console which will show console message

## create a new extension 
- create a directory for the extension
- create manifest.json:

### manifest.json
```json
{

  "manifest_version": 2,
  "name": "Borderify",
  "version": "1.0",

  "description": "Adds a red border to all webpages matching mozilla.org.",

  "icons": {
    "48": "icons/border-48.png"
  },

  # define what this is allowed to do
  "permissions": [
    "activeTab",
    "storage"
  ],

  # browser_actions are popups that get input
  "browser_action": {
    "default_icon": "icons/web-ack-48.png",
    "default_title": "web-ack",
    "default_popup": "popup/pop.html"
  },

  # content_scripts just run when a page loads
  "content_scripts": [
    {
      "matches": ["*://*.mozilla.org/*"],
      "js": ["borderify.js"]
    }
  ]

}
```

## links
- [firefox docs getting started](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension)
- [webext](https://extensionworkshop.com/documentation/develop/getting-started-with-web-ext/)  tool to help make plugins 
