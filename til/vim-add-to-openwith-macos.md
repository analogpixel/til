# Vim add to openwith in macos

Obsidian has a horrible problem in that it autosaves almost every second, and this plays
havoc with cloud storage, so I wanted a way to edit files in vim instead of obsidian.

To do this:

- Open Automator
- Create a new Application
- Add a `Run AppleScript` action, and paste in this code:

```
-- forked version of https://gist.github.com/charlietran/43639b0f4e0a01c7c20df8f1929b76f2

on run {input, parameters}
	set paths to ""
	repeat with i from 1 to length of input
		set cur to item i of input
		set paths to paths & " " & quote & POSIX path of cur & quote
	end repeat
	set cmd to "vim -p" & paths
	tell application "iTerm"
		set created to false
		if not (exists current window) then
			create window with profile "Default"
			set created to true
		end if
		tell current window
			if not created then
				create tab with profile "Default"
			end if
			tell current session
				activate
				write text cmd
			end tell
		end tell
	end tell
end run
```

- Save the file
- right click on a file, and select open with.
- go to wherever you saved you file and use that.

Now if you set this as the default open with, you can now go back to obsidian, and map open with default app to some
swanky key combo, and edit your files in vim.
