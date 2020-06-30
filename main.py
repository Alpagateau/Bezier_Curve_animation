import numpy as np
from numpy import random as rng
import pygame
import sys
from pygame.locals import *
import AnimationSelector
import Maths as m
import BezierAnimation as BA
import UI_Handler as UI

pygame.init()

#set the screen 
ScreenSize = (800,800)
Screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption('Bezier Curve Animation') 

#Set the position of the control points in the screen (0 > Screen.W, 0 > Screen.H)
points = [(400,0),(800,0),(800,350),(800,700),(400,700),(0,700),(0,350),(0,0),(400,0 )]
selector = AnimationSelector.Selector(Screen, BA.Curve(points, Screen))
#selector.isPlaying = True
selector.MaxFrame = 2500

canvas = UI.Canvas(ScreenSize, Screen)
canvas.addElement(UI.viewPort(selector))
canvas.addElement(UI.Panel((0,700,800,100),(164,154,155)))
canvas.addElement(UI.Button((400,750), (255,0,255), "Play", (255,255,255), 25))


x = 0
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
	canvas.Update()
	if canvas.elements[2].Clicked == True:
		selector.isPlaying = True
	#Update the screen 
	pygame.display.update()