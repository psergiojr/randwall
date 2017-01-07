#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

WIDTH = 1366
HEIGHT = 768

def rand_color():
    r = random.choice(range(0,255))
    g = random.choice(range(0,255))
    b = random.choice(range(0,255))
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)


def stripes():
    columns = []
    col_width = WIDTH/10
    while sum(columns) < WIDTH:
        columns.append( col_width )

    x = 0
    for column in columns:
        print('<rect x="{x}" y="0" width="{col_width}"\
                height="{col_height}" style="fill:{color}"\
                />'.format(x=x, col_width=column,
                    col_height=HEIGHT, color=rand_color()))
        x += column

if __name__ == '__main__':
    print('<svg xmlns="http://www.w3/org/2000/svg" width="1366" height="768">')
    stripes()
    print('</svg>')
