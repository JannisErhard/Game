def place_in_map(level):
    for i, row in enumerate(level):
        for j, tile in enumerate(row):
            if tile == ' ':
                return i,j

