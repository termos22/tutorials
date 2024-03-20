import processing

class Sketch(processing.app.Sketch):

    def settings(self):
        self.size(900, 900)
        self.frameRate(30)

    def setup(self):
        self.background(0)
        self.stroke(255)
        self.strokeWeight(3)

    def draw(self):
        self.translate(self.width/2, self.height/2)
        for i in range(0, 280, 10):
            self.pushMatrix()
            self.rotate(self.radians(i) * self.cos(self.radians(self.angle)))
            self.line(200 * self.sin(self.radians(self.angle)), 0, 0, 200)
            self.popMatrix()
        self.angle += 1

if __name__ == '__main__':
    sketch = Sketch()
    sketch.run()