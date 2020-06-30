import numpy as np
from numpy import random as rng
import pygame
import sys
from pygame.locals import *
import matplotlib.pyplot as plt

#function to pick a color for lines
def getRandomColor(i = -55):
	colors = [
	(0,255,0),
	(250,0,0),
	(255,0,255),
	(255,255,0),
	(255,45,120),
	]
	if i == -55:
		return colors[np.random.randint(0,len(colors))]
	else:
		return colors[int(np.mod(i, len(colors)))]

#The curve class
class Curve:
	def __init__(self, points):
		#initialise the control points
		self.controls_points = points
		#set all arrays to 0
		self.animation_points= []
		self.Curve_points = []
		self.FinalPoints = []

	def draw_Control_Points(self):
		#Only draw the white control points
		global Screen
		for p in self.controls_points:
			pygame.draw.circle(Screen, (255,255,255), p, 5)
		for l in range(len(self.controls_points) - 1):
			pygame.draw.line(Screen, (255,255,255), self.controls_points[l], self.controls_points[l+1], 2)

	#this function can draw a bezier Curve with 3 or 4 control points
	def draw_animation_points(self, t):
		#Do the animation
		global lerp
		self.animation_points = []
		for l in range(len(self.controls_points) - 1):
			x,y = self.controls_points[l]
			j,k = self.controls_points[l+1]
			o = int(lerp(x, j, t))
			h = int(lerp(y, k, t))
			self.animation_points += [(o,h)]
			pygame.draw.circle(Screen, (0,255,10), [o,h], 5)
		for l in range(len(self.animation_points) - 1):
			pygame.draw.line(Screen, (0,255,0), self.animation_points[l], self.animation_points[l+1], 2)
		if(len(self.animation_points) > 2):
			secondary = []
			for l in range(len(self.animation_points) - 1):
				x,y = self.animation_points[l]
				j,k = self.animation_points[l+1]
				o = int(lerp(x, j, t))
				h = int(lerp(y, k, t))
				secondary += [(o,h)]
				pygame.draw.circle(Screen, (255,0,240), [o,h], 5)
			for l in range(len(secondary) - 1):
				pygame.draw.line(Screen, (255,0,210), secondary[l], secondary[l+1], 2)
			self.FinalPoints = secondary[:]
		else:
			self.FinalPoints = self.animation_points[:]

	#this function can draw a bezier Curve with any number of control points
	def draw_animation_points2(self, t):
		#set the size of animations iteration
		self.animation_points = [0] * (len(self.controls_points))
		self.animation_points[0] = self.controls_points[:]
		#loop for each iteration
		for iteration in range(len(self.controls_points)-1):
			self.animation_points[iteration + 1] = []
			for l in range(len(self.animation_points[iteration]) - 1):
				x,y = self.animation_points[iteration][l]
				j,k = self.animation_points[iteration][l+1]
				o = int(lerp(x, j, t))
				h = int(lerp(y, k, t))
				self.animation_points[iteration + 1] += [(o,h)]
				pygame.draw.circle(Screen, getRandomColor(iteration), [o,h], 5)
				self.FinalPoints = (o,h)
			for l in range(len(self.animation_points[iteration + 1]) - 1):
				pygame.draw.line(Screen, getRandomColor(iteration), self.animation_points[iteration+1][l], self.animation_points[iteration+1][l+1], 2)

	def draw_curve(self, t):
		global lerp
		x,y = self.FinalPoints
		pygame.draw.circle(Screen, (10,10,240), [x,y], 5)
		self.Curve_points += [(x,y)]

		for i in range(len(self.Curve_points) - 1):
			pygame.draw.line(Screen, (0,0,255), self.Curve_points[i], self.Curve_points[i+1], 5)


	def Draw(self, t):
		#Juste a function to call every other function
		self.draw_Control_Points()
		self.draw_animation_points2(t)
		self.draw_curve(t)

pygame.init()

#set the screen 
ScreenSize = (800,800)
Screen = pygame.display.set_mode(ScreenSize)

def lerp(a, b, t):
	return (a + (t * (b-a)))

#Set the position of the control points in the screen (0 > Screen.W, 0 > Screen.H)
points = [(0,250), (240,0), (350,156), (450,450), (500,368), (600,0),(800,250),(750,650),(600,758)]

curve = Curve(points)

TotaFrame = 5000

actualFrame = 0

waitingFrame = 200

#The game loop
IsActive = True
while IsActive == True:
	#fill the screen with a black background
	Screen.fill((0,0,0))
	#get the quit event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	#Run the animation
	if TotaFrame > actualFrame:
		ti = actualFrame / TotaFrame
		actualFrame += 1
		curve.Draw(ti)
	else:
		actualFrame += 1
		curve.Draw(1)
		if actualFrame > (TotaFrame + waitingFrame):
			actualFrame = 0
			curve = Curve(points)
	#Update the screen 
	pygame.display.update()