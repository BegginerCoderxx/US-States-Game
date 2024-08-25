import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()

guessed_state = []
while  len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}Guess the state", prompt="What's another state's name?").title()
    def get_mouse_click_coor(x,y):
        print(x,y)

    if answer_state == "Exit":
        missing_states = [state for state in data_list if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to.csv("learning.csv")
        break
    if answer_state in data_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())






