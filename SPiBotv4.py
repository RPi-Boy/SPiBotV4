import pygame
from gpiozero import Robot

robot= Robot(left=(7,8) , right=(9,10))#or whatever gpio pins you used
pygame.init()
screen= pygame.display.set_mode((400,400))
#creates a window for game here the window to control the bot

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygme.QUIT:
            done=true
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                robot.forward()
            if event.key==pygame.K_s:
                robot.backward()
            if event.key==pygame.K_a:
                robot.left()
            if event.key==pygame.K_d:
                robot.right()
            if event.key==pygame.K_x:
                robot.stop()
