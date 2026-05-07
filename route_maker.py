import pygame
pygame.init()

screen = pygame.display.set_mode((900, 900), pygame.RESIZABLE)
pygame.display.set_caption("Route Maker")
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.WINDOWRESIZED:
            screen = pygame.display.set_mode((event.x, event.y), pygame.RESIZABLE)

    screen.fill((0, 0, 0))
    # redraw your content here

    pygame.display.flip()
    clock.tick(60)
    