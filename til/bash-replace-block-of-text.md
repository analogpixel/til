# Bash replace a block of text

if you have a block in a text file that you would want to update with a script:

```
%% start_section %%
stuff here
stuff here
%% end_section %%
```

you can do this:

```bash
(
  grep --before-context 99999999 "%% start_section %%" /tmp/my_source_file
  cat /tmp/add_this_content
  grep --after-context 9999999 "%% end_section %%" /tmp/my_source_file
) > /tmp/output
mv /tmp/output /tmp/my_source_file
```

it looks dirty, but is much more reliable and understanable than most solutions that use sed/awk/perl,
expecially when your content has new lines in it. 
