def collision_check(player_pos,obstacle_list,tilesize,dx,dy):
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
        if (player_pos.x+tilesize == tile[1].x or player_pos.x == tile[1].x+tilesize) and (player_pos.y+tilesize == tile[1].y or player_pos.y == tile[1].y+tilesize):
            # standing top left edge moving down right -> forbidden
            if player_pos.x+tilesize == tile[1].x  and player_pos.y+tilesize == tile[1].y and dx > 0 and dy > 0:
                dx, dy = 0,0
            # standing bottom left edge moving up right -> forbidden
            if player_pos.x+tilesize == tile[1].x  and player_pos.y == tile[1].y+tilesize and dx > 0 and dy < 0:
                dx, dy = 0,0
            # standing top right edge moving bottom left -> forbidden
            if player_pos.x == tile[1].x+tilesize  and player_pos.y+tilesize == tile[1].y and  dx < 0 and dy > 0:
                dx, dy = 0,0
            # standing bottom right edge moving top left -> forbidden
            if player_pos.x == tile[1].x+tilesize  and player_pos.y == tile[1].y+tilesize and dx < 0 and dy < 0:
                dx, dy = 0,0
    return dx,dy
