import pygame
import random
import math


pygame.init()

size = (width, height) = (800, 600)

screen = pygame.display.set_mode(size)
bgImg = pygame.image.load("images/spacebg.jpg")


pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 500
playerX_change = 0

#enemy
def intializeEnemy():
    enemyX = random.randint(0,735)
    enemyY = random.randint(20,100)

enemyImg = pygame.image.load("images/enemy.png")
enemyX = random.randint(0,735)
enemyY = random.randint(20,100)
enemyX_change = 1.5
enemyY_change = 40



#bullet
bulletImg = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

def resetBullet():
    bulletY = 500
    bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def showScore(X,Y):
    score = font.render("Score: "+str(score_value), True, (255,255,255))
    screen.blit(score, (X, Y))

def player(X, Y):
    screen.blit(playerImg, (X, Y))

def enemy(X, Y):
    screen.blit(enemyImg, (X, Y))

def fire_bullet(X,Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (X+20, Y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if(distance < 33):
        return True
    return False

running = True
while(running):
    screen.fill((0, 0, 0))
    screen.blit(bgImg,(0,0))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                playerX_change -= 2
            if(event.key == pygame.K_RIGHT):
                playerX_change += 2
            if(event.key == pygame.K_SPACE and bullet_state is "ready"):
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0


    playerX += playerX_change
    if(playerX <= 0):
        playerX = 0
    elif(playerX >= 736):
        playerX = 736

    if(bulletY <= 0):
        bulletY = 500
        bullet_state = "ready"
        # resetBullet()

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    enemyX += enemyX_change
    if(enemyX <= 0):
        enemyX_change = 1.5
        enemyY += enemyY_change
    elif(enemyX >= 736):
        enemyX_change = -1.5
        enemyY += enemyY_change

    if(isCollision(enemyX,enemyY,bulletX, bulletY)):
        bulletY = 500
        bullet_state = "ready"
        # resetBullet()
        score_value += 1
        enemyX = random.randint(0,735)
        enemyY = random.randint(20,100)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    showScore(textX,textY)
    pygame.display.update()