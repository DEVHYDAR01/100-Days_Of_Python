# from turtle import Turtle, Screen
#
# hydar = Turtle()
# my_screen = Screen()
# hydar.shape("turtle")
# hydar.color("BlueViolet")
# hydar.forward(100)
#
# print(Turtle)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)