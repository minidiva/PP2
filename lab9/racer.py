import pygame
import sys
import random


pygame.init()
pygame.mixer.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


try:
    car_img = pygame.image.load("car.png").convert_alpha()
    coin_img = pygame.image.load("coin.png").convert_alpha()
    obstacle_img = pygame.image.load("obstacle.png").convert_alpha()
    background_img = pygame.image.load("background.png").convert()
except FileNotFoundError as e:
    print(f"Error loading image: {e}")
    sys.exit()


car_img = pygame.transform.scale(car_img, (50, 80))
coin_img = pygame.transform.scale(coin_img, (30, 30))
obstacle_img = pygame.transform.scale(obstacle_img, (60, 60))
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))


player_width = 50
player_height = 80
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 20
player_speed = 8


coin_width = 30
coin_height = 30
coin_speed = 5
coin_spawn_delay = 2000  
last_coin_spawn = pygame.time.get_ticks()
coin_amount = 0


obstacle_width = 60
obstacle_height = 60
obstacle_speed = 4
obstacle_spawn_delay = 1500 
last_obstacle_spawn = pygame.time.get_ticks()


bg_y1 = 0
bg_y2 = -screen_height
bg_speed = 3


score = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


try:
    coin_sound = pygame.mixer.Sound("coin.wav")
except FileNotFoundError:
    coin_sound = pygame.mixer.Sound(pygame.mixer.Sound(buffer=bytes(1))) 

coins = []
obstacles = []

def spawn_coin():
    return {
        "rect": pygame.Rect(
            random.randint(0, screen_width - coin_width),
            -coin_height,
            coin_width,
            coin_height
        ),
        "active": True
    }

def spawn_obstacle():
    return {
        "rect": pygame.Rect(
            random.randint(0, screen_width - obstacle_width),
            -obstacle_height,
            obstacle_width,
            obstacle_height
        ),
        "active": True
    }

def show_game_over():
    screen.fill(BLACK)
    text = font.render("GAME OVER! Final Score: " + str(score), True, WHITE)
    screen.blit(text, (screen_width//2 - 150, screen_height//2 - 20))
    pygame.display.flip()
    pygame.time.wait(3000)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    current_time = pygame.time.get_ticks()
    if current_time - last_coin_spawn > coin_spawn_delay:
        coins.append(spawn_coin())
        last_coin_spawn = current_time

    if current_time - last_obstacle_spawn > obstacle_spawn_delay:
        obstacles.append(spawn_obstacle())
        last_obstacle_spawn = current_time

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    for coin in coins[:]:
        coin["rect"].y += coin_speed
        if coin["rect"].y > screen_height:
            coins.remove(coin)
        elif coin["active"] and player_rect.colliderect(coin["rect"]):
            add_score = random.randint(1,10) # UPD: Random Weights for coins 1-10
            score += add_score
            coin_amount += 1
            coin_sound.play()
            coin["active"] = False
            coins.remove(coin)
        if coin_amount == 4: # UPD: If player have collected 4 coins despite of weigth, then he is a pro and has to be eliminated ASAP
            obstacle_speed = 8

    for obstacle in obstacles[:]:
        obstacle["rect"].y += obstacle_speed
        if obstacle["rect"].y > screen_height:
            obstacles.remove(obstacle)
        elif obstacle["active"] and player_rect.colliderect(obstacle["rect"]):
            show_game_over()
            running = False

    bg_y1 += bg_speed
    bg_y2 += bg_speed
    if bg_y1 > screen_height:
        bg_y1 = -screen_height
    if bg_y2 > screen_height:
        bg_y2 = -screen_height


    screen.blit(background_img, (0, bg_y1))
    screen.blit(background_img, (0, bg_y2))
    

    screen.blit(car_img, (player_x, player_y))
    

    for coin in coins:
        screen.blit(coin_img, coin["rect"].topleft)
    

    for obstacle in obstacles:
        screen.blit(obstacle_img, obstacle["rect"].topleft)
    

    score_text = font.render(f"Speed: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()