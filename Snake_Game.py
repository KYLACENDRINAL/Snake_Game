# A snake game that will display the score, high score and levels of the game.

# pseudocode

# Set up the screen
import turtle
import time
import random

delay = 0.1
level = 1

# Score
score = 0
high_score = 0

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

# Create the snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Displaying the score, highest score and level
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0        High Score: 0        Level: 0", align="center", font=("Georgia", 16, "normal"))


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

    # Check the collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Reset the level
        level = 1

        pen.clear()
        pen.write("Score: {}        High Score: {}        Level: {}".format(score, high_score, level), align="center", font=("Georgia", 16, "normal"))


    # Check collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Create the segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

       # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}        High Score: {}        Level: {}".format(score, high_score, level), align="center", font=("Georgia", 16, "normal"))


    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Reset the level
            level = 1

            pen.clear()
            pen.write("Score: {}        High Score: {}        Level: {}".format(score, high_score, level), align="center", font=("Georgia", 16, "normal"))

    # Create the level
    if level == 1 and score == 100:
        level += 1
        delay *= 0.9
    if level == 2 and score == 200:
        level += 1
        delay *= 0.9
    if level == 3 and score == 300:
        level += 1
        delay *= 0.9
    if level == 4 and score == 400:
        level += 1
        delay *= 0.9
    if level == 5 and score == 500:
        level += 1
        delay *= 0.9
    if level == 6 and score == 600:
        level += 1
    if level == 7 and score == 700:
        level += 1
        delay *= 0.9
    if level == 8 and score == 800:
        level += 1
        delay *= 0.9
    if level == 9 and score == 900:
        level += 1
        delay *= 0.9
    if level == 10 and score == 1000:
        level += 1

    time.sleep(delay)



wn.mainloop()

# YOUTUBE LINK REFERENCES
#1.https://youtu.be/BP7KMlbvtOo?si=OaOCWsBnYb3N892F

#2.https://youtu.be/rrOqlfMujqQ?si=xrhfvyW3QUpr09fV

#3.https://youtu.be/J5yJilI-Af4?si=ViDvZFk4ux2grxAQ

#4.https://youtu.be/DxVPN1PIuLM?si=TVzBZLyQRISixasR

#5.https://youtu.be/VH-011awPyQ?si=PAi3Vqc_i_eJr5iI

#6.https://youtu.be/duElRYWqLgY?si=sxtnUhQJwOFf1nSW

#7.https://youtu.be/Vi0AhyUCCkE?si=Ay09OVZNp1mMlyqw



    

