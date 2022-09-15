import pygame
import random

pygame.init()

win = pygame.display.set_mode((500,500))

tom = pygame.image.load('tom.png')
jerry = pygame.image.load('jerry.png')

pygame.display.set_caption('Tom & Jerry')

font = pygame.font.SysFont('arial', 20, True)

run = True

x = 200
y = 200
dr_x = 1
dr_y = 0
coins = 0

cx = random.randint(1, 480)
cy = random.randint(1, 480)

def frame_format():
    win.fill((0,0,0))
    score = font.render('Jerry caught: ' + str(coins), 1,(0,0,255))
    win.blit(score, (30, 30))
    win.blit(tom, (x,y))
    win.blit(jerry, (cx, cy))
    pygame.display.update()
    

while run:
    pygame.time.delay(50)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        dr_x = -1
        dr_y = 0
    if keys[pygame.K_RIGHT]:
        dr_x = 1
        dr_y = 0
    if keys[pygame.K_UP]:
        dr_x = 0
        dr_y = -1
    if keys[pygame.K_DOWN]:
        dr_x = 0
        dr_y = 1
    if 480 > x + dr_x *5 > 0:
        x += dr_x *5
    if 480 > y + dr_y*5 > 0:
        y += dr_y*5

    
    if cx <= x <= cx+20 and cy <= y <= cy+20 or cx <= x+20 <= cx+20 and cy <= y+20 <= cy+20 or cx <= x+20 <= cx+20 and cy <= y <= cy+20 or cx <= x <= cx+20 and cy <= y+20 <= cy+20:
        coins += 1
        cx = random.randint(1, 480)
        cy = random.randint(1, 480)

    
    
    frame_format()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
