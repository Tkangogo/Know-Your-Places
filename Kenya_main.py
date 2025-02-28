import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.setup(850, 750)
screen.title("Kenya Counties Game")
image = "blank_Kenya_counties_map_gif.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("Kenya_counties_coordinates.csv")
counties_list = data["County"].to_list()
counties_guessed = []

while len(counties_guessed) < 47:
    user_input = screen.textinput(title=f"{len(counties_guessed)}/47 counties correct", prompt="Guess a county: ").title()
    if user_input in counties_list:
        row_of_interest = data[data["County"] == user_input]
        x_position = row_of_interest.x_coord.item()
        y_position = row_of_interest.y_coord.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_position,y_position)
        t.write(arg=f"{user_input}",align="center", font=('Arial', 7, 'normal'))
        if user_input not in counties_guessed:
            counties_guessed.append(user_input)

    elif user_input == "Exit":
        counties_not_guessed = [county for county in counties_list if county not in counties_guessed]
        counties_to_learn = pd.DataFrame(counties_not_guessed)
        counties_to_learn.to_csv("unknown_counties", index=False)
        screen.bye()  # Close the program if "Exit" is entered
        break


screen.exitonclick()
