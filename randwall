#!/usr/bin/env python
from scipy.spatial import Delaunay
import random
import numpy
import math

CELL_SIZE = random.randrange(75, 250, 25)
WIDTH = 1920.0
HEIGHT = 1080.0
VARIANCE = 0.75


cells_x = int((WIDTH + 4 * CELL_SIZE) / CELL_SIZE)
cells_y = int((HEIGHT + 4 * CELL_SIZE) / CELL_SIZE)

bleed_x = ((cells_x * CELL_SIZE) - WIDTH) / 2.0
bleed_y = ((cells_y * CELL_SIZE) - HEIGHT) / 2.0

variance = CELL_SIZE * VARIANCE / 2.0

color1 = random.randrange(0, 180)
color2 = random.randrange(0, 180)


def centro(vertices):
    return (
       (vertices[0][0] + vertices[1][0] + vertices[2][0])/3.0,
       (vertices[0][1] + vertices[1][1] + vertices[2][1])/3.0
    )

def gradient(x, y):
    w = (WIDTH + (bleed_x * 2)) / 2.0
    h = (HEIGHT + (bleed_y * 2)) / 2.0
    r = math.hypot(abs(w - x) , abs(h - y))
    r_max = math.hypot( (WIDTH + (bleed_x * 2)), (HEIGHT + (bleed_y * 2)) ) / 2
    c = r/r_max * 255
    if(c > 255):
        c = 255
    return '#%02x%02x%02x' % (c,color1,color2)

def generate_points():
    w = WIDTH + bleed_x
    h = HEIGHT + bleed_y
    half_cell_size = CELL_SIZE / 2.0
    double_v = variance * 2.0
    negative_v = -variance

    points = [];

    for i in range(int(-bleed_x), int(w), int(CELL_SIZE)):
        for j in range (int(-bleed_y), int(h), int(CELL_SIZE)):
            x = (i + half_cell_size) + (random.random() * double_v + negative_v);
            y = (j + half_cell_size) + (random.random() * double_v + negative_v);
            points.append([int(x), int(y)]);
    return points



np_points = numpy.array(generate_points())
tri = Delaunay(np_points)
triangules = np_points[tri.simplices.copy()]

polys = []

for vertices in triangules:
    x,y = centro(vertices)
    polys.append((gradient(x,y), vertices))

# print triangules;
# print polys;

print '<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s">' % (int(WIDTH), int(HEIGHT))
for poly in polys:
    str_out = '<path d="M'
    color, vertice = poly
    d = 'L'.join([','.join([str(y) for y in point]) for point in vertice])
    print '<path d="M%sZ" fill="%s" stroke="%s" stroke-width="1.51"/>' % (d, color, color)
print '</svg>'


