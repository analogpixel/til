# Macos Font smoothing

After getting 2 new monitors for my macbook I was noticing some programs,
firefox especially, had horrible font rending.  Turns out Apple doesn't always
approve of buying non-retina displays fixes need to be put in place to get font
smoothing back in applications like firefox:

from the terminal run:

```sh
defaults write -g CGFontRenderingFontSmoothingDisabled -bool NO
defaults -currentHost write -globalDomain AppleFontSmoothing -int 2
```

And then reboot.  The AppleFontSmoothing can be adjusted from 1 up to 3.


## Links
* https://www.reddit.com/r/firefox/comments/acyuz6/if_fonts_look_bad_on_external_monitor_using_macos/
* https://colinstodd.com/posts/tech/fix-macos-catalina-fonts-after-upgrade.html
