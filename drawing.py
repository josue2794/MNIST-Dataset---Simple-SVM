#!/usr/bin/python3

import tkinter as tk
import pygame as pg
top = tk.Tk()
top.title ('Número')

prev_X = None
prev_Y = None

canv = tk.Canvas (top, bg = 'white', height = 168, width = 168)
canv.pack()

def clic(event):
    global prev_X
    global prev_Y
    X = event.x
    Y = event.y
    if prev_X != None:
        canv.create_line (prev_X, prev_Y, X, Y, fill = 'black', width = 8, smooth = True)
    prev_X = X
    prev_Y = Y

canv.bind('<B1-Motion>', clic)

top.mainloop()
