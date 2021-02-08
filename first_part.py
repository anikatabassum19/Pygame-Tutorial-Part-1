import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

game_window = pygame.display.set_mode((500,700))
pygame.display.set_caption("Snake Game With Orchi")

game_window.fill(blue)

pygame.display.update()

Exit = False

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True

pygame.quit()
quit()

    










