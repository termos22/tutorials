import math
from processing_py import *

angle = 90
app = App(900, 900)

def draw():
  app.background(0,0,0)
  app.translate(app.width/2, app.height/2)
  app.stroke(255)
  app.strokeWeight(3)
  for i in range(0, 280, 10):
    app.pushMatrix()
    app.rotate(math.radians(i) * math.cos(math.radians(angle)))
    app.line(200 * math.sin(math.radians(angle)), 0, 0, 200)
    app.popMatrix()
  angle += 1


while True:
  draw()
