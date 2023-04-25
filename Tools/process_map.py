#!/usr/bin/env python3
import copy



raw=[[ ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#',  ],
[ '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ',  ],
[ ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ',  ],
[ ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' ',  ],
[ '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#',  ],
[ '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ',  ],
[ '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#',  ],
[ ' ', '#', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ',  ],
[ ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ',  ],
[ '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',  ],
[ ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#',  ],
[ ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#',  ],
[ ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#',  ],
[ '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',  ],
[ ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#',  ],
[ '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ',  ],
[ ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ',  ]]

raw = [ [ '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', '#',  ],
[ '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#',  ],
[ ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ',  ],
[ '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ',  ],
[ '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#',  ],
[ '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', ' ',  ],
[ '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#',  ],
[ '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', '#', ' ',  ],
[ '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', ' ',  ],
[ ' ', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#',  ],
[ ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#',  ],
[ ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#',  ],
[ ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#',  ],
[ ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ',  ],
[ '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#',  ],
[ '#', '#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ',  ],
[ ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#',  ],
[ ' ', ' ', '#', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ',  ],
[ '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ',  ],
[ '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ',  ],
[ ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#',  ],
[ ' ', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#',  ],
[ ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', ' ',  ],
[ '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#',  ],
[ ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ',  ]]

processed = copy.deepcopy(raw)

for i, row in enumerate(raw):
    for j, tile in enumerate(row):
        if i > 0 and j > 0 and i < len(raw)-1 and j < len(raw[0])-1:
            #print(i,j)
            if tile == '#':
                # neighbor is below
                if  raw[i-1][j]  ==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j]  ==' ' :
                   processed[i][j] = '1'
                #################################
                if  raw[i-1][j]  ==' '  and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' :
                   processed[i][j] = '2'
                #################################
                if raw[i-1][j]  ==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  ==' ' :
                   processed[i][j] = '3'
                #################################
                if raw[i-1][j]  =='#' and  raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j]  ==' ' :
                   processed[i][j] = '4'
                #################################
                if  raw[i-1][j]  ==' ' and  raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' '  :
                   processed[i][j] = '5'
                #################################
                if  raw[i-1][j]  =='#' and  raw[i][j-1]  ==' ' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#'  :
                   processed[i][j] = '6'
                #################################
                if  raw[i-1][j]  ==' ' and  raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' '  :
                   processed[i][j] = '7'
                if  raw[i-1][j]  ==' ' and  raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#'  :
                   processed[i][j] = '8'
                if raw[i-1][j]  ==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' :
                   processed[i][j] = '9'
                if  raw[i-1][j]  =='#' and  raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' '  :
                   processed[i][j] = '10'
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  ==' ' : 
                   processed[i][j] = '11'

                ################################# 3 obstacles neighbouring
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' :# right left up down
                   processed[i][j] = '12'
                if raw[i-1][j]  =='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' :
                   processed[i][j] = '13'
                if raw[i-1][j]  ==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' :
                   processed[i][j] = '14'
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' ' :
                   processed[i][j] = '15'
                ################################# 3 obstacles neighbouring, bunched up
                if  raw[i-1][j]  ==' '  and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' and raw[i+1][j-1] == '#': # left bottom
                   processed[i][j] = '19'
                if  raw[i-1][j]  =='#'  and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  ==' ' and raw[i-1][j-1] == '#': # left top
                   processed[i][j] = '18'
                if  raw[i-1][j]  ==' '  and raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i+1][j+1] == '#': # right bottom
                   processed[i][j] = '17'
                if  raw[i-1][j]  =='#'  and raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' ' and raw[i-1][j+1] == '#': # right top
                   processed[i][j] = '16'
                ################################# 4 obstacles, 3 neighbouring, 1 isolated
                #  atop                   left                   right                   below                  
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' and raw[i-1][j-1] == '#':# right left up down
                   processed[i][j] = '27'
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' and raw[i+1][j-1] == '#':# right left up down
                   processed[i][j] = '26'
                if raw[i-1][j]  =='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i-1][j+1] == '#':
                   processed[i][j] = '25'                                                                                           
                if raw[i-1][j]  =='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i+1][j+1] == '#':
                   processed[i][j] = '24'
                if raw[i-1][j]  ==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i+1][j-1] == '#':
                   processed[i][j] = '29'                                                                                           
                if raw[i-1][j]  ==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i+1][j+1] == '#':
                   processed[i][j] = '28'
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' ' and raw[i-1][j-1] == '#':
                   processed[i][j] = '31'                                                                                           
                if raw[i-1][j]  =='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' ' and raw[i-1][j+1] == '#':
                   processed[i][j] = '30'
                ################################# 4 obstacles, 4 isolated
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '44'
                ################################# 5 obstacles neighbouring, bunched up
                # atop                      left                   right               below                      top right                bottom right               
                if  raw[i-1][j]  =='#'  and raw[i][j-1]  ==' ' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i-1][j+1] == '#' and raw[i+1][j+1] == '#' : # left is way
                   processed[i][j] = '20'
                if  raw[i-1][j]  =='#'  and raw[i][j-1]  =='#' and raw[i][j+1]  ==' '  and raw[i+1][j]  =='#' and raw[i-1][j-1] == '#' and raw[i+1][j-1] == '#' : # right is way
                   processed[i][j] = '21'                                                                       # bottom right            
                if  raw[i-1][j]  ==' '  and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  =='#' and raw[i+1][j+1] == '#' and raw[i+1][j-1] == '#': # top is way
                   processed[i][j] = '22'
                if  raw[i-1][j]  =='#'  and raw[i][j-1]  =='#' and raw[i][j+1]  =='#'  and raw[i+1][j]  ==' ' and raw[i-1][j-1] == '#' and raw[i-1][j+1] == '#': # bottom is way
                   processed[i][j] = '23'
                ################################# 5 obstacles neighbouring, bunched up, 2 isolated 
                #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '40'
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '41'
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '42'
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '43'
                ################################# 6 obstacles neighbouring, bunched up, one isolated 
                #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '36'
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '37'
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '38'
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '39'
                ################################# 6 obstacles neighbouring, two bunched groups of 3 
                #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '46'
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '45'
                ################################# 7 obstacles neighbouring, bunched up
                #left top                 top                    top right              left                   right                  bottom left            bottom                 bottom right
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]==' ' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '32'
                if raw[i-1][j-1]==' ' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '33'
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
                   processed[i][j] = '34'
                if raw[i-1][j-1]=='#' and raw[i-1][j]  =='#' and raw[i-1][j+1]=='#' and raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
                   processed[i][j] = '35'

# 32 33 34 35 36 37 38 39 40 41 42 43 44
# 0x x0 00 00 xx x0 0x 00 x0 xx 0x xx xx
# 00 00 x0 0x 00 x0 0x xx xx x0 xx 0x xx
  
        if i == 0 and j > 0 and i < len(raw)-1 and j < len(raw[0])-1:
            if tile == '#':
                # neighbor is below
                if  raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j]  ==' ' :
                   processed[i][j] = '4'
                if  raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j]  =='#' :
                   processed[i][j] = '6'
                if  raw[i][j-1]  ==' ' and raw[i][j+1]  =='#' and raw[i+1][j]  ==' ' :
                   processed[i][j] = '16'
                if  raw[i][j-1]  =='#' and raw[i][j+1]  ==' ' and raw[i+1][j]  ==' ' :
                   processed[i][j] = '18'
                if  raw[i][j-1]  =='#' and raw[i][j+1]  =='#' and raw[i+1][j]  ==' ' :
                   processed[i][j] = '23'

for row in raw:
    print(row)


print("")

for row in processed:
    print(row)
#print(raw)
print("")
print(processed)
# water cases:
#   x 0 x   x 0 x   x 0 x   x 4 x   x 0 x   x A x   x 0 x   x 0 x   x 0 x   x 8 x   x 9 x     x C x    x C x    x 0 x    x C x    0 D D   0 0 0   0 0 0 
#   0 1 0   0 2 0   3 3 0   0 4 0   0 5 5   0 A 0   B B B   0 6 6   7 7 0   8 8 0   0 9 9     C C 0    0 C C    C C C    C C C    0 D D   E E E   E E E
#   x 0 x   x 2 x   x 0 x   x 0 x   x 0 x   x A x   x 0 x   x 6 x   x 7 x   x 0 x   x 0 x     x C x    x C x    x C x    x 0 x    0 0 0   0 E E   E E 0 
#                                                                                                                               
#     1   |   1       3       4       5   |   6       7   |   8       9       10      11   |    12       13       14       15   |       4   |   1       2 
#        raw[i-1][j-1] above left 
#        raw[i-1][j]   above
#        raw[i-1][j+1] above right 
#        raw[i][j-1]   left 
#        raw[i][j+1]   right 
#        raw[i+1][j-1] below left
#        raw[i+1][j]   below 
#        raw[i+1][j+1] below right 



#                if raw[i-1][j-1]=='#' and raw[i-1][j]  ==' ' and raw[i-1][j+1]==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]=='#' and raw[i-1][j]  ==' ' and raw[i-1][j+1]==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]=='#' and raw[i-1][j]  ==' ' and raw[i-1][j+1]==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]==' ' and raw[i-1][j]  ==' ' and raw[i-1][j+1]=='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]==' ' and raw[i-1][j]  ==' ' and raw[i-1][j+1]=='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]==' ' and raw[i-1][j]  ==' ' and raw[i-1][j+1]=='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]=='#' and raw[i-1][j]  ==' ' and raw[i-1][j+1]=='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]=='#' and raw[i-1][j]  ==' ' and raw[i-1][j+1]=='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]=='#' and raw[i-1][j]  ==' ' and raw[i-1][j+1]=='#' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]==' ' and raw[i-1][j]  ==' ' and raw[i-1][j+1]==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]==' ' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]==' ' and raw[i-1][j]  ==' ' and raw[i-1][j+1]==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]=='#' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'
#                if raw[i-1][j-1]==' ' and raw[i-1][j]  ==' ' and raw[i-1][j+1]==' ' and raw[i][j-1]  ==' ' and raw[i][j+1]  ==' ' and raw[i+1][j-1]==' ' and raw[i+1][j]  =='#' and raw[i+1][j+1]=='#' :
#                   processed[i][j] = '2'V
