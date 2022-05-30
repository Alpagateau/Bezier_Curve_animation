import numpy as np
from numpy import random as rng
import pygame
import sys
from pygame.locals import *
import pygame.gfxdraw
import AnimationSelector
import Maths as m

class Curve:
	def __init__(self, points, Screen):
		#initialise the control points
		self.controls_points = points
		#set all arrays to 0
		self.animation_points= []
		self.Curve_points = []
		self.FinalPoints = []
		#The Screen
		self.Screen = Screen

	def draw_Control_Points(self):
		#Only draw the white control points
		for p in self.controls_points:
			pygame.draw.circle(self.Screen, (0,0,0), p, 5)
		for l in range(len(self.controls_points) - 1):
			pygame.draw.line(self.Screen, (0,0,0), self.controls_points[l], self.controls_points[l+1], 1)

	#this function can draw a bezier Curve with 3 or 4 control points. It is not used
	def draw_animation_points(self, t):
		#Do the animation
		self.animation_points = []
		for l in range(len(self.controls_points) - 1):
			x,y = self.controls_points[l]
			j,k = self.controls_points[l+1]
			o = int(m.lerp(x, j, t))
			h = int(m.lerp(y, k, t))
			self.animation_points += [(o,h)]
			pygame.draw.circle(self.Screen, (0,255,10), [o,h], 5)
		for l in range(len(self.animation_points) - 1):
			pygame.draw.line(self.Screen, (0,255,0), self.animation_points[l], self.animation_points[l+1], 1)
		if(len(self.animation_points) > 2):
			secondary = []
			for l in range(len(self.animation_points) - 1):
				x,y = self.animation_points[l]
				j,k = self.animation_points[l+1]
				o = int(m.lerp(x, j, t))
				h = int(m.lerp(y, k, t))
				secondary += [(o,h)]
				pygame.draw.circle(self.Screen, (255,0,240), [o,h], 5)
			for l in range(len(secondary) - 1):
				pygame.draw.line(self.Screen, (255,0,210), secondary[l], secondary[l+1], 1)
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
				o = m.lerp(x, j, t)
				h = m.lerp(y, k, t)
				self.animation_points[iteration + 1] += [(o,h)]
				pygame.draw.circle(self.Screen, m.getRandomColor(iteration), [int(o),int(h)], 5)
				self.FinalPoints = (o,h)
			for l in range(len(self.animation_points[iteration + 1]) - 1):
				pygame.draw.line(self.Screen, m.getRandomColor(iteration), m.intArr(self.animation_points[iteration+1][l]), m.intArr(self.animation_points[iteration+1][l+1]), 1)

	def draw_curve(self, t):
		global lerp
		x,y = self.FinalPoints
		pygame.draw.circle(self.Screen, (10,10,240), [x,y], 5)
		self.Curve_points += [(x,y)]

		for i in range(len(self.Curve_points) - 1):
			pygame.draw.line(self.Screen, (0,0,0), self.Curve_points[i], self.Curve_points[i+1], 2)

	def Draw(self, t):
		#Juste a function to call every other function
		self.draw_Control_Points()
		self.draw_animation_points2(t)
		self.draw_curve(t)

	def Reset(self):
		self.Curve_points = []
		self.FinalPoints = []