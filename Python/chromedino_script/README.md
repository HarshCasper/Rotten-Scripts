# Chrome Dino Game Automation Using Python

## Description
This python scripts enables chrome dinosaur to play chrome dino game automatically.


## Execution 
* Run `pip install -r requirements.txt` .
* Run `python coordinates.py` for knowing the cooridnates of your screen.
* Go to the `chrome://dino` in your Google Chrome Browser.
* Run `python enemy_location_checker.py` to know the location of cactus and bird (obstacles for dino).
* Now , Run `python main.py`  
* Then go to the `chrome://dino` in your Google Chrome Browser and press any key from keyboard to start the game.
* See how it plays and press a key to interrupt/stop the game.


##Features of files
### Coordinates.py:
To know the coordinates of screen first we need to find the X and Y locations of screen .

### enemy_location_checker.py:
To make dino identify the cactus and bird , captured the image of two make a frame of it and trained dino to escape it.
As , there are only three colors present in this game : black(for night) , white(for day)  and gray(for obstacles and dino)
So , To match the gray pixels of obstacle to make identify dino for obstacle and if obstacle is close to dino then make a jump. 
For this take a image with obstacles coming in between using **ImageGrab from pillow library** and then find out the pixels in which the obstacles are coming. 

### main.py
As game continues, search width has to be increased for bot.For this **time module from python** helps to simulate the dino acceleration.
Also reverse the loop for dino to get searched from back of screenshot to identify obstacle and it will speed up the program.



** All the requirements for this script is mentioned in **requirements.txt** file.






![Demo of the Game](demo_dinogame.gif)
