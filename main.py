import pygame
from pygame.math import Vector2
from sys import exit
from settings import *
from random import randint



class SNAKE:
    def __init__(self):
        # [head, snake_block, tail]
        self.body = [Vector2(9,10), Vector2(10,10), Vector2(11, 10)]
        # Diretion the snake is initially moving (left)
        self.direction = Vector2(-1,0)
        self.new_block = False

    
    def move(self):
        # if a new block it's being added
        if self.new_block:
            body_copy = self.body[:]
            
        # if the snkaing is just moving
        else:
            body_copy = self.body[:-1] # without the tail

        # Insert the new head (previous head + direction (-1,0)) in the first position of the body copy
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new_block = False


    def add_new_block(self):
        self.new_block = True


    def draw(self):
        # For each snake block of the body, create a rect and draw it on the screen
        for snake_block in self.body:
            x_pos = snake_block.x * BLOCK_SIZE
            y_pos = snake_block.y * BLOCK_SIZE

            snake_body_rect = pygame.Rect(x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE)

            pygame.draw.rect(pygame.display.get_surface(), SNAKE_COLOR, snake_body_rect)



class FRUIT:
    def __init__(self):
        self.randomize()


    def randomize(self):
        # Generate random spawn postions
        self.x = randint(0, BLOCK_NUMBER - 1)
        self.y = randint(0, BLOCK_NUMBER - 1)
        self.pos = (self.x, self.y)


    def draw(self):
        # Create the fruit rect and draw it on the screen
        x_pos = self.x * BLOCK_SIZE
        y_pos = self.y * BLOCK_SIZE

        fruit_rect = pygame.Rect(x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE)

        pygame.draw.rect(pygame.display.get_surface(), FRUIT_COLOR, fruit_rect)



class SnakeGame:
    def __init__(self):
        # Setup
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption(TITLE_TEXT)
        self.clock = pygame.time.Clock()

        # Text
        self.big_text_font = pygame.font.Font(TEXT_FONT_PATH, BIG_FONT_SIZE)
        self.normal_text_font = pygame.font.Font(TEXT_FONT_PATH, NORMAL_FONT_SIZE)

        # Game Objects
        self.snake = SNAKE()
        self.fruit = FRUIT()

        # User events
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, GAME_UPDATE_TIME)

        # Game variables
        self.game_active = False
        self.score = 0


    def reset(self):
        # Reset the snake, the score and generate a new fruit
        self.game_active = True
        self.score = 0
        self.snake.body = [Vector2(9,10), Vector2(10,10), Vector2(11, 10)]
        self.snake.direction = Vector2(-1,0)
        self.fruit.randomize()


    def draw_title(self):
        title_text_surface = self.big_text_font.render(TITLE_TEXT, False, TITLE_COLOR)
        title_text_rect = title_text_surface.get_rect(center = TITLE_POS)
        self.screen.blit(title_text_surface, title_text_rect)


    def draw_play_message(self):
        play_text_surface = self.normal_text_font.render(PLAY_TEXT, False, PLAY_COLOR)
        play_text_rect = play_text_surface.get_rect(center = PLAY_POS)
        self.screen.blit(play_text_surface, play_text_rect)


    def draw_score(self):
        if self.game_active:
            score_surface = self.big_text_font.render(str(self.score), False, SCORE_COLOR)
            score_rect = score_surface.get_rect(center = (MIDDLE_POS, MIDDLE_POS))
            self.screen.blit(score_surface, score_rect)

    
    def draw_snake_image(self):
        snake_surface = pygame.image.load(SNAKE_IMAGE_PATH)
        scaled_snake_surface = pygame.transform.rotozoom(snake_surface, 0, SNAKE_IMAGE_SCALE)
        snake_rect = scaled_snake_surface.get_rect(center=SNAKE_IMAGE_POS)
        self.screen.blit(scaled_snake_surface,snake_rect)


    def check_fruit_collision(self):
        # If the head of the snake is in the same position of the fruit
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.score += 1
            self.snake.add_new_block()


    def check_wall_collision(self):
        # If the head of the snake is outside the screen (collision with the wall)
        if not 0 <= self.snake.body[0].x < BLOCK_NUMBER or not 0 <= self.snake.body[0].y < BLOCK_NUMBER:
            return True

    
    def check_self_collision(self):
        # Check if the head of the snake is in the same position of any snake block
        for snake_block in self.snake.body[1:]:
            if self.snake.body[0] == snake_block: 
                return True


    def check_defeat(self):
        if self.check_wall_collision() or self.check_self_collision():
            self.game_active = False


    def update(self):
        self.snake.move()
        self.check_fruit_collision()
        self.check_defeat()


    def draw(self):
        self.draw_score()
        self.snake.draw()
        self.fruit.draw()

    
    def key_input(self, event):
        # move up if not moving down
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            if self.snake.direction.y != 1:
                self.snake.direction = Vector2(0, -1)
        # move down if not moving up
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if self.snake.direction.y != -1:
                self.snake.direction = Vector2(0, 1)
        # move left if not moving right
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if self.snake.direction.x != 1:
                self.snake.direction = Vector2(-1, 0)
        # move right if not moving left
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if self.snake.direction.x != -1:
                self.snake.direction = Vector2(1, 0)


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active:
                if event.type == self.GAME_UPDATE:
                    self.update()

                if event.type == pygame.KEYDOWN:
                    self.key_input(event)

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset()



    def run(self):
        while True:
            self.event_loop()

            if self.game_active:
                self.screen.fill(BACKGROUND_COLOR)

                self.draw()
            
            else:
                self.screen.fill(BACKGROUND_COLOR)
                self.draw_snake_image()
                self.draw_title()
                self.draw_play_message()

            pygame.display.update()
            self.clock.tick(FPS)



snake_game = SnakeGame()

if __name__ == "__main__":
    snake_game.run()
    