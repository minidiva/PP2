import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False
clock = pygame.time.Clock()

clockImage = pygame.image.load("clock.png")
hourArm = pygame.image.load("rightarm.png")
minuteArm = pygame.image.load("leftarm.png")


clock_rect = clockImage.get_rect(center=(500, 500))
hour_rect = hourArm.get_rect(center=(500, 500))
minute_rect = minuteArm.get_rect(center=(500, 500))

def rotate_image(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, new_rect

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min + current_time.tm_sec / 60

    hour_angle = -((hours + minutes / 60) * 30)
    minute_angle = -(minutes * 6)

    rotated_hour, hour_pos = rotate_image(hourArm, hour_angle, (500, 500))
    rotated_minute, minute_pos = rotate_image(minuteArm, minute_angle, (500, 500))

    screen.fill((255, 255, 255))
    screen.blit(clockImage, clock_rect)
    screen.blit(rotated_hour, hour_pos)
    screen.blit(rotated_minute, minute_pos)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()