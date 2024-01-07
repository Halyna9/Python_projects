import os
import time
import random 

SNOW_DENSITY = 7    # percentage of density
DELAY = .3          #seconds

snowflakes = ["*", "❅", "❄", "+", "❆", "@"]

terminal = os.get_terminal_size()
width = terminal.columns
hight = terminal.lines

grid = []

for _ in range (hight):
    grid.append(" " * width)

def draw_grid():
    os.system("cls" if os.name == "nt" else "clear")

    print("\033[?25l") #clear cursor from the terminal

    output = " "
    for row in grid:
        output += "".join(row) + "\n"

    output = output.strip("\n")
    print(output, end = "")

while True:

    row = []

    for _ in range(width):
        if random.random() < SNOW_DENSITY /100:
            row.append(random.choice(snowflakes))
        else:
            row.append(" ")
    grid.insert(0, row)
    grid.pop()

    draw_grid()

    time.sleep(DELAY)