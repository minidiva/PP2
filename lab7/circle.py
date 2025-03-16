import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_y = y - 20
                if new_y >= 25:
                    y = new_y
            elif event.key == pygame.K_DOWN:
                new_y = y + 20
                if new_y <= 275:
                    y = new_y
            elif event.key == pygame.K_LEFT:
                new_x = x - 20
                if new_x >= 25:
                    x = new_x
            elif event.key == pygame.K_RIGHT:
                new_x = x + 20
                if new_x <= 375:
                    x = new_x
    
    screen.fill((255, 255, 255))
    color = (255, 0, 0)
    pygame.draw.circle(screen, color, (x, y), 25)
    
    pygame.display.flip()
    clock.tick(60)