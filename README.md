# Bezier_Curve_animation
This is a simple animation of the making of a bezier curve using the De Castlejau's algorithm

## How to use it

1. download it and unpack it
1. install the dependencies. To do that, use the command "pip install -r Dependencies.txt"
1. open the code an run it and, VOILA

## How to modify it
it is very simple to modify the bezier curve animation. Go to the 114th line : 
```
points = [(0,250), (240,0), (350,156), (450,450), (500,368), (600,0),(800,250),(750,650),(600,758)]
```
and modify the points. They are used as tuples so you just have to add them as "(x,y)" with x between 0 and the Screen Width and y between 0 and the Screen Height
