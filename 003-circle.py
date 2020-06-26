def setup():
  size(512,512)
  ellipseMode(CENTER)
  background(255)

def draw():
  r = width / 2
  translate(r, r)
  x = r / 2 * sin(radians(frameCount)) * cos(frameCount)
  y = r / 2 * cos(radians(frameCount))
  d = width * 0.1
  ellipse(x, y, d, d)