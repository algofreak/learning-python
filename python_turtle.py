from turtle import *

colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'purple', 'pink', 'brown']
size = len(colors)
i = 0
speed('fast')
while True:
    color(colors[i])
    i += 1
    i %= size
    forward(81)
    left(170)
    right(34)
    if abs(pos()) < 1:
        break
done()
