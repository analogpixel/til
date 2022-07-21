# Entr reload a program or script on file changes

If you want to watch for file changes and then reload a program when
that happens you can use `entr`:

`find file_to_watch | entr ./program_to_reload`
