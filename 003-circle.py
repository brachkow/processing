def setup():
    size(2048,2048)
    ellipseMode(CENTER)
    background(255)

def draw():
  r = width / 2
  translate(r, r)
  x = r / 2 * sin(radians(frameCount % 360)) * cos(frameCount)
  y = r / 2 * cos(radians(frameCount % 360))
  d = width * 0.1
  ellipse(x, y, d, d)
  if (frameCount <= 180):
    saveFrame()