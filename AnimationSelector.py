import numpy as np
from numpy import random as rng
import pygame
import sys
from pygame.locals import *
import BezierAnimation as BA

class Selector:
	def __init__(self,_Screen ,curentAnim):
		self.Screen = _Screen
		self.curentAnim = curentAnim
		self.isPlaying = False
		self.frame = 0
		self.MaxFrame = 0
		self.waitframe = 1000

	def Restart(self):
		self.curentAnim.reset()
	
	def Use(self):
		if self.frame == self.MaxFrame+self.waitframe:
			self.isPlaying = False
			self.curentAnim.Reset()
			self.frame = 0

		if self.frame < self.MaxFrame:
			self.frame += 1
			self.curentAnim.Draw((self.frame / self.MaxFrame))
		elif self.frame < self.MaxFrame+self.waitframe:
			self.frame += 1
			self.curentAnim.Draw(1)

