import math

import pygame
import time
import random
import sys
from pygame.locals import *
from pygame import mixer

fps = 32
pygame.init()
screen = pygame.display.set_mode((800, 800))

screen.fill((255, 255, 255))
icon = pygame.image.load("mosquito.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Mosquito Smasher")
mos = pygame.image.load("sprite.png")
net = pygame.image.load("net.png")
net2 = pygame.image.load("net2.png")
blood = pygame.image.load("blood.png")
miss = pygame.image.load("MISS.png")
gameover = pygame.image.load("gameover.png")

run = True
x = 0
y = 0
n = 0
lv = 3
sc = 0
myfont1 = pygame.font.SysFont("monospace", 20)
myfont2 = pygame.font.SysFont("monospace", 20)


def rany():
    global x
    global y
    x = 0
    y = random.randint(0, 700)


def strline():
    global x
    global y
    screen.fill((255, 255, 255))
    screen.blit(mos, (x, y))
    x += 0.5
    y += 0.5


def parabola():
    global x
    global y
    screen.fill((255, 255, 255))
    screen.blit(mos, (x, y))
    x += 0.01
    y = x * x


def circle():
    global x
    global y
    screen.fill((255, 255, 255))
    screen.blit(mos, (x, y))

    x = x + 0.5

    y = 25 / x


def anyway():
    global x
    global y
    screen.fill((255, 255, 255))
    screen.blit(mos, (x, y))
    x = random.randrange(x, x + 2)
    y = random.randrange(y - 2, y + 2)


def gameov():
    screen.fill((255, 255, 255))
    screen.blit(gameover, (100, 100))
    pygame.display.update()
    mixer.music.load('videogame-death-sound-43894.mp3')
    mixer.music.play()
    time.sleep(5)


mixer.music.load('flying-mosquito-105770.mp3')
mixer.music.play(-1)
while run:
    n += 1
    lclick = False
    mx, my = pygame.mouse.get_pos()
    txt1 = myfont1.render("Score:" + str(sc), 5, (0, 0, 0))
    txt2 = myfont2.render("Lives:" + str(lv), 5, (0, 2, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and ((mx <= x + 32 and mx >= x - 32) and (my <= y + 32 and my >= y - 32)):
                lclick = True
                sc = sc + 1

                screen.fill((255, 255, 255))
                slap_sound = mixer.Sound('karate-chop-6357.wav')
                slap_sound.play()
                screen.blit(blood, (mx, my))
                screen.blit(net2, (mx, my))

                pygame.display.update()

                time.sleep(1)
                rany()

            else:
                lv = lv - 1
                if lv == 0:
                    gameov()
                    sys.exit()
                miss_sound = mixer.Sound('error-1-126514.mp3')
                miss_sound.play()
                screen.blit(miss, (250, 400))
                pygame.display.update()
                time.sleep(1)

    anyway()
    screen.blit(net, (mx, my))
    screen.blit(txt1, (400, 10))
    screen.blit(txt2, (600, 10))
    pygame.display.update()
    if x >= 700:
        rany()
