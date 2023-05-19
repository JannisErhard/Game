# Game
- add hostile sprite animated
- add pathfinding 
- add player sprite animated
- add functionality to mspawn sprites in runtime
- add culling
- consider bug when spawned inside thresholds border is stuck to cursor

# Bugs 
- if map is smaller than windowsize bumping into the border causes the map to move around (unclear)
- if the map is close enough to the border of the screen the moving stops 



# Considerations
- zoom-in can only mean draw pixelmaps upscaled. as everything is build from tiles which are tilesize^2 changing tilesize is tantamount to zooming 
- if screen is resized tilesize has to be changed accordingly 
- fixed should remain the number of tiles shown on a screen
- hence the screensize can be calulated from the number of tiles and the tilesize
- otherwise the field of view can be changed by scaling up the window and this means gameplay fundamentally changes if finding the exit is relevant  
- draw the map around the player starting position
- choose resolution -> pick tilesize -> need tilesize-x any tilesize-y to be chose separately if it should make sense 
- in general i presume screens have some "reasonable format" 
- the x and y tilesize could be calculated according to some division 
