import pygame
import sys

# käynnistetään pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

pallo_x = 300
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 222, 179))
    pygame.draw.rect(screen, (233, 133, 133), (pygame.mouse.get_pos(), (100, 100)))
    pygame.draw.circle(screen, (133, 233, 133), (pallo_x, 200), 40)
    pallo_x += 10
    if pallo_x > 600:
        pallo_x = 0

    # päivitetään muutokset näytölle
    pygame.display.update()

# lopetetaan pygame
pygame.quit()