# P5.js dynamic mask


I wanted to apply a gradient to moving blobs in processing.  At first
I was just going to do a pixel to pixel copy from source->dest  but since
I was doing transforms and xy from one side didn't match up to the 
other side that got messy.  So instead, I rendered the blobs as a mask, 
and then applied that mask to the gradient.

```javascript
let mask;
let img;

void setup() {
  // https://stackoverflow.com/a/51214735
  // works around bug
  pixelDensity(1);

  createCanvas(400, 400);
  mask = createGraphics(400, 400);
}


void draw() {

  // create your dynamic mask here
  mask.pixelDensity(1);
  mask.clear();

  // p5js uses alpha to determine what is masked and what is not.
  // and alpha of 255 means no mask, and an alpha of 0 means all mask.
  mask.fill('blue');
  mask.circle(0,0, 10,10);

  // erase the screen
  background(255);

  // masks are cumulative, so you have to reset it each time
  var newImg = createImage(400, 400);
  newImg.copy(img,0,0, width,height, 0,0, width,height);

  newImg.mask(mask);

  // diplay the masked image
  image(newImg,0,0);
}
```
