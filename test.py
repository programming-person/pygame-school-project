import os, sys
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
clock = pygame.time.Clock()
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if is_blue:
                is_blue = False
            else:
                is_blue = True
    pressed = pygame.key.get_pressed();
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        x += 3
    if is_blue:
        colour = (0, 128, 255)
    else: colour = (255, 100, 0)
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, colour, (x, y), 30)
    pygame.display.update()
    clock.tick(60)
