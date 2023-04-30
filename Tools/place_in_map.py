OFFSET_Y = 3
OFFSET_X = 3
def place_in_map(level):
    for i, row in enumerate(level[OFFSET_Y:]):
        for j, tile in enumerate(row[OFFSET_X:]):
            if tile == ' ':
                return i+OFFSET_Y,j+OFFSET_X

