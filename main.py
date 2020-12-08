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
# Background
background = pygame.image.load("space-galaxy-background.jpg")
#game loop
running = True


class Player:
    def __init__(self, x, y, xChange, yChange):
        self.x = x
        self.y = y
        self.xChange = xChange
        self.yChange = yChange
    def appear(self):
        playerImg = pygame.image.load("shooter.png")
        screen.blit(playerImg, (self.x, self.y))
        self.x += self.xChange
    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.xChange = -7
            if event.key == pygame.K_RIGHT:
                self.xChange = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.xChange = 0

shootie = Player(370,480,0,0)

class Enemy():
    def __init__(self, x, y, xChange, yChange):
        self.x = x
        self.y = y
        self.xChange = 5
        self.yChange = 40
    def randSpawn(self):
        self.x = random.randint(0,735)
        self.y = random.randint(50, 150)        
    def move(self):
        enemyImg = pygame.image.load("alien.png")
        screen.blit(enemyImg, (self.x, self.y))
        self.x += self.xChange
        if self.x <= 0:
            self.xChange = 5
            self.y += self.yChange
        elif self.x >= 736:
            self.xChange = -5
            self.y += self.yChange
alien = Enemy(0,0,5,40)

class Astroids(Enemy):
    def randSpawn(self):
        if self.y == -90:
            self.x = random.randint(0, 735)
    def move(self):
        rockImg = pygame.image.load("rock.png")
        screen.blit(rockImg, (self.x, self.y))
        self.yChange = 10
        self.y += self.yChange
        if self.y >= 900:
            self.y = -90
    

rock = Astroids(0, 0, 5, 0)
class Bullet:
    def __init__(self, x, y, yChange, state):
        self.x = x
        self.y = y
        self.yChange = yChange
        self.state = "ready"
    def fire(self):
        self.state = "fire"
        self.x = shootie.x

    def move(self):
        bulletImg = pygame.image.load("bullet.png")
        screen.blit(bulletImg, (self.x + 16, self.y + 10))        
        if self.state == "fire":
            self.y -= self.yChange
        if self.y <= 0:
            self.y = 480
            self.state = "ready"
            self.x = -50

bullet = Bullet(-50, 480, 10, "ready")

rock.randSpawn()
alien.randSpawn()
while running:
    screen.fill((0,0,0))  
    #Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        #to close window
        if event.type == pygame.QUIT:
            running = False
        shootie.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire()
    
    rock.move()
    bullet.move()
    
    alien.move()
    shootie.appear()
    
    #Updates each frame
    pygame.display.update()




