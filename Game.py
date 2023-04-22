#!/usr/bin/env python3
import pygame
from World.maps import *

pygame.init()

#  load graphics
ball = pygame.image.load("PNGs/intro_ball.gif")
tilset = pygame.image.load("PNGS/032-Heaven01_b.png")
water_autotiles = pygame.image.load("PNGS/001-G_Water01.png")
water_images = []
water_images.append(pygame.image.load("PNGS/water_0.png"))
water_images.append(pygame.image.load("PNGS/water_1.png"))
water_images.append(pygame.image.load("PNGS/water_2.png"))
water_images.append(pygame.image.load("PNGS/water_3.png"))
grass = pygame.image.load("PNGS/grass01.png")

n_x_tiles, n_y_tiles = 15, 9
i_zoom =3 
window=(32*n_x_tiles*i_zoom,32*n_y_tiles*i_zoom)
screen = pygame.display.set_mode(window, pygame.RESIZABLE)
tilesize = screen.get_width()/n_x_tiles 
background = pygame.Surface(window)

# variables for scrolling
thr=tilesize*4
scroll = [0,0]
scroll_memory = [0,0]

small_ball =  pygame.transform.scale(ball, (tilesize, tilesize))
ballrect = small_ball.get_rect()


#### Populate the surface with objects to be displayed ####
world = campaign[1]
obstacle_list = []
bg_list = []
for y, sublist in enumerate(world):
    for x, tile in enumerate(sublist):
        img = pygame.transform.scale(grass,(tilesize,tilesize))
        img_rect = img.get_rect()
        img_rect.x, img_rect.y = x*tilesize,y*tilesize
        tile_data = (img, img_rect)
        bg_list.append(tile_data) 
        if tile == '#':
            imgs = []
            for img in water_images:
                imgs.append(pygame.transform.scale(img,(tilesize,tilesize)))
            img_rect = imgs[0].get_rect()
            img_rect.x, img_rect.y = x*tilesize,y*tilesize
            tile_data = (imgs, img_rect)
            obstacle_list.append(tile_data)

print(obstacle_list[0])

#### Update the the display and wait ####
done = False

player_pos  = pygame.Vector2((5)*tilesize, (5)*tilesize)

a=0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #if event.type == pygame.VIDEORESIZE: # this would lead ot problems with the scrolling
        #    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    scroll = [0,0]
    keys = pygame.key.get_pressed()


    dx, dy = 0, 0
    if keys[pygame.K_w]:
        if player_pos.y-dt > 0: 
            dy = -dt
    if keys[pygame.K_s]:
        if player_pos.y+dt+tilesize < screen.get_height(): 
            dy =  dt
    if keys[pygame.K_a]:
        if  player_pos.x-dt > 0:
            dx =  -dt
    if keys[pygame.K_d]:
        if player_pos.x+dt+tilesize < screen.get_width():
            dx =  dt




    for tile in obstacle_list:
        # p_{x_r} > t_{x_l} > p_{x_r} + dx & not (tile_{y_t} > p_{y_t} or p_{y_b} < t_{y_b})
        if player_pos.x+tilesize <= tile[1].x and tile[1].x < player_pos.x+tilesize+dx and not (player_pos.y+tilesize <= tile[1].y or player_pos.y >= tile[1].y+tilesize):
            dx = 0
        # p_{x_l} > t_{x_r} > p_{x_l} + dx & not (tile_{y_t} > p_{y_t} or p_{y_b} < t_{y_b})
        if player_pos.x >= tile[1].x+tilesize and tile[1].x+tilesize > player_pos.x+dx and not (player_pos.y+tilesize <= tile[1].y or player_pos.y >= tile[1].y+tilesize):
            dx = 0
        # p_{y_b} > t_{y_t} > p_{y_b} + dy & not (tile_{x_r} < p_{x_l} or tile_{x_l} > p_{x_r})
        if player_pos.y+tilesize <= tile[1].y and tile[1].y < player_pos.y+tilesize+dy and not (player_pos.x+tilesize <= tile[1].x or player_pos.x >= tile[1].x+tilesize):
            dy = 0
        # p_{y_t} > t_{y_b} > p_{y_t} + dy & not (tile_{x_r} < p_{x_l} or tile_{x_l} > p_{x_r})
        if player_pos.y >= tile[1].y+tilesize and tile[1].y+tilesize > player_pos.y+dy and not (player_pos.x+tilesize <= tile[1].x or player_pos.x >= tile[1].x+tilesize):
            dy = 0


    # calculate of character has gotten too close to the edge 
    if player_pos.x+dx > screen.get_width() - thr or  player_pos.x+dx < thr:
#    if player_pos.x > screen.get_width() - thr or  player_pos.x < thr:
        scroll[0] = -dx
        dx = 0  
    elif player_pos.y+dy > screen.get_height() - thr or player_pos.y+dy < thr:  
        scroll[1] = -dy 
        dy = 0


    # stop scrolling if map Ends 
    abs_p_right =  scroll_memory[0] + player_pos.x + tilesize
    abs_p_left = scroll_memory[0] + player_pos.x
    abs_p_bottom = scroll_memory[1] + player_pos.y + tilesize
    abs_p_top =  scroll_memory[1] + player_pos.y
    print(player_pos.x, scroll[0], scroll_memory[0])

    if abs_p_right >= len(world[0])*tilesize:
        rest = abs_p_right - len(world[0])*tilesize
        scroll[0] = rest # scrolls rest  
        if rest == 0:
            print("Stuck 3")
    if abs_p_left <= 0:
        rest = abs_p_left - 0
        scroll[0] = rest
        if rest == 0:
            print("Stuck 4")
    if abs_p_bottom >= len(world)*tilesize:
        rest = abs_p_bottom -len(world)*tilesize 
        scroll[1] = rest
        if rest == 0:
            print("Stuck 5")
    if abs_p_top <= 0:
        rest = abs_p_top
        scroll[1] = rest
        if rest == 0:
            print("Stuck 6")


    print(scroll[0])
    scroll_memory[0] -= scroll[0]
    scroll_memory[1] -= scroll[1]

    player_pos.x, player_pos.y = player_pos.x+dx, player_pos.y+dy
    ballrect.x, ballrect.y = player_pos[0],player_pos[1]

    # shift bottom layer if character gets too close to the edge 
    for tile in bg_list:
        tile[1][0] = tile[1][0] + scroll[0]
        tile[1][1] = tile[1][1] + scroll[1]

    # shift obstacle layer if character gets too close to the edge 
    for tile in obstacle_list:
        tile[1][0] = tile[1][0] + scroll[0]
        tile[1][1] = tile[1][1] + scroll[1]

    screen.fill((0,0,0)) 
    for tile in bg_list:
        screen.blit(tile[0], tile[1])
    for tile in obstacle_list:
        screen.blit(tile[0][int(a)], tile[1])

    a+=0.3
    print(int(a)%4)
    if a >= 4:
        a=0


    screen.blit(small_ball, player_pos)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    dt = tilesize/4 #pygame.time.Clock().tick(120)/1
## Update the the display and wait ####

pygame.quit()

