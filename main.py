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
points = [(200,200), (300,300), (400,200), (500, 300), (600,200)]
curve = BA.Curve(points, Screen)
selector = AnimationSelector.Selector(Screen, curve)
#selector.isPlaying = True
selector.MaxFrame = 2500

canvas = UI.Canvas(ScreenSize, Screen)
canvas.addElement(UI.viewPort(selector))
canvas.addElement(UI.Panel((0,700,800,100),(164,154,155)))
canvas.addElement(UI.Button((400,750), (255,64,70), "Play", (255,255,255), 25))
canvas.addElement(UI.Button((400,780), (255,64,70), "Set Points", (255,255,255), 25))


x = 0
PlacePoints = False
#The game loop
IsActive = True
while IsActive == True:
	#fill the screen with a black background
	Screen.fill((255,255,255))
	#get the quit event
	for event in pygame.event.get():
		canvas.Update()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if pygame.mouse.get_pressed()[0]:
			if PlacePoints == True:
				if canvas.elements[2].Clicked == False and canvas.elements[1].Clicked == False:
					points += [pygame.mouse.get_pos()]
		
		
	#Run the animation
	canvas.Update()
	if canvas.elements[2].Clicked == True:
		selector.isPlaying = True
		PlacePoints = False
		selector.curentAnim.controls_points = points
	
	if canvas.elements[3].Clicked == True:
		PlacePoints = True

	if selector.isPlaying == False:
		selector.curentAnim.draw_Control_Points()
	#Update the screen 
	
	pygame.display.update()