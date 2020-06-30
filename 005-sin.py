def setup():
  size(1024, 1024)
  background(0)
  stroke(57, 255, 20)
  strokeWeight(10)

def draw():
  translate(0, width / 2)
  point(frameCount, (width / 2 * 0.75) * sin(radians(frameCount)))