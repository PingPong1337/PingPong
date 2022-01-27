import random
import string
from tkinter import *

# Bokstaven för ormens huvud
HEAD_CHAR = "O"
FOOD_CHARS = string.ascii_letters

# Formulär
class Application:
  # sätter upp variablerna 
  TITLE = "Snake"
  SIZE = 300, 300

  def __init__(self, master):
    # Laddar ner variablerna
    self.master = master
    self.head = None
    self.head_position = None
    self.segments = []
    self.segments_positions = []
    self.food = None
    self.food_position = None
    self.direction = None
    self.moved = True
    self.running = False

    # Run the init function
    self.init()

  def init(self):
    self.master.title(self.TITLE)

    # Gör canvasen
    self.canvas = Canvas(self.master)
    self.canvas.grid(sticky=NSEW)

    # Gör start knappen
    self.start_button = Button(self.master, text="Start", command=self.on_start)
    self.start_button.grid(sticky=EW)

    # fäster rörlseknapparna till canvas
    self.master.bind("w", self.on_up)
    self.master.bind("a", self.on_left)
    self.master.bind("s", self.on_down)
    self.master.bind("d", self.on_right)

    # Bestämmer storleken på canvas
    self.master.columnconfigure(0, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.master.resizable(width=False, height=False)
    self.master.geometry("%dx%d" % self.SIZE)

  # När startknappen klickas
  def on_start(self):
    # startar om allt
    self.reset()
    # Ser om spelet redan körs
    if self.running:
      self.running = False
      # Bestämmer vad det ska stå på knappen
      self.start_button.configure(text="Start")
    else:
      self.running = True
      # Bestämmer vad det ska stå på knappen
      self.start_button.configure(text="Stop")
      # Startar spelet
      self.start()

  # starta om funktion
  def reset(self):
    # tar bort ormens kropp
    del self.segments[:]
    del self.segments_positions[:]
    self.canvas.delete(ALL)

  # Start funktionen för spelet
  def start(self):
    # Tar in informationen för canvas (bredd och höjd)
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()

    # Ritar spel skärmen
    self.canvas.create_rectangle(10, 10, width - 10, height - 10)
    self.direction = random.choice('wasd')
    head_position = [round(width / 2, -1), round(height / 2, -1)]
    self.head = self.canvas.create_text(tuple(head_position), text=HEAD_CHAR)
    self.head_position = head_position

    # Ropar efter funktionen för att starta spelet - lägger ut mat och uppdaterar
    self.spawn_food()
    self.tick()

  # Funktion för att lägga fram mat
  def spawn_food(self):
    # hämtar vikt och höjd för canvas
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()

    # letar om mat läggs ut på ormen
    positions = [tuple(self.head_position), self.food_position] + self.segments_positions
    position = round(random.randint(20, width - 20), -1), round(random.randint(20, height - 20), -1)

    # om ny skapad mat överlappar, skapar tills det inte är så
    while position in positions:
      position = round(random.randint(20, width - 20), -1), round(random.randint(20, height - 20), -1)

    # väljer en slumpmässig bokstav
    character = random.choice(FOOD_CHARS)
    self.food = self.canvas.create_text(position, text=character)

    # lagrar den senast skapade bokstaven
    self.food_position = position
    self.food_character = character

  # När timern tickar (uppdaterar spelet)
  def tick(self):
    # hämtar canvas bredd och höjd
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()
    previous_head_position = tuple(self.head_position)

    # rör på ormen
    if self.direction == "w":
      self.head_position[1] -= 10
    elif self.direction == "a":
      self.head_position[0] -= 10
    elif self.direction == "s":
      self.head_position[1] += 10
    elif self.direction == "d":
      self.head_position[0] += 10

    # ser om spelet är över
    head_position = tuple(self.head_position)
    if(head_position[0] < 10 or head_position[0] >= width - 10 or head_position[1] < 10 or head_position[1] >= height - 10 or any(segments_position == head_position for segments_position in self.segments_positions)):
      self.game_over()
      return

    # Ser om ormen äter maten
    if head_position == self.food_position:
      self.canvas.coords(self.food, previous_head_position)
      self.segments.append(self.food)
      self.segments_positions.append(previous_head_position)
      self.spawn_food()

    # Gör så att maten följer ormens huvud
    if self.segments:
      previous_position = previous_head_position
      for index, (segment, position) in enumerate(zip(self.segments, self.segments_positions)):
        self.canvas.coords(segment, previous_position)
        self.segments_positions[index] = previous_position
        previous_position = position

    # Lägger det nya huvudets position i head_position
    self.canvas.coords(self.head, head_position)
    self.moved = True

    # Ändrar nivån (når en högre nivå beroende på ormens längd)
    speed = 100

    if len(self.segments) > 5:
      speed = 75

    if len(self.segments) > 10:
      speed = 60

    if len(self.segments) > 20:
      speed = 45

    # # Ropar efter tick funktionen att uppdatera en gång till efter en viss tid
    if self.running:
      self.canvas.after(speed, self.tick)

    display_speed = 10000 / speed
    self.start_button.configure(text = "Speed: %d" %display_speed)

  # Fuktion för "game over" skärmen
  def game_over(self):
    # Hämtar canvas bredd och höjd
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()

    # Stoppar spelet från att köras
    self.running = False

    # ändrar knappens text till "start"
    self.start_button.configure(text="Start")

    # visar "game over" och resultaten
    score = len(self.segments) * 10
    self.canvas.create_text(round(width/2), round(height/2), text="Game Over! Your score is: %d" %score)

  # Funktion för 4 inputs
  def on_up(self, event):
    if self.moved and not self.direction == "s":
      self.direction = "w"
      self.moved = False

  def on_down(self,event):
    if self.moved and not self.direction == "w":
      self.direction = "s"
      self.moved = False

  def on_left(self, event):
    if self.moved and not self.direction == "d":
      self.direction = "a"
      self.moved = False

  def on_right(self, event):
    if self.moved and not self.direction == "a":
      self.direction = "d"
      self.moved = False

# Bestämmer main loopen (utanför några klasser)
def main():
  root = Tk()
  Application(root)
  root.mainloop()

# Kör appen
if __name__ == "__main__":
  main()