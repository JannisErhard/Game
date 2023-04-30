#!/usr/bin/env python3
import pygame as pg 
from World.maps import *
import sys
from Tools.make_maps_2 import generate_map,generate_map_labyrinth,generate_map_labyrinth_2,generate_map_labyrinth_3
from Tools.process_map import process 
from Tools.place_in_map import place_in_map
from Tools.collision import collision_check

pg.init()

#  load graphics
ball = pg.image.load("PNGS/intro_ball.gif")
indices = [i for i in range(1,47+1)]
c_indices = [str(i) for i in indices]
water_images = []
for i in indices:
    sublist = []
    sublist.append(pg.image.load(f"PNGS/water_{i}_1.png"))
    sublist.append(pg.image.load(f"PNGS/water_{i}_2.png"))
    sublist.append(pg.image.load(f"PNGS/water_{i}_3.png"))
    sublist.append(pg.image.load(f"PNGS/water_{i}_4.png"))
    water_images.append(sublist)

grass = pg.image.load("PNGS/grass01.png")

seed = 9
n_x_tiles, n_y_tiles = 15, 9
i_zoom = 3
window=(32*n_x_tiles*i_zoom,32*n_y_tiles*i_zoom)
screen = pg.display.set_mode(window, pg.RESIZABLE)
tilesize = screen.get_width()/(n_x_tiles)
background = pg.Surface(window)

# variables for scrolling
thr=tilesize*2
scroll = [0,0]
scroll_memory = [0,0]

small_ball =  pg.transform.scale(ball, (tilesize, tilesize))
ballrect = small_ball.get_rect()


#### Map generation ####
#world = generate_map_labyrinth_3(50,50,seed,20)
world = generate_map(15,15,seed,60)

#### Player Placement ####
player_pos  = pg.Vector2((5)*tilesize, (5)*tilesize)

#player_pos.y, player_pos.x = place_in_map(world)
#player_pos.y, player_pos.x = int(player_pos.y*tilesize) , int(player_pos.x*tilesize)

print(player_pos)



obstacle_list = []
bg_list = []
for y, sublist in enumerate(world):
    for x, tile in enumerate(sublist):
        img = pg.transform.scale(grass,(tilesize,tilesize))
        img_rect = img.get_rect()
        img_rect.x, img_rect.y = x*tilesize,y*tilesize
        tile_data = (img, img_rect)
        bg_list.append(tile_data) 
        if tile in c_indices:
            imgs = []
            for img in water_images[int(tile)-1]:
                imgs.append(pg.transform.scale(img,(tilesize,tilesize)))
            img_rect = imgs[0].get_rect()
            img_rect.x, img_rect.y = x*tilesize,y*tilesize
            tile_data = (imgs, img_rect)
            obstacle_list.append(tile_data)


#### Update the the display and wait ####
done = False


a=0

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        #if event.type == pg.VIDEORESIZE: # this would lead ot problems with the scrolling
        #    screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

    scroll = [0,0]
    keys = pg.key.get_pressed()


    dx, dy = 0, 0
    if keys[pg.K_w]:
        if player_pos.y-dt > 0: 
            dy = -dt
    if keys[pg.K_s]:
        if player_pos.y+dt+tilesize < screen.get_height(): 
            dy =  dt
    if keys[pg.K_a]:
        if  player_pos.x-dt > 0:
            dx =  -dt
    if keys[pg.K_d]:
        if player_pos.x+dt+tilesize < screen.get_width():
            dx =  dt

    dx, dy = collision_check(player_pos,obstacle_list,tilesize,dx,dy)

    # calculate of character has gotten too close to the edge 
    if player_pos.x+dx > screen.get_width() - thr or  player_pos.x+dx < thr:
#    if player_pos.x > screen.get_width() - thr or  player_pos.x < thr:
        scroll[0] = -dx
        dx = 0  
    if player_pos.y+dy > screen.get_height() - thr or player_pos.y+dy < thr:  
        scroll[1] = -dy 
        dy = 0


    # stop scrolling if map Ends 
    abs_p_right =  scroll_memory[0] + player_pos.x + tilesize
    abs_p_left = scroll_memory[0] + player_pos.x
    abs_p_bottom = scroll_memory[1] + player_pos.y + tilesize
    abs_p_top =  scroll_memory[1] + player_pos.y

    if abs_p_right >= len(world[0])*tilesize:
        rest = abs_p_right - len(world[0])*tilesize
        scroll[0] = rest # scrolls rest  
    if abs_p_left <= 0:
        rest = abs_p_left - 0
        scroll[0] = rest
    if abs_p_bottom >= len(world)*tilesize:
        rest = abs_p_bottom -len(world)*tilesize 
        scroll[1] = rest
    if abs_p_top <= 0:
        rest = abs_p_top
        scroll[1] = rest


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
    if a >= 4:
        a=0

    # Debug 
    #for i in range(int(screen.get_width()//tilesize)):
    #    pg.draw.line(screen, (0,0,0), (i*tilesize, 0), (i*tilesize, screen.get_height()))
    #for i in range(int(screen.get_height()//tilesize)):
    #    pg.draw.line(screen, (0,0,0), (0,i*tilesize), (screen.get_width(), i*tilesize))

    screen.blit(small_ball, player_pos)
    pg.display.flip()
    pg.time.Clock().tick(60)
    dt = tilesize/4 #pg.time.Clock().tick(120)/1
## Update the the display and wait ####

pg.quit()

