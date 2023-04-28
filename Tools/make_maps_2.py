#!/usr/bin/env python3
import copy
import random
from .process_map import process

len_y = 25
len_x = 25 
possible_directions = [[0,1],[1,0],[-1,0],[0,-1]]

def walker(i,j,max_i,max_j):
    ri = random.randint(1,2)
    if ri == 1:
        i += 1
    if ri == 2:
        j += 1
    return i,j,' ',(i==max_i-1 or j==max_j-1)

def walker_3(i,j,max_i,max_j,direction):
    ri = random.randint(1,10)
    if ri > 4:
        direction = possible_directions[random.randint(0,1)]

    i,j = i+direction[0], j+direction[1]
    return i,j,' ',(i==max_i-1 or j==max_j-1 or j == 0 or i == 0)

def walker_2(i,j,max_i,max_j,direction):
    ri = random.randint(1,10)
    if ri > 6:
        direction[0], direction[1] =  random.randint(-1,1),  random.randint(-1,1)

    i,j = i+direction[0], j+direction[1]
    return i,j,' ',(i==max_i-1 or j==max_j-1 or j == 0 or i == 0)


def generate_map_labyrinth_3(len_x,len_y,seed,walkers):
    random.seed(seed)
    raw = []
    for i in range(len_y):
        sublist = []
        for j in range(len_x):
            sublist.append('#')
        raw.append(sublist)

    direction = [0,0]
    direction =  possible_directions[random.randint(0,3)]
    for i in range(walkers):
        a,b = random.randint(1,len_x-1),random.randint(1,len_y-1)

        alive = True 
        die = False 
        while alive:
            a,b,raw[a][b],die = walker_3(a,b,len_x,len_y,direction)
            if die:
                alive = False
    processed = process(raw)
    return processed

def generate_map_labyrinth_2(len_x,len_y,seed,walkers):
    random.seed(seed)
    raw = []
    for i in range(len_y):
        sublist = []
        for j in range(len_x):
            sublist.append('#')
        raw.append(sublist)

    direction = [0,0]
    direction[0], direction[1] = random.randint(-1,1),  random.randint(-1,1)
    for i in range(walkers):
        a,b = random.randint(1,len_x-1),random.randint(1,len_y-1)

        alive = True 
        die = False 
        while alive:
            print(a,b)
            a,b,raw[a][b],die = walker_2(a,b,len_x,len_y,direction)
            if die:
                alive = False
    processed = process(raw)
    return processed

def generate_map_labyrinth(len_x,len_y,seed,walkers):
    walkers = 10
    random.seed(seed)
    raw = []
    for i in range(len_y):
        sublist = []
        for j in range(len_x):
            sublist.append('#')
        raw.append(sublist)
    for i in range(walkers):
        a,b = random.randint(1,len_x//2),random.randint(1,len_y//2)
        alive = True 
        die = False 
        while alive:
            a,b,raw[a][b],die = walker(a,b,len_x,len_y)
            if die:
                alive = False
    processed = process(raw)
    return processed

def generate_map(len_x,len_y,seed):
    random.seed(seed)
    raw = []
    for i in range(len_y):
        sublist = []
        for j in range(len_x):
            ri = random.randint(1,6)
            if ri > 4:
                sublist.append(' ')
            else:
                sublist.append('#')
        raw.append(sublist)
    processed = process(raw)
    return processed
