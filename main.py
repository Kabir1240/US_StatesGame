from turtle import Turtle, Screen
import pandas
BLANK_STATE_IMAGE_PATH = "blank_states_img.gif"
STATE_DATA_PATH = "50_states.csv"
ALIGNMENT = 'center'
FONT = ('Courier', 8, 'normal')


# initialize screen and turtles
screen = Screen()
image_turtle = Turtle()
screen.addshape(BLANK_STATE_IMAGE_PATH)
image_turtle.shape(BLANK_STATE_IMAGE_PATH)

writing_turtle = Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()

# initialize data needed
dataframe = pandas.read_csv(STATE_DATA_PATH)
list_of_states = dataframe.state.str.lower().to_list()

states_correct = 0
guessed_states = []
while states_correct < 50:
    prompt_response = screen.textinput(title=f"{states_correct}/50 correct U.S States Game",
                                       prompt="What's another states name?")

    if prompt_response == "" or prompt_response is None:
        prompt_response = screen.textinput(title=f"{states_correct}/50 correct U.S States Game",
                                           prompt="What's another states name?")
    elif prompt_response.lower() == "exit":
        break

    elif prompt_response.lower() in list_of_states and prompt_response.lower() not in guessed_states:
        row = dataframe[dataframe.state.str.lower() == prompt_response.lower()]
        writing_turtle.goto(x=row.x.item(), y=row.y.item())
        writing_turtle.write(f"{row.state.item()}", move=False, align=ALIGNMENT, font=FONT)

        states_correct += 1
        guessed_states.append(prompt_response.lower())

screen.mainloop()
