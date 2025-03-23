import pgzrun
import random
from time import time

TITLE="Satellite Game"

WIDTH=800
HEIGHT=500

satellites =[]
number_of_satellite=8
next_satellite=0

lines=[]

start_time  = 0
total_time = 0
end_time= 0


def create_satellite():
    global start_time
    #doing a list so the first value will have index number 0.But it will be by default 0, don't have to use it
    for i in range(0,number_of_satellite):
       satellite=Actor("satellite")
       satellite.pos=random.randint(50,750),random.randint(50,450)
       satellites.append(satellite)
    start_time= time()   



def draw():
    global total_time
    screen.clear()
    screen.blit("background",(0,0))
    number=1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_satellite<number_of_satellite:
        total_time=time()- start_time
        screen.draw.text(str(round(total_time,1)),topleft=(20,10))
    
    else:
        screen.draw.text(str(round(total_time,1)),topleft=(20,10))

    if next_satellite==8:
        screen.draw.text("Good Job! Your time is " + str(round(total_time, 1)), center=(400, 10), color="white", fontsize=40)

    

def update():
    pass

def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite<number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite+=1
        else:
            lines=[]
            next_satellite=0

    

create_satellite()    
pgzrun.go()