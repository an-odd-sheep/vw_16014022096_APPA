import pygame
import sys
from pygame.locals import *

pygame.init()
pygameSurface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")
white = pygame.Color(255, 255, 255)


tank = pygame.image.load("EXPERIMENT 07/military-parade.png")
xt = 220
yt = 420

is_jumping = False
velocity_y = 0
gravity = 0.5
jump_strength = 10  
initial_y = 0  

def mov_left():
    global xt
    xt -= 5
    if xt < 30:
        xt = 30

def mov_right():
    global xt
    xt += 5
    if xt > 470:
        xt = 470

def mov_up():
    global yt
    yt -= 5
    if yt < 30:
        yt = 30

def mov_down():
    global yt
    yt += 5
    if yt > 470:
        yt = 470

def start_jump():
    global is_jumping, velocity_y, initial_y
    is_jumping = True
    initial_y = yt  
    velocity_y = -jump_strength  


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                mov_left()
            if event.key == K_RIGHT:
                mov_right()
            if event.key == K_UP:
                mov_up()
            if event.key == K_DOWN:
                mov_down()
            if event.key == K_SPACE and not is_jumping:
                start_jump()

    
    if is_jumping:
        yt = yt + velocity_y
        velocity_y += gravity  

        
        if yt >= initial_y:
            yt = initial_y  
            is_jumping = False
            velocity_y = 0  

    
    pygameSurface.fill(white)
    pygameSurface.blit(tank, (xt, yt))
    pygame.display.update()
