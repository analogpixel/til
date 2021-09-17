# How to clean up logs with Java Stack Traces in them

When you are looking at logs that have java stack traces, the traces can be hundreds of lines to scroll through,  so this awk comand
will truncate the stack trace to only a few lines in the log file:

`awk '/^20..-*/ {ll=0} // { ll++; if (ll < 5) print $0 }' application.log`

the `^20..` part is looking for the start of a normal log line (in the case the date 2021-....blah)  and then setting the counter to 0. For
every line the counter gets incremented, and after so many lines of no date, it just stops printing the lines until it sees a date again.

## links
* https://www.gnu.org/software/gawk/manual/gawk.html
