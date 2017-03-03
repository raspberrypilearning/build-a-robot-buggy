from gpiozero import Robot, DistanceSensor, DigitalInputDevice
from time import sleep, time
from threading import Thread

remy = Robot(left=(9, 10), right = (7,8))
dist = DistanceSensor(echo = 17, trigger = 4)
line = DigitalInputDevice(18)
on_line = False

def is_on_line():
    global on_line
    while True:
        on_line = not line.value

detect_line = Thread(target=is_on_line)
detect_line.start()

def slow_left(s):
    remy.left(speed = 1)
    sleep(0.05)
    remy.left(speed = s)
    
def slow_right(s):
    remy.right(speed = 1)
    sleep(0.05)
    remy.right(speed = s)

def find_line(max_time):
    right = True
    search_time = 0.1
    full_search = time() + max_time
    while time() < full_search:
        start_search = time()
        if right:
            slow_right(0.5)
        else:
            slow_left(0.5)
        while time() < search_time + start_search:
            if on_line == True:
                return True
            else:
                pass
            
        search_time += 0.1
        right = not right

while True:
    if on_line == True:
        remy.forward(speed = 0.5)
    else:
        remy.stop()
        find_line(10)
