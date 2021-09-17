# How to clean up logs with Java Stack Traces in them

When you are looking at logs that have java stack traces, the traces can be hundreds of lines to scroll through,  so this awk awk comand
will truncate the stack trace to only a few lines in the log file:

`awk '/^20..-*/ {ll=0} // { ll++; if (ll < 5) print $0 }' application.log`

## links
* https://www.gnu.org/software/gawk/manual/gawk.html
