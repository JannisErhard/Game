#!/usr/bin/env python3
import copy

def right(i,j,raw):
    return raw[i][j+1] == '#'
def left(i,j,raw):
    return raw[i][j-1] == '#'
def top(i,j,raw):
    return raw[i-1][j] == '#'
def bottom(i,j,raw):
    return raw[i+1][j] == '#'

def top_left(i,j,raw):
    return raw[i-1][j-1] == '#'
def top_right(i,j,raw):
    return raw[i-1][j+1] == '#'
def bottom_left(i,j,raw):
    return raw[i+1][j-1] == '#'
def bottom_right(i,j,raw):
    return raw[i+1][j+1] == '#'


def process(raw):
    processed = copy.deepcopy(raw)
    for i, row in enumerate(raw):
        for j, tile in enumerate(row):
            if i > 0 and j > 0 and i < len(raw)-1 and j < len(raw[0])-1:
                #print(i,j)
                if tile == '#':
                    # neighbor is below
                    if  raw[i-1][j] == ' ' and raw[i][j-1] == ' ' and raw[i][j+1] == ' ' and raw[i+1][j] == ' ' :
                       processed[i][j] = '1'
                    #################################
                    if  raw[i-1][j] == ' '  and raw[i][j-1] == ' ' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' :
                       processed[i][j] = '2'
                    #################################
                    if raw[i-1][j] == ' ' and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == ' ' :
                       processed[i][j] = '3'
                    #################################
                    if raw[i-1][j] == '#' and  raw[i][j-1] == ' ' and raw[i][j+1] == ' ' and raw[i+1][j] == ' ' :
                       processed[i][j] = '4'
                    #################################
                    if  raw[i-1][j] == ' ' and  raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == ' '  :
                       processed[i][j] = '5'
                    #################################
                    if  raw[i-1][j] == '#' and  raw[i][j-1] == ' ' and raw[i][j+1] == ' '  and raw[i+1][j] == '#'  :
                       processed[i][j] = '6'
                    #################################
                    if  raw[i-1][j] == ' ' and  raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == ' '  :
                       processed[i][j] = '7'
                    if  raw[i-1][j] == ' ' and  raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == '#'  :
                       processed[i][j] = '8'
                    if raw[i-1][j] == ' ' and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' :
                       processed[i][j] = '9'
                    if  raw[i-1][j] == '#' and  raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == ' '  :
                       processed[i][j] = '10'
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == ' ' : 
                       processed[i][j] = '11'
    
                    ################################# 3 obstacles neighbouring
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' :# right left up down
                       processed[i][j] = '12'
                    if raw[i-1][j] == '#' and raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' :
                       processed[i][j] = '13'
                    if raw[i-1][j] == ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' :
                       processed[i][j] = '14'
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == ' ' :
                       processed[i][j] = '15'
                    ################################# 3 obstacles neighbouring, bunched up
                    if  raw[i-1][j] == ' '  and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' and raw[i+1][j-1] == '#': # left bottom
                       processed[i][j] = '19'
                    if  raw[i-1][j] == '#'  and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == ' ' and raw[i-1][j-1] == '#': # left top
                       processed[i][j] = '18'
                    if  raw[i-1][j] == ' '  and raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i+1][j+1] == '#': # right bottom
                       processed[i][j] = '17'
                    if  raw[i-1][j] == '#'  and raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == ' ' and raw[i-1][j+1] == '#': # right top
                       processed[i][j] = '16'
                    ################################# 4 obstacles, 3 neighbouring, 1 isolated
                    #  atop                   left                   right                   below                  
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' and raw[i-1][j-1] == '#':# right left up down
                       processed[i][j] = '27'
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' and raw[i+1][j-1] == '#':# right left up down
                       processed[i][j] = '26'
                    if raw[i-1][j] == '#' and raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i-1][j+1] == '#':
                       processed[i][j] = '25'                                                                                           
                    if raw[i-1][j] == '#' and raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i+1][j+1] == '#':
                       processed[i][j] = '24'
                    if raw[i-1][j] == ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i+1][j-1] == '#':
                       processed[i][j] = '29'                                                                                           
                    if raw[i-1][j] == ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i+1][j+1] == '#':
                       processed[i][j] = '28'
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == ' ' and raw[i-1][j-1] == '#':
                       processed[i][j] = '31'                                                                                           
                    if raw[i-1][j] == '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == ' ' and raw[i-1][j+1] == '#':
                       processed[i][j] = '30'
                    ################################# 4 obstacles, 4 isolated
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '44'
                    ################################# 5 obstacles neighbouring, bunched up
                    # atop                      left                   right               below                      top right                bottom right               
                    if  raw[i-1][j] == '#'  and raw[i][j-1] == ' ' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i-1][j+1] == '#' and raw[i+1][j+1] == '#' : # left is way
                       processed[i][j] = '20'
                    if  raw[i-1][j] == '#'  and raw[i][j-1] == '#' and raw[i][j+1] == ' '  and raw[i+1][j] == '#' and raw[i-1][j-1] == '#' and raw[i+1][j-1] == '#' : # right is way
                       processed[i][j] = '21'                                                                       # bottom right            
                    if  raw[i-1][j] == ' '  and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == '#' and raw[i+1][j+1] == '#' and raw[i+1][j-1] == '#': # top is way
                       processed[i][j] = '22'
                    if  raw[i-1][j] == '#'  and raw[i][j-1] == '#' and raw[i][j+1] == '#'  and raw[i+1][j] == ' ' and raw[i-1][j-1] == '#' and raw[i-1][j+1] == '#': # bottom is way
                       processed[i][j] = '23'
                    ################################# 5 obstacles neighbouring, bunched up, 2 isolated 
                    #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '40'
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '41'
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '42'
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '43'
                    ################################# 6 obstacles neighbouring, bunched up, one isolated 
                    #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '36'
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '37'
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '38'
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '39'
                    ################################# 6 obstacles neighbouring, two bunched groups of 3 
                    #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '46'
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '45'
                    ################################# 7 obstacles neighbouring, bunched up
                    #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== ' ' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '32'
                    if raw[i-1][j-1]== ' ' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '33'
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== ' ' and raw[i+1][j] == '#' and raw[i+1][j+1]== '#' :
                       processed[i][j] = '34'
                    if raw[i-1][j-1]== '#' and raw[i-1][j] == '#' and raw[i-1][j+1]== '#' and raw[i][j-1] == '#' and raw[i][j+1] == '#' and raw[i+1][j-1]== '#' and raw[i+1][j] == '#' and raw[i+1][j+1]== ' ' :
                       processed[i][j] = '35'
                    if top(i,j,raw) and bottom(i,j,raw) and left(i,j,raw) and right(i,j,raw) and top_left(i,j,raw) and top_right(i,j,raw) and bottom_left(i,j,raw) and bottom_right(i,j,raw):
                        processed[i][j] = '47'
    
      
            if i == 0 and j > 0 and i < len(raw)-1 and j < len(raw[0])-1: # top  border
                if tile == '#':
                    processed[i][j] = '4'
                    if bottom(i,j,raw):
                        processed[i][j] = '6'
                    if right(i,j,raw):
                        processed[i][j] = '16'
                    if left(i,j,raw):
                        processed[i][j] = '18'
                    if bottom(i,j,raw) and right(i,j,raw):
                        processed[i][j] = '20'
                    if bottom(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '21'
                    if right(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '23'
                    if bottom(i,j,raw) and right(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '39'
                    if bottom(i,j,raw) and right(i,j,raw) and left(i,j,raw) and bottom_left(i,j,raw):
                        processed[i][j] = '35'
                    if bottom(i,j,raw) and right(i,j,raw) and left(i,j,raw) and bottom_right(i,j,raw):
                        processed[i][j] = '34'
                    if bottom(i,j,raw) and right(i,j,raw) and left(i,j,raw) and bottom_left(i,j,raw) and bottom_right(i,j,raw):
                        processed[i][j] = '47'
            if i > 0 and j > 0 and i == len(raw)-1 and j < len(raw[0])-1: # bottom border
                if tile == '#':
                    processed[i][j] = '2'
                    if top(i,j,raw):
                        processed[i][j] = '6'
                    if right(i,j,raw):
                        processed[i][j] = '17'
                    if left(i,j,raw):
                        processed[i][j] = '19'
                    if top(i,j,raw) and right(i,j,raw):
                        processed[i][j] = '20'
                    if top(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '21'
                    if right(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '22'
                    if top(i,j,raw) and right(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '36'
                    if top(i,j,raw) and right(i,j,raw) and left(i,j,raw) and top_left(i,j,raw):
                        processed[i][j] = '32'
                    if top(i,j,raw) and right(i,j,raw) and left(i,j,raw) and top_right(i,j,raw):
                        processed[i][j] = '33'
                    if top(i,j,raw) and right(i,j,raw) and left(i,j,raw) and top_left(i,j,raw) and top_right(i,j,raw):
                        processed[i][j] = '47'
    
            if i > 0 and j > 0 and i < len(raw)-1 and j == len(raw[0])-1: # right border 
                if tile == '#':
                    processed[i][j] = '5'
                    if top(i,j,raw):
                        processed[i][j] = '16'
                    if bottom(i,j,raw):
                        processed[i][j] = '17'
                    if left(i,j,raw):
                        processed[i][j] = '7'
                    if top(i,j,raw) and bottom(i,j,raw):
                        processed[i][j] = '20'
                    if top(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '23'
                    if bottom(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '22'
                    if top(i,j,raw) and bottom(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '37'
                    if top(i,j,raw) and bottom(i,j,raw) and left(i,j,raw) and top_left(i,j,raw):
                        processed[i][j] = '34'
                    if top(i,j,raw) and bottom(i,j,raw) and left(i,j,raw) and bottom_left(i,j,raw):
                        processed[i][j] = '33'
                    if top(i,j,raw) and bottom(i,j,raw) and left(i,j,raw) and bottom_left(i,j,raw) and top_left(i,j,raw):
                        processed[i][j] = '47'
    
            if i > 0 and j == 0 and i < len(raw)-1 and j < len(raw[0])-1: # left border
                if tile == '#':
                    processed[i][j] = '3'
                    if raw[i-1][j]== '#':
                        processed[i][j] = '18'
                    if raw[i][j+1] == '#':
                        processed[i][j] = '7'
                    if raw[i+1][j] == '#':
                        processed[i][j] = '19'
                    if  raw[i-1][j] == '#' and  raw[i+1][j] == '#':
                        processed[i][j] = '21'
                    if  raw[i-1][j] == '#' and  raw[i][j+1] == '#':
                        processed[i][j] = '31'
                    if  raw[i+1][j] == '#' and  raw[i][j+1] == '#':
                        processed[i][j] = '29'
                    if raw[i-1][j] == '#' and  raw[i][j+1] == '#'  and  raw[i-1][j+1] == '#':
                        processed[i][j] = '23'
                    if raw[i+1][j] == '#' and  raw[i][j+1] == '#'  and  raw[i+1][j+1] == '#':
                        processed[i][j] = '22'
                    if raw[i-1][j] == '#' and  raw[i+1][j] == '#'  and  raw[i][j+1] == '#':
                        processed[i][j] = '38'
                    if raw[i-1][j] == '#' and  raw[i+1][j] == '#'  and  raw[i][j+1] == '#' and raw[i+1][j+1] == '#':
                        processed[i][j] = '32'
                    if raw[i-1][j] == '#' and  raw[i+1][j] == '#'  and  raw[i][j+1] == '#' and raw[i-1][j+1] == '#':
                        processed[i][j] = '35'
                    if raw[i-1][j] == '#' and  raw[i+1][j] == '#'  and  raw[i][j+1] == '#' and raw[i-1][j+1] == '#' and raw[i+1][j+1] == '#':
                        processed[i][j] = '47'
    
            if i == 0 and j == 0 and i < len(raw)-1 and j < len(raw[0])-1: # top left corner
                if tile == '#':
                    processed[i][j] = '18'
                    if bottom(i,j,raw):
                        processed[i][j] = '21'
                    if right(i,j,raw):
                        processed[i][j] = '23'
                    if bottom(i,j,raw) and right(i,j,raw):
                        processed[i][j] = '35'
                    if bottom(i,j,raw) and right(i,j,raw) and bottom_right(i,j,raw):
                        processed[i][j] = '47'
    
            if i > 0 and j == 0 and i == len(raw)-1 and j < len(raw[0])-1: # bottom left corner
                if tile == '#':
                    processed[i][j] = '19'
                    if top(i,j,raw):
                        processed[i][j] = '21'
                    if right(i,j,raw):
                        processed[i][j] = '22'
                    if top(i,j,raw) and right(i,j,raw):
                        processed[i][j] = '32'
                    if top(i,j,raw) and right(i,j,raw) and top_right(i,j,raw):
                        processed[i][j] = '47'
    
            if i == 0 and j > 0 and i < len(raw)-1 and j == len(raw[0])-1: # top right corner
                if tile == '#':
                    processed[i][j] = '16'
                    if bottom(i,j,raw):
                        processed[i][j] = '20'
                    if left(i,j,raw):
                        processed[i][j] = '23'
                    if bottom(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '34'
                    if bottom(i,j,raw) and left(i,j,raw) and bottom_left(i,j,raw):
                        processed[i][j] = '47'
    
            if i > 0 and j > 0 and i == len(raw)-1 and j == len(raw[0])-1: # bottom right corner
                if tile == '#':
                    processed[i][j] = '17'
                    if top(i,j,raw):
                        processed[i][j] = '20'
                    if left(i,j,raw):
                        processed[i][j] = '22'
                    if top(i,j,raw) and left(i,j,raw):
                        processed[i][j] = '33'
                    if top(i,j,raw) and left(i,j,raw) and top_left(i,j,raw):
                        processed[i][j] = '47'
    return processed





# water cases:
#   x 0 x   x 0 x   x 0 x   x 4 x   x 0 x   x A x   x 0 x   x 0 x   x 0 x   x 8 x   x 9 x     x C x    x C x    x 0 x    x C x    0 D D   0 0 0   0 0 0 
#   0 1 0   0 2 0   3 3 0   0 4 0   0 5 5   0 A 0   B B B   0 6 6   7 7 0   8 8 0   0 9 9     C C 0    0 C C    C C C    C C C    0 D D   E E E   E E E
#   x 0 x   x 2 x   x 0 x   x 0 x   x 0 x   x A x   x 0 x   x 6 x   x 7 x   x 0 x   x 0 x     x C x    x C x    x C x    x 0 x    0 0 0   0 E E   E E 0 
#                                                                                                                               
#     1   |   1       3       4       5   |   6       7   |   8       9       10      11   |    12       13       14       15   |       4   |   1       2 
