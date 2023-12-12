import pygame

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

WIDTH = HEIGHT = 512  # width and height of the chess board


def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    original_background = pygame.image.load("Assets/board.png")
    background = pygame.transform.scale(original_background, (WIDTH, HEIGHT))

    run = True
    while run:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        pygame.display.update()


def main():
    try:
        pygame.init()
        run_game()

    finally:
        pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
