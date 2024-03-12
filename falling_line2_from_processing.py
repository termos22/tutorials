# Kod dla Python utworzony przez Gemini ze źródła napisanego w Processing.org
# w stanie surowym nie działa. staram się to uruchomić.
# wygląda na to, że wymaga modułu/biblioteki processing-py.

import math
from processing_py import *

angle = 90 # Deklaracja zmiennej
 
def setup(): # Funkcja setup
  App(900, 900) # Ustaw rozmiar okna
  
def draw(): # Funkcja draw
  App.background(0) # Wyczyść ekran
  App.translate(App.width/2, App.height/2) # Przesuń układ współrzędnych do środka okna
  App.stroke(255) # Ustaw kolor i grubość linii
  App.strokeWeight(3) # Pętla rysująca linie
  for i in range(0, 280, 10):
    App.pushMatrix() # Zapisz stan transformacji
    App.rotate(math.radians(i) * math.cos(math.radians(angle))) # Obróć układ współrzędnych
    App.line(200 * math.sin(math.radians(angle)), 0, 0, 200) # Narysuj linię
    App.popMatrix() # Przywróć stan transformacji
  angle += 1 # Zwiększ kąt
 
setup() # Wywołaj funkcję setup
 
while True: # Uruchamia pętlę draw
  draw()
  
  
# Poniżej znajduje się komentaż od Gemini po wygenerowaniu kodu.
#
# Ten kod działa w Pythonie i tworzy ten sam efekt wizualny co kod Processing.
# 
# Główne różnice:
# W Pythonie używamy funkcji math.radians i math.sin zamiast radians i sin.
# Pętla for w Pythonie używa zakresu range(0, 280, 10), który jest równoważny zakresowi 0; i<280; i+=10 w Processing.
# W Pythonie używamy while True: do uruchamiania pętli draw w nieskończoność.
# Oprócz tych różnic, kod jest bardzo podobny w obu językach.