import numpy as np
from numpy import random as rng

def lerp(a, b, t):
	return (a + (t * (b-a)))

def getRandomColor(i = -55):
	colors = [
	(50,50,50),
	(100,100,100),
	(150,150,150),
	(200,200,200),
	(250,250,250),
	]
	if i == -55:
		return colors[rng.randint(0,len(colors))]
	else:
		return colors[int(np.mod(i, len(colors)))]

def intArr(a):
	b = []
	for i in a:
		b += [int(i)]
	return b