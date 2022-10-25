# P5.JS perfect gif loop

So when you run execute the SaveGif function it will reset frameCount to 0, and
start recording the gif.  In the code below, `t` will be between 0 and 1 during
the animation.

```javascript
nFrames = 100;
t = 0;

function setup(){createCanvas(600,600)};

function draw(){
t = 1.0*frameCount/nFrames;
background(0);
translate(300,300);
x = 200*sin(TAU*t);
y = 200*cos(TAU*t);
circle(x,y,20);
}

function keyPressed() {
  if (key === 's') {   
    saveGif('mySketch', nFrames, {delay:0,units:'frames'} );
  }
}
```

## Links
- [src](https://twitter.com/incre_ment/status/1584337643290050562)
- [frame count](https://p5js.org/reference/#/p5/frameCount)
- [TAU](https://p5js.org/reference/#/p5/TAU)  : alias for TWO_PI
- [saveGif](https://p5js.org/reference/#/p5/saveGif)
