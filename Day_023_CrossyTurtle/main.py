import time
from turtle import Screen, left
from player import Player
from cars import Cars

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

player = Player()
cars = Cars()

screen.listen()

screen.onkey(player.forward, "w")
screen.onkey(player.backward, "s")



gaming = True

while gaming:
    time.sleep(0.1)
    screen.update()
    
    # Finish line
    
    cars.create_car()
    cars.move_cars()
    
    # Detect car collision
    for car in cars.all_cars:
        if player.distance(car) < 20:
            gaming = False
    
    if player.ycor() > 280:
        player.level_up()
    

screen.exitonclick()