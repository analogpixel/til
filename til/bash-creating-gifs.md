# Bash creating gifs with ffmpeg and gifsicle

## creating a gif from a series of images
```
ffmpeg  -framerate 59 -i frame-000%3d.png aout.gif

## Speed it up
ffmpeg  -framerate 59 -i frame-000%3d.png -filter:v "setpts=0.3*PTS" aout.gif
```


## Optimizing the gif with gifsicle

```
gifsicle --optimize=9  --resize 400x400 < aout.gif  > out.gif
```
