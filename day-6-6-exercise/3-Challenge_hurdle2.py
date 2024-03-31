def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def hurdle1():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jumps = 6
while at_goal() != jumps:
    hurdle1()
    jumps = jumps - 1

    







################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
