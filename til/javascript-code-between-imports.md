# Javascript Code Between Imports

You can't put code inbetween `import` statements in javascript.  that's why you
see people including a file `import "./jq-global.js";`  that includes code to
import a module and set variables to window.whatever to make it global
