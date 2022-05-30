
import numpy as np
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
			"""
			if type(e) == type(Button((0,0),(255,255,255),"",(255,255,255),0)):
				if pygame.mouse.get_pressed()[0]:
					e.Clicked = e.getClicked(pygame.mouse.get_pos())
				else:
					e.Clicked = False
			"""
			if pygame.mouse.get_pressed()[0]:
				e.Clicked = e.getClicked(pygame.mouse.get_pos())
			else:
				e.Clicked = False

class viewPort:
	def __init__(self, ObjectToDraw):
		self.drawObj = ObjectToDraw
		self.Clicked = False

	def Draw(self, Screen):
		if self.drawObj.isPlaying == True:
			self.drawObj.Use()

	def getClicked(self,point):
		return pygame.Rect(0,0,800,800).collidepoint(point)

class Panel:
	def __init__(self, PosAndDim, color):
		self.pad = PosAndDim
		self.c = color
		self.Clicked = False

	def Draw(self, Screen):
		pygame.draw.rect(Screen, self.c, self.pad)
	
	def getClicked(self,point):
		c = pygame.Rect(self.pad).collidepoint(point)
		if c:
			self.c = (0,255,0)
		else:
			self.c = (100,100,100)
		return c
	
	def getPosAndDim(self):
		x,y,w,h = self.pad
		return [x,y,w,h]

class Button:
	def __init__(self, Pos, color, title, textColor, fontSize, hovercolor=(0,255,0)):
		self.Pos = Pos
		self.c = color
		self.txt = title
		self.tc = textColor
		self.font = pygame.font.Font('freesansbold.ttf', fontSize)
		self.text = self.font.render(self.txt, True, self.tc, self.c)
		self.hovertext = self.font.render(self.txt, True, self.tc, hovercolor)
		self.textRect = self.text.get_rect()
		self.textRect.center = self.Pos
		self.Usable = True
		self.Clicked = False

	def Draw(self, Screen):
		if(not self.Clicked):
			Screen.blit(self.text, self.textRect)
		else:
			Screen.blit(self.hovertext, self.textRect)
		
	def getClicked(self,point):
		return self.textRect.collidepoint(point)

	def getPosAndDim(self):
		x,y = self.textRect.bottomleft
		w,h = self.textRect.topright
		w-=x
		h-=y
		return [x,y,w,h]