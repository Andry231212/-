# импорт библиотек
import pygame
import time
import random

pygame.mixer.init()
fire_sound = pygame.mixer.Sound('5-gta-wasted.ogg')
fire_so = pygame.mixer.Sound('am_njam_-_njam_njam_njam___z2-_mp3cut.net_.ogg')
pygame.mixer.music.load('pixel-perfect-112527.ogg')
pygame.mixer.music.play()


snake_speed = 15
# размер окна 
window_x = 720
window_y = 480
background = pygame.transform.scale(pygame.image.load('dbg8qqd-0fb0aced-d05c-4df6-a7c6-b8e04c184ac5.png'),(window_x,window_y)) 
 
# добавляем цвета 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
#  Инициализация pygame
pygame.init()
 
# Инициализировать игрового окно
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))
 
# Контроллер FPS
fps = pygame.time.Clock()

# положения змеи по умолчанию
snake_position = [100, 50]
 
# определение первых 4 блоков змейки
# тело 
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
# местоположение еды 
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
 
# установка направления змеи по умолчанию
# в право
direction = 'RIGHT'
change_to = direction

# балы начально
score = 0
 
# отображение функции Score
def show_score(choice, color, font, size):
   
    # ввод шрифта 
    score_font = pygame.font.SysFont(font, size)
     
    # создаем объект поверхности дисплея
    # оценка_поверхности
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # создать прямоугольный объект
    # текстовый объект поверхности
    score_rect = score_surface.get_rect()
     
    #отображение текста
    game_window.blit(score_surface, score_rect)

# проигрыш 
def game_over():
   
    # создание объекта шрифта my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # создание текстовой поверхности, на которой текст
    game_over_surface = my_font.render('Твой результат: ' + str(score), True, black)
     
    # создаем прямоугольный объект для текста
    game_over_rect = game_over_surface.get_rect()
     
    # установка положения текста
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # пишем текст 
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # через 2 секунды мы выйдем из
    time.sleep(2)
     
    pygame.quit()
     
    # выход из программы 
    quit()

# Основная функция
while True:
    # обработка ключевых событий
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # Если одновременно нажать две клавиши
    # мы не хотим, чтобы змея двигалась в двух направлениях
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Перемещение змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Механизм роста тела змеи
    # если фрукты и змеи столкнутся, то очки будут
    # увеличивается на 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fire_so.play()
        score += 10
        snake_speed += 0.7
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.blit(background, (0,0))
     
    for pos in snake_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))
 
    # Условия окончания игры
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        fire_sound.play()
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        fire_sound.play()
        game_over()
     
    # Прикосновение к телу змеи
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            fire_sound.play()
            game_over()
     
    # отображение счета непрерывно
    show_score(1, white, 'times new roman', 20)
     
    # Обновить игровой экран
    
    pygame.display.update()
    
 
    # Кадров в секунду
    fps.tick(snake_speed)