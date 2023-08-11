import pygame
from pygame.locals import *
import time
import random

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert_alpha()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,10)*SIZE
        self.y = random.randint(1,10)*SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("square.png").convert_alpha()
        self.eye_left = pygame.image.load("eye_left small.jpg").convert()
        self.eye_right = pygame.image.load("eye_right small.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]
        self.background_img = pygame.image.load("snake_background.jpg").convert()
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
      eye_left_pos = None
      eye_right_pos = None

    # Clear the screen with the background image
      self.parent_screen.blit(self.background_img, (0, 0))

      for i in range(self.length):
        self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        if i == 0:
            if self.direction == 'left':
                eye_left_pos = (self.x[i] + 10, self.y[i] + 10)
                eye_right_pos = (self.x[i] + SIZE - 20, self.y[i] + 10)
            elif self.direction == 'right':
                eye_left_pos = (self.x[i] + 10, self.y[i] + 10)
                eye_right_pos = (self.x[i] + SIZE - 20, self.y[i] + SIZE - 20)
            elif self.direction == 'up':
                eye_left_pos = (self.x[i] + 10, self.y[i] + 10)
                eye_right_pos = (self.x[i] + SIZE - 20, self.y[i] + 10)
            elif self.direction == 'down':
                eye_left_pos = (self.x[i] + 10, self.y[i] + SIZE - 20)
                eye_right_pos = (self.x[i] + SIZE - 20, self.y[i] + SIZE - 20)

      if eye_left_pos is not None and eye_right_pos is not None:
        self.parent_screen.blit(self.eye_left, eye_left_pos)
        self.parent_screen.blit(self.eye_right, eye_right_pos)

      pygame.display.flip()


    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake game")
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.background_img = pygame.image.load("snake_background.jpg").convert_alpha()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.surface.blit(self.background_img, (0, 0))
        self.snake.draw()
        self.apple.draw()
      
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occured"
        if not (0 <= self.snake.x[0] < 500) or not (0 <= self.snake.y[0] < 500):
            raise Exception("Snake hit the screen edge")

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(400,10))

    def show_game_over(self):
        self.surface.blit(self.background_img, (0, 0))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (100, 150))
        line2 = font.render("To play again press Enter.", True, (255, 255, 255))
        self.surface.blit(line2, (100,100))
        line3 = font.render("To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line3, (100,200))

        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)

if __name__ == '__main__':
    game = Game()
    game.run()