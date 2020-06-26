let tool = 'PEN';
let color = '#000000';
let weight = 4;

function setup() {
  const canvas = createCanvas(windowWidth, windowHeight);
  canvas.parent('canvasContainer');
  background('white');

  brushSize = createSlider(0, 10, weight, 1);
  penButton = createButton('PEN');
  fillButton = createButton('FILL');
  eraseButton = createButton('ERASE');
  saveButton = createButton('SAVE');

  penButton.mousePressed(() => {tool = 'PEN';});
  fillButton.mousePressed(() => {tool = 'FILL';});
  eraseButton.mousePressed(() => {tool = 'ERASE';});

  saveButton.mousePressed(() => {
    saveCanvas(canvas, 'myCanvas', 'jpg');
  });

  [brushSize, penButton, fillButton, eraseButton, saveButton].forEach((item, index) => {
    item.position(10, 10 + index * 30);
  });

  colorPicker = createColorPicker(color);
  colorPicker.position(width - 60, 10);
}

function draw() {
  noErase();

  color = colorPicker.color();
  weight = brushSize.value();

  fill(color);
  stroke(color);
  strokeWeight(weight);

  if (mouseIsPressed) {
    switch(tool) {
      case 'PEN':
        line(mouseX, mouseY, pmouseX, pmouseY);
        break;
      case 'FILL':
        rect(0, 0, width, height);
        break;
      case 'ERASE':
        erase();
        line(mouseX, mouseY, pmouseX, pmouseY);
        break;
    }
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
