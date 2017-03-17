# Following a line

Robot's aren't programmed to follow lines, just for fun. There are real world uses for a robot that can follow a line autonomously (on it's own).

In warehouses all over the world, robots are programmed to follow lines, stickers and barcodes so that they can navigate with ease from one area to another.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8gy5tYVR-28" frameborder="0" allowfullscreen></iframe>

## Installing your Line Sensor

1. You're going to need to cut a hole in the bottom of your container, to allow the line sensor wires to attach to the Raspberry Pi.

	![line sensor hole](ls-hole.jpg)

1. The line sensor can then be attached to the bottom of your robot, using a little blutac, and the jumper leads passed through the holw.

	![line sensor attached](ls-attached.jpg)

1. Then the jumper leads can be connected to your Raspberry Pi. Here the output pin of the line sensor is attached to GP18 on the Pi.

	![line sensor wired](ls-wired.jpg)

## Coding your line following robot.

There's no single way to code the line following algorithm, and you're going to need to experiment quite heavily, to produce one that is suited to your specific build.

Here is one method you coudl try though:

1. You can start with the basic code, that sets up your robot.

	```python
	from gpiozero import Robot, LineSensor

	remy = Robot(left = (7, 8), right = (9, 10))
	ls = linesensor(18)
	```

1. Now you need to try an figure out the basic algorithm that your robot will use. Try writing it down in structured English to begin with. Something along the lines of:

  1. If over line drive forward
  1. If not over line find line

1. Let's begin with 





```python
from gpiozero import LineSensor, Robot

robot = Robot(left=(9, 10), right=(7, 8))
line = LineSensor(25)

robot.source_delay = 0.5
speed = 0.6

def look_for_line():
    while True:
        yield (1, 0.5)  # left motor full speed, right motor half speed
        yield (0.5, 1)  # left motor half speed, right motor full speed

while True:
    robot.forward(speed)
    line.wait_for_no_line()  # go forward until the line is lost
    robot.source = look_for_line()  # alternate between slight left and slight right
    line.wait_for_line()  # until the line is found
	robot.source = None # unset the source to stop looking left and right
```
