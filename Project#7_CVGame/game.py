import numpy as np
import pygame,sys
import cv2 as cv
import os

pygame.font.init() 

H,W= 500,800
screen =pygame.display.set_mode((W,H))
pygame.display.set_caption("Pong")
clock=pygame.time.Clock()
ball=pygame.Rect(W/2-15,H/2-15,30,30)
centerCircle=pygame.Rect(W/2-60,H/2-60,120,120)
player1=pygame.Rect(0,H/2,10,70)
player2=pygame.Rect(W-10,H/2,10,70)
lightGrey=(200,200,200)
ballSpeedX=5
ballSpeedY=7
bg_color=pygame.Color('grey12')
playerSpeed=0
opponent_speed=0
score=0
score_colour=(0, 255, 0)
font1 =pygame.font.SysFont("Arial", 30)
 

while True:
    for events in pygame.event.get():\

        
        if events.type==pygame.KEYDOWN:
            if events.key==pygame.K_DOWN:
                playerSpeed+=7
            if events.key==pygame.K_UP:
                playerSpeed+=-7
        if events.type==pygame.KEYUP:
            if events.key==pygame.K_UP:
                    playerSpeed+=+7
            if events.key==pygame.K_DOWN:
                playerSpeed+=-7
    screen.fill(bg_color)
    pygame.draw.ellipse(screen,lightGrey,ball)
    pygame.draw.ellipse(screen,lightGrey,centerCircle,2)
    pygame.draw.rect(screen,lightGrey,player1)
    pygame.draw.rect(screen,lightGrey,player2)
    pygame.draw.aaline(screen,lightGrey,(W/2,0),(W/2,H))
    


    ball.x +=ballSpeedX
    ball.y +=ballSpeedY
    player1.y +=playerSpeed
    player2.y +=opponent_speed
    if ball.colliderect(player1) or ball.colliderect(player2):
        ballSpeedX *=-1
    if ball.colliderect(player1):
        score+=1
        score_colour=(0, 255, 0)
    if ball.top<= 0 or ball.bottom>=H:
        ballSpeedY *=-1
    if ball.left<= 0 or ball.right>=W:
        ballSpeedX *=-1
        score_colour=(255,0,0)

    # print(player1.top)
    if player1.top <=0:
        player1.top=0
    if player1.bottom >=H :
        player1.bottom=H
    if player2.top <=0:
        player2.top=0
    if player2.bottom >=H :
        player2.bottom=H
    
    if player2.bottom<=ball.bottom and ball.x >W/2:
        opponent_speed =7
    elif player2.top>=ball.top and ball.x >W/2:
        opponent_speed =-7
    else :
        opponent_speed =0
    

    text1 = font1.render(f'Score {score}', True, score_colour)
    textRect1 = text1.get_rect()
    textRect1.right=W-30
    textRect1.top=10
    screen.blit(text1,textRect1)

    





    if events.type==pygame.QUIT:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(90)

