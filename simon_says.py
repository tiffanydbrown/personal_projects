import turtle
import random
import time

# Setup the game window
win = turtle.Screen()
win.title("Simon Says")
win.bgcolor("black")
win.setup(width=600, height=600)

# Game variables
sequence = []  # Stores the sequence of colors
player_sequence = []  # Stores the player's guesses

# A function to determine what happens when the red quadrant is clicked.
def on_red_click(x, y):
    quadrant_click_handler(quadrant_turtles[0])

# A function to determine what happens when the blue quadrant is clicked.
def on_blue_click(x, y):
    quadrant_click_handler(quadrant_turtles[1])

# A function to determine what happens when the green quadrant is clicked.
def on_green_click(x, y):
    quadrant_click_handler(quadrant_turtles[2])

# A function to determine what happens when the yellow quadrant is clicked.
def on_yellow_click(x, y):
    quadrant_click_handler(quadrant_turtles[3])

# A function that draws a single quadrant of a specific color.
def draw_quadrant(color, x, y):
    t = turtle.Turtle()
    t.speed(1) # Speed of animation
    t.shape("square")
    t.color(color)
    t.penup() # Prevent drawing lines.
    t.goto(x, y)
    t.shapesize(stretch_wid=15, stretch_len=15) # Adjust size
    return t

# Initializes and draws all 4 quadrants.
def draw_quadrants():
    quadrants = []
    quadrants.append(draw_quadrant("red", -150, 150))
    quadrants.append(draw_quadrant("blue", 150, 150))
    quadrants.append(draw_quadrant("green", -150, -150))
    quadrants.append(draw_quadrant("yellow", 150, -150))
    return quadrants

def next_round():
    add_to_sequence(quadrant_turtles)
    display_sequence()

def play_game(quadrant_turtles):
    add_to_sequence(quadrant_turtles)
    display_sequence()
    quadrant_turtles[0].onclick(on_red_click)
    quadrant_turtles[1].onclick(on_blue_click)
    quadrant_turtles[2].onclick(on_green_click)
    quadrant_turtles[3].onclick(on_yellow_click)

########################################################################
# Add a random quadrant to the sequence
def add_to_sequence(quadrants):
    sequence.append(random.choice(quadrants))

# Displays the current sequence to the player by highlighting each quadrant.
def display_sequence():
    for quadrant in sequence:
        original_color = quadrant.color()[0]
        quadrant.color("white")
        time.sleep(0.5)
        quadrant.color(original_color)
        time.sleep(0.5)


# Determines if the player's sequence of 
# clicked quadrants matches the intended sequence
def check_player_sequence():
    for i in range(len(player_sequence)):
        if player_sequence[i] != sequence[i]:
            return False
    return True

# A function that runs whenever a quadrant is clicked
def quadrant_click_handler(quadrant):
    original_color = quadrant.color()[0]
    quadrant.color("white")
    time.sleep(0.2)
    quadrant.color(original_color)

    player_sequence.append(quadrant)
    if not check_player_sequence():
        print("You got the wrong sequence! Game over!")
        win.bye()
    elif len(player_sequence) == len(sequence):
        print("You are correct!")
        player_sequence.clear()
        time.sleep(1)
        next_round()

# Initialize the game
quadrant_turtles = draw_quadrants()
play_game(quadrant_turtles)

# Keep the window open
win.mainloop()
