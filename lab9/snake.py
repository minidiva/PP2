import pygame
import random
import sys

# инициализация
pygame.init()
pygame.mixer.init()

# окно параметры
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Demo")
clock = pygame.time.Clock()

# шрифт
font = pygame.font.Font(None, 30)

# базовыве цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# параметры змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15

# еда
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True
food_weight = random.randint(1,5) # UPD: фича с весом еды

# параметры игры
game_score = 0
level = 1
foods_eaten = 0
isRunning = True


# Fгенерация еды
def generate_food():
    while True:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_weight = random.randint(1,5) # UPD: параметр веса еды
        # чек не спавна на змейке
        if food_pos not in snake_body:
            return food_pos, food_weight

# цикл игры
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # управление
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # смена направления
    snake_direction = change_to

    # направление
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # вставка на новую позицию
    snake_body.insert(0, list(snake_pos))

    # чек если сьел еду
    if snake_pos == food_pos:
        food_spawn = False
        game_score += food_weight # UPD: обновлённый скор
        foods_eaten += 1
        # след лвл после 3 еды
        if foods_eaten >= 3:
            level += 1
            speed += 2  # увеличение скорости
            foods_eaten = 0  # обнулить количество еды после нового лвла
    else:
        snake_body.pop()

    # чек нужно ли заспавнить еду
    if not food_spawn:
        food_pos, food_weight = generate_food()
        food_spawn = True

    # коллизия с стенами
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    # коллизия с змейкой
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # апдейт окна
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # вывод скора
    game_score_text = font.render(f"Score: {game_score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(game_score_text, (20, 20))
    screen.blit(level_text, (20, 50))

    pygame.display.flip()
    clock.tick(speed)

# гейм овер скрин
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)  # 3 секунды после чего игра закрывается
pygame.quit()