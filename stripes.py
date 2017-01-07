#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

WIDTH = 1366
HEIGHT = 768

def rand_color(base=None, boundaries=50):
    if base:
        red, green, blue = int(base[1:3], 16), int(base[3:5], 16), int(base[5:], 16)
        r = random.choice(range(red-boundaries, red+boundaries))
        g = random.choice(range(green-boundaries, green+boundaries))
        b = random.choice(range(blue-boundaries, blue+boundaries))
    else:
        r = random.choice(range(0,255))
        g = random.choice(range(0,255))
        b = random.choice(range(0,255))
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def stripes():
    columns = []
    while sum(columns) <= WIDTH:
        col_width = random.choice( range(int(WIDTH/10), int(WIDTH/2)) )
        columns.append( col_width )
    x = 0
    base_color = rand_color()
    for column in columns:
        print('<rect x="{x}" y="0" width="{col_width}" \
height="{col_height}" style="fill:{color};stroke:none"\
/>'.format(x=x, col_width=column, col_height=HEIGHT, color=rand_color(base_color)))
        x += column

if __name__ == '__main__':
    print('<svg xmlns="http://www.w3.org/2000/svg" width="1366" height="768">')
    stripes()
    print('</svg>')
