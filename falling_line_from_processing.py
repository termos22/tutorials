from processing_py import *


app = App(900, 900)

def draw():
  angle = 90
  app.background(0)
  app.translate(app.width/2, app.height/2)
  app.stroke(255)
  app.strokeWeight(3)
  for i in range(0, 280, 10):
    app.pushMatrix()
    app.rotate(radians(i) * app.cos(app.radians(angle)))
    app.line(200 * app.sin(app.radians(angle)), 0, 0, 200)
    app.popMatrix()
    app.redraw()
    angle += 1


while True:
  draw()
