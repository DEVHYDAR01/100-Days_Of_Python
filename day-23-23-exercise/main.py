import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.speed_increase)
    screen.update()
    screen.onkey(fun=player.move_up, key="Up")
    car_manager.create_cars()
    car_manager.car_movement()
    # Detect when the turtle player collides with a car and stop the game if this happens.
    for car in car_manager.cars:
        if car.distance(player) < 10:
            game_is_on = False

    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
    if player.ycor() > 300:
        player.return_home()
        car_manager.speed_add()


screen.exitonclick()

