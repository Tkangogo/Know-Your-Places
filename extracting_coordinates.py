import turtle
import pandas as pd

counties = []  # List to store county data


def get_coordinates(x, y):
    """Callback function to capture clicked coordinates and trigger county name input."""
    county_name = screen.textinput(title="Kenya Counties", prompt="Enter the county name: ").title()

    if county_name and county_name != "Exit":  # Ensure valid input
        counties.append({"County": county_name, "x_coord": x, "y_coord": y})  # Store as a dictionary

        # Display county name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(arg=f"{county_name}", align="center", font=('Arial', 7, 'normal'))

    else:
        # Convert to DataFrame and save as CSV
        counties_data_frame = pd.DataFrame(counties)
        counties_data_frame.to_csv("Kenya_counties_coordinates.csv", index=False)
        print("CSV file saved successfully!")
        screen.bye()  # Close the program if "Exit" is entered


# Setup screen
screen = turtle.Screen()
screen.setup(850, 750)
screen.title("Kenya Counties Game")
image = "blank_Kenya_counties_map_gif.gif"
screen.addshape(image)
turtle.shape(image)

# Bind the click event
turtle.onscreenclick(get_coordinates)
turtle.mainloop()  # Keep the window open