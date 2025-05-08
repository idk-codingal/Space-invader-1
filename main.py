# Importing everything and initializing it
import math
import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 15
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Captions and icons and background
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('caption-removebg-preview.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Background.jpg')
 
# Creating players
playerImg = pygame.image.load('invader.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
PLAYERX_change = 0

# Creating enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Loop for enemies
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy-removebg-preview.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Making bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Defining everything
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], x, y)
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            running = False
        
        # Defining keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX == playerX
                fire_bullet(bulletX, bulletY) 

        if event.type == pygame.KEY_UP and event.key in[pygame.K_left, pygame.K_RIGHT]:
                playerX_change = 0
            
    # Player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    # Enemy movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change [i] *= -1 
            enemyY [i] += enemyY_change[i]

        # Checking collisions
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)

        # Bullet movement
        if bulletY <= 0:
           bulletY = PLAYER_START_Y
           bullet_state = "ready"
        elif bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
