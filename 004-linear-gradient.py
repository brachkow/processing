def setup():
  size(512,512)
  
  # start point color
  r1 = 100
  g1 = 100
  b1 = 255

  # end point color
  r2 = 120
  g2 = 200
  b2 = 150

  colorMode(RGB)
  for x in range(1, width):
    rt = r1 - (r1 - r2) * map(x, 0, 512, 0, 1)
    gt = g1 - (g1 - g2) * map(x, 0, 512, 0, 1)
    bt = b1 - (b1 - b2) * map(x, 0, 512, 0, 1)

    stroke(rt, gt, bt)
    line(x, 0, x, height)