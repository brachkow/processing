def setup():
  size(512,512)
  rectMode(CENTER)
  noStroke()

def draw():
  clear()
  background(255)
  side = width / 2

  for i in range(0, 13):
    pushMatrix()
    translate(width / 2, height / 2)
    if (i % 2 != 0):
      fill(255);
    else:
      fill(0);
    rotate(radians(frameCount) * 2 * pow(-1, i))
    rect(0, 0, side, side)
    popMatrix()
    side = side / sqrt(2)