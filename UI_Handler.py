import numpy as np
from numpy import random as rng
import pygame
import sys
from pygame.locals import *

class Canvas:
	def __init__(self, size, Screen):
		self.w, self.h = size
		self.Screen = Screen
		self.elements = []

	def addElement(self, element):
		self.elements += [element]

	def Update(self):
		for e in self.elements:
			e.Draw(self.Screen)
			if type(e) == type(Button((0,0),(255,255,255),"",(255,255,255),0)):
				if pygame.mouse.get_pressed()[0]:
					e.Clicked = e.getClicked(pygame.mouse.get_pos())
				else:
					e.Clicked = False

class viewPort:
	def __init__(self, ObjectToDraw):
		self.drawObj = ObjectToDraw

	def Draw(self, Screen):
		if self.drawObj.isPlaying == True:
			self.drawObj.Use()

class Panel:
	def __init__(self, PosAndDim, color):
		self.pad = PosAndDim
		self.c = color

	def Draw(self, Screen):
		pygame.draw.rect(Screen, self.c, self.pad)

class Button:
	def __init__(self, Pos, color, title, textColor, fontSize):
		self.Pos = Pos
		self.c = color
		self.txt = title
		self.tc = textColor
		self.font = pygame.font.Font('freesansbold.ttf', fontSize)
		self.text = self.font.render(self.txt, True, self.tc, self.c)
		self.textRect = self.text.get_rect()
		self.textRect.center = self.Pos
		self.Usable = True
		self.Clicked = False

	def Draw(self, Screen):
		Screen.blit(self.text, self.textRect)
		if self.Clicked == True:
			print("CLICKED !!!")

	def getClicked(self,point):
		return self.textRect.collidepoint(point)
