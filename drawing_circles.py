#!/usr/bin/python3

import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np

top = tk.Tk()
top.title ('Número')

R = 8 # radius of each individual circle

canv = tk.Canvas (top, bg = 'black', height = 168, width = 168)
canv.pack()

width = 168
height = 168
white = (255, 255, 255)
black = (0, 0, 0)
image1 = Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)

def clic(event):
    x = event.x
    y = event.y
    canv.create_oval (x-R, y-R, x+R, y+R, fill = 'white', outline = 'white')
    draw.ellipse ([x-R, y-R, x+R, y+R], white)

def save (event):
    print ('Entró al save')
    filename = "number.png"
    arr = np.array(image1)
    flat_arr = arr.ravel()
    image1.save(filename)

canv.bind('<B1-Motion>', clic)
canv.bind('<Button-2>', save)

top.mainloop()
