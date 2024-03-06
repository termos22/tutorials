import math

# Deklaracja zmiennej
angle = 90

# Funkcja setup
def setup():
  # Ustaw rozmiar okna
  size(900, 900)

# Funkcja draw
def draw():
  # Wyczyść ekran
  background(0)
  # Przesuń układ współrzędnych do środka okna
  translate(width/2, height/2)
  # Ustaw kolor i grubość linii
  stroke(255)
  strokeWeight(3)
  # Pętla rysująca linie
  for i in range(0, 280, 10):
    # Zapisz stan transformacji
    pushMatrix()
    # Obróć układ współrzędnych
    rotate(math.radians(i) * math.cos(math.radians(angle)))
    # Narysuj linię
    line(200 * math.sin(math.radians(angle)), 0, 0, 200)
    # Przywróć stan transformacji
    popMatrix()
  # Zwiększ kąt
  angle += 1

# Wywołaj funkcję setup
setup()

# Uruchamij pętlę draw
while True:
  draw()
  
# Ten kod działa w Pythonie i tworzy ten sam efekt wizualny co kod Processing.
# 
# Główne różnice:
# W Pythonie używamy funkcji math.radians i math.sin zamiast radians i sin.
# Pętla for w Pythonie używa zakresu range(0, 280, 10), który jest równoważny zakresowi 0; i<280; i+=10 w Processing.
# W Pythonie używamy while True: do uruchamiania pętli draw w nieskończoność.
# Oprócz tych różnic, kod jest bardzo podobny w obu językach.