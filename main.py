import pygame
import math
import random
#initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))
#Title and Icon
icon = pygame.image.load('spaceship.png')
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)
# Bakcground
background = pygame.image.load("space-galaxy-background.jpg")
#game loop
running = True
while running:
    screen.fill((0,0,0))  
    #Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        #to close window
        if event.type == pygame.QUIT:
            running = False

    #Updates each frame
    pygame.display.update()