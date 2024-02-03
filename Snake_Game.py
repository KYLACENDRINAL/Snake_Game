# A snake game that will display the score, high score and levels of the game.

# pseudocode

# Set up the screen
import turtle
wn = turtle.Screen()
wn.title("Snake Game by Kyla Endrinal")
wn.bgcolor("pink")
wn.setup(width=600, height=600)
wn.tracer


# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

wn.mainloop()



# Define the function to move the snake head
# Set up the keyboard bindings
# Create the snake food
# Check collision with the food
# Create the segments
# Check the collision with the border
# Check the collision with body segments
# Set up the score
# Create the level
