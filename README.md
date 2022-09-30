# Snake Game Version 1.0

## Project Overview
- 1. ### Concept
    - The snake game is a classic and the challenge of programming it is definitely a milestone for me. It's is a great and fun project to exercise the implementation of Object Oriented Programming, so I built this game completely class-based (maybe that's not the best approach to implement it, but that's how I'm going to do it).

- 2. ### Technology
    - In view of the simplicity of this game, Python is a great option to do it, mainly because of the Pygame library which makes the implementation of simple games very straightforward and easy (the performance is the best, but for this game that's not a problem). 

- 3. ### Implementation
    - #### Game window
        - The screen (game window) is a square divided in multiple blocks
        - Exemple:
            ```
            width = block * number of blocks (40 * 6) = 240px
            <----------------------------->
            1 block = 40px
            <---->
            +----+----+----+----+----+----+
            |    |    |    |    |    |    |
            +----+----+----+----+----+----+
            |    |    |    |    |    |    |
            +----+----+----+----+----+----+
            |    |    |    |    |    |    |
            +----+----+----+----+----+----+
            |    |    |    |    |    |    |
            +----+----+----+----+----+----+
            |    |    |    |    |    |    |
            +----+----+----+----+----+----+
            |    |    |    |    |    |    |
            +----+----+----+----+----+----+
            ```

    - #### Vectors
        - A 2 dimensional vector stores a position (x,y) in blocks (block size = 40 pixels)
        - Example: 
            - Vector2(2,3) -> (x = 2 blocks, y = 3 blocks)
            - The real postion (in pixels) of this vector would be (2 * block size, 3 * block size) -> (80, 120)

    - #### Snake class
        - The body of the snake is a list of vectors
            - Each vector represents the postion (x,y) of the snake block on the screen

        - Movement
            - If the snake is not growing
                1. Copy the snake body without the last snake block (tail)
                2. Insert the a new snake block (head) in the direction that the snake is moving
                3. The copy is the new snake body
            - If the snake is growing
                1. Copy the snake body
                2. Insert the a new snake block (head) in the direction that the snake is moving
                3. The copy is the new snake body

        - Draw the snake
            - For each vector in the body list, it's created a rect
                - Get the postion (x, y) in pixels
                - Each rect is drawn on the screen

    - #### Fruit class
        - Generates random x and y positions
        - Creates a fruit rect in the generated position
        - Draws the fruit rect on the screen
    
    - #### Game class
        - Contains the pygame setup and most of the game logic

        - Tracks the events (Event loop)
            - Quit game
            - Game update timer (user event)

        - Game state
            - While the snake is alive (the user is plaing the game), the game is active
            - If the snake dies (or the user just started the application), the game is not active, in this case the user sees an intermediate screen

        - Check collisions 
            - Snake head to apple
            - Snake head to wall
            - Snake head to snake body

        - Score
            - Every time the snake eats a fruit, the score counter adds 1 point
            - When the snake dies, the score counter goes back to 0
            - The current score is displayed on the background

        - Update game
            - It's an user event that triggers every 1500ms (you can change that value in settings.py)
                - Snake movement
                - Check collision
                - Check defeat 

        - Draw all the elements (score, snake, fruit) on the screen 

    - #### Settings file
        - Almost all the graphics of this game can be customized by changing the varibles of this file
        - Screen size, colors, text, text position, fonts (font type, color, size), images

- 4. ### Ideas for the next version
    - #### Score rank
        - A feature that I think would be nice to  add is a score rank, which the game would save the 5 five best scores in a text file or JSON file
        - Everytime the player finishes a game, his final score would be compared the the 5 best, if the score is greater than any of them, would replace the score lower than it



## How to run
1. Install the [Python interpreter](https://www.python.org/downloads/)
2. Install the [Pygame library](https://www.pygame.org/wiki/GettingStarted) -> Command: ```pip install pygame```
3. Download the source code
4. Access the game folder
5. Run the main.py file -> Command: ````python main.py```


## How to play
1. Press SPACE to start the game
2. Movement
    - Move up: w or UP
    - Move down: s or DOWN
    - Move right: d or RIGHT
    - Move left: a or LEFT
3. Eat the fruits to score (the snake growns in size)
4. You lose if the snake collides with the wall or with itself


## References
- This project is my implmentation of snake game, but this video taught me the basics of pygame and the concepts of the snake game:
> https://www.youtube.com/watch?v=QFvqStqPCRU&t=6656s

- [Pygame Documentation](https://www.pygame.org/docs/)