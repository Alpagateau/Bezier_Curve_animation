import numpy as np
from numpy import random as rng

def lerp(a, b, t):
	return (a + (t * (b-a)))

def getRandomColor(i = -55):
	colors = [
	(0,255,0),
	(250,0,0),
	(255,0,255),
	(255,255,0),
	(255,45,120),
	]
	if i == -55:
		return colors[rng.randint(0,len(colors))]
	else:
		return colors[int(np.mod(i, len(colors)))]