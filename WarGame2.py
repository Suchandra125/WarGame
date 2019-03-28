import pygame
import time
import random

pygame.init()
display_width = 1400
display_height = 800
black = (0,0,0)
white = (255,255,255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('War')
clock = pygame.time.Clock()
warImg1 = pygame.image.load('player1.png')
warImg2 = pygame.image.load('player2.png')
warImg3 = pygame.image.load('bullect1.png')

def war(x,y):
    gameDisplay.blit(warImg1,(x,y))

def war1(x,y):
    gameDisplay.blit(warImg2,(x,y))

def bullect(x,y):
    gameDisplay.blit(warImg3,(x,y))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    gameloop()
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy, thingw,thingh])

def crash():
    message_display("You Crashed..!")

def gameloop():
    x1 = (display_width * 0.025)
    y1 = (display_height * 0.5)
    x2 = (display_width * 0.9)
    y2 = (display_height * 0.5)

    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0
    flag1 = 0
    thing_startx = random.randrange(400,1000)
    thing_starty = -200
    thing_speed = 10
    thing_width = 60
    thing_height = 60
    killed = False

    while not killed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -5
                if event.key == pygame.K_RIGHT:
                    x1_change = 5
                if event.key == pygame.K_DOWN:
                    y1_change = 5
                if event.key == pygame.K_UP:
                    y1_change = -5
                if event.key == pygame.K_SPACE:
                    flag1 = 1
                if event.key == pygame.K_KP6:
                    x2_change = 5
                if event.key == pygame.K_KP4:
                    x2_change = -5
                if event.key == pygame.K_KP5:
                    y2_change = 5
                if event.key == pygame.K_KP8:
                    y2_change = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bullect(x3, y3)
                if event.key == pygame.K_DOWN:
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = 0
                if event.key == pygame.K_LEFT:
                    x1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = 0
                if event.key == pygame.K_KP6:
                    x2_change = 0
                if event.key == pygame.K_KP4:
                    x2_change = 0
                if event.key == pygame.K_KP5:
                    y2_change = 0
                if event.key == pygame.K_KP8:
                    y2_change = 0


        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change
        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        war(x1,y1)
        war1(x2,y2)

        if x1>display_width or x1<0:
            crash()
        if y1>display_height or y1<0:
            crash()
        if x2>display_width or x2<0:
            crash()
        if y2>display_height or y2<0:
            crash()
        if x1==x2 and y1==y2:
            crash()

        if(thing_starty > display_height):
            thing_starty =  0- thing_height
            thing_startx = random.randrange(400,1000)

        if flag1 == 1:
            x3 = x1 + 70
            y3 = y1 + 55
            while (x3 < display_width):
                x3 = x3 + 15
                if x3 == thing_startx:
                    x3 = thing_startx
                bullect(x3, y3)
            flag1 = 0

        if thing_starty == y1 and thing_startx == x1:
            crash()
        pygame.display.update()
        clock.tick(20)

gameloop()
pygame.quit()
quit()