"""import subprocess
import pygame

def start_pong():
    subprocess.run(['python', 'pong.py'])

def start_snake():
    subprocess.run(['python', 'snake.py'])
def start_spaceinvaders():
    subprocess.run(['python','space_game.py'])

def run_game(choice):
    if choice == 'p':
        start_pong()
    elif choice == 's':
        start_snake()
    elif choice == 'd':
        start_spaceinvaders()

if __name__ == '__main__':
    pygame.init()
   

    print("Choose the game to play:")
    print("Enter 'p' for Pong or 's' for Snake or 'd' for spaceinvaders.")
    choice = input("Your choice:")

    if choice.lower() in ['p', 's','d',]:
        run_game(choice.lower())
    else:
        print("Invalid choice. Please enter 'p' for Pong or 's' for Snake.")
        pygame.quit()

    pygame.quit()"""
import subprocess
import pygame

def start_pong():
    subprocess.run(['python', 'pong.py'])

def start_snake():
    subprocess.run(['python', 'snake.py'])

def start_spaceinvaders():
    subprocess.run(['python', 'space_game.py'])

def draw_menu(screen):
    font = pygame.font.Font(None, 36)
    menu_options = {
        'p': 'Pong',
        's': 'Snake',
        'd': 'Space Invaders',
        'q': 'Quit',
    }

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return
                elif event.unicode in menu_options:
                    return menu_options[event.unicode]

        for key, text in menu_options.items():
            text_surface = font.render(f"Press '{key}' to play {text}", True, (255, 255, 255))
            screen.blit(text_surface, (50, 50 * (ord(key) - ord('a') + 1)))

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Game Menu")

    print("Choose the game to play:")
    print("Enter 'p' for Pong or 's' for Snake or 'd' for Space Invaders.")
    choice = draw_menu(screen)

    if choice.lower() in ['p', 's', 'd']:
        if choice == 'p':
            start_pong()
        elif choice == 's':
            start_snake()
        elif choice == 'd':
            start_spaceinvaders()
    else:
        print("Invalid choice. Please enter 'p' for Pong or 's' for Snake.")
        pygame.quit()

