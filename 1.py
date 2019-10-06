import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
import os
import time

x1 = 0
x2 = 0
y1 = 0
y2 = 0
a = 75


def reload():
    global x1
    global y1
    global x2
    global y2
    global img
    x1 = 0
    x2 = 0
    y1 = 0
    y1 = 0
    img = Image.open(r'F:\Workplace\JumpKing\01.png')
    plt.imshow(img, animated=True)
    plt.show()


def update(times):
    time.sleep(int(times / 1000) + 2)
    os.system(r'F:\1.bat')


def on_press(event):
    global x1
    global y1
    global x2
    global y2
    if event.button == 1:
        x1 = event.xdata
        y1 = event.ydata
    if event.button == 3:
        x2 = event.xdata
        y2 = event.ydata
    if x1 and x2 and y1 and y2:
        length = ((x2-x1)**2+(y2 - y1)**2)**0.5
        times = length / a * 100
        cmd = 'adb shell input swipe 100 100 200 200 %s' % str(int(round(times)))
        print(cmd)
        os.system(cmd)
        update(times)
        reload()


fig = plt.figure()
img = Image.open(r'F:\Workplace\JumpKing\01.png')
fig.canvas.mpl_connect('button_press_event', on_press)

if __name__ == '__main__':
    update(0)
    time.sleep(1)
    reload()
