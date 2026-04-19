import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S states Game")
image = "blank_states_img.gif"
screen.addshape(image)
score = 0
turtle.shape(image)
guessed_states = []


states_data = pd.read_csv("50_states.csv")
states = pd.Series(states_data['state'])


while len(guessed_states) < len(states):


    answer_state = screen.textinput(f"{score} / {states.count()}", "What is another State's name ?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in states.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        score += 1
        correct = states_data[states_data.state == answer_state]

        x = int(correct.x.iloc[0])
        y = int(correct.y.iloc[0])

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        while len(guessed_states) < len(states):
            writer.goto(x, y)
            writer.write(answer_state)
            break

