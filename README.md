# randwall

(Pseudo) random geometric wallpaper generator

## Implemented

- Delaunay triangulation

## TODO

- Voronoi
- Beehive pattern
- Circle packing
- Free random path
- Self-avoiding path
- Stripes (horizontal, vertical, concentric, etc.) - **ongoing**
- Config file
- Optional automatic generation of PNGs (CairoSVG?)

## Dependencies

Delaunay Triangulation: SciPy

    sudo apt-get install python-scipy


## Generate SVG 

    python randwall > test.svg 
    
![example output](https://github.com/spacekatia/randwall/blob/master/test.svg)

## Generate PNG

	sudo  apt-get install librsvg2-bin     
    
    python randwall | rsvg-convert > test.png  
