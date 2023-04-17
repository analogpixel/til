# Bash creating gifs with ffmpeg and gifsicle

## creating a gif from a series of images
```
ffmpeg  -framerate 59 -i frame-000%3d.png aout.gif

## Speed it up
ffmpeg  -framerate 59 -i frame-000%3d.png -filter:v "setpts=0.3*PTS" aout.gif
```

## Creating from a quicktime movie

this create a gif from a motion movie with transparent background it also speeds it up by 2:

```
ffmpeg -i motion_animation.mov -filter_complex "[0:v]setpts=0.5*PTS,split[v0][v1];[v0]palettegen[p];[v1][p]paletteuse" -r 15 -y output.gif
```


## Optimizing the gif with gifsicle

```
gifsicle --optimize=9  --resize 400x400 < aout.gif  > out.gif
```
