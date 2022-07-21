# Entr reload a program or script on file changes

If you want to watch for file changes and then reload a program when
that happens you can use [entr](https://github.com/eradman/entr):

`find file_to_watch | entr ./program_to_reload`

if the app you are running is a server use `-r`

`find file_to_watch | entr -r ./program_to_reload`
