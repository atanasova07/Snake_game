# Snake_game
Snake game
### **Description:**
There are two options to play this game: with a friend(two players) or alone(one player). 
Another functionality is viewing the last 10 results(scoreboard).
On the playing field there are a few obstacles. Their role is to make the game more difficult. 
There are different figures to be eaten by the snake.


### **Deep dive in the game:**
There are 4 types of figures:
    - "circle" - it gives you one point and one square to length of the snake. The snake needs to eat it, otherwise there will not appear new figure;
    - "triangle" - if your snake is smaller than 4 squares, the game ends. Its function is basically to remove 2 squares from the snake. The figure is on the screen for a while and then disappears;
    - "turtle" - it gives you three points and three squares to length of the snake. The figure is on the screen for a while and then disappears;
    - "square" - it gives you one chance to hit the wall and not to die.
