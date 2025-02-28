import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.setup(850, 750)
screen.title("US States Guessing Game")
image = "blank_US_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("All_50_US_states.csv")
states_list = data["state"].to_list()
states_guessed = []

while len(states_guessed) < 47:
    user_input = screen.textinput(title=f"{len(states_guessed)}/50 states correct", prompt="Guess a state: ").title()
    if user_input in states_list:
        row_of_interest = data[data["state"] == user_input]
        x_position = row_of_interest.x.item()
        y_position = row_of_interest.y.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_position,y_position)
        t.write(arg=f"{user_input}",align="center", font=('Arial', 7, 'normal'))
        if user_input not in states_guessed:
            states_guessed.append(user_input)

    elif user_input == "Exit":
        states_not_guessed = [state for state in states_list if state not in states_guessed]
        states_to_learn = pd.DataFrame(states_not_guessed)
        states_to_learn.to_csv("unknown_states", index=False)
        screen.bye()  # Close the program if "Exit" is entered
        break


screen.exitonclick()
