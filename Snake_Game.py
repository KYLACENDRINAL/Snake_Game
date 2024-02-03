# A snake game that will display the score, high score and levels of the game.

# pseudocode

# Set up the screen
import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game by Kyla Endrinal")
wn.bgcolor("pink")
wn.setup(width=600, height=600)
wn.tracer(0)


# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Define the function to move the snake head
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)



# Set up the keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    move()
    time.sleep(delay)


wn.mainloop()




# Create the snake food
# Check collision with the food
# Create the segments
# Check the collision with the border
# Check the collision with body segments
# Set up the score
# Create the level
    

