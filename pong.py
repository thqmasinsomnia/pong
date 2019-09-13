# http://www.youtube.com/watch?v=bt8edFhIudQ
# https://www.youtube.com/watch?v=W1B_poM9l7M
# https://www.youtube.com/watch?v=br3OzOrARh4
# https://www.youtube.com/watch?v=wIamg9wSdMg
# https://www.youtube.com/watch?v=EXzoh6uJO1w

import pygame
import random
import sys
from pygame.locals import *

HEIGHT = 500
WIDTH = 700
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)



class scoreboard():
    def updatescore(self, compwins, playerwins, compsets, playersets):
        font = pygame.font.Font(None, 74)
        text = font.render(str(compwins), 1, WHITE)
        gameDisplay.blit(text, (250, 10))
        text = font.render(str(compsets), 1, WHITE)
        gameDisplay.blit(text, (250, 50))
        text = font.render(str(playerwins), 1, WHITE)
        gameDisplay.blit(text, (420, 10))
        text = font.render(str(playersets), 1, WHITE)
        gameDisplay.blit(text, (420, 50))


class Ypaddle(pygame.sprite.Sprite):

    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)

        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    def moveup(self, pix):
        self.rect.y -= pix
        if self.rect.y < 0:
            self.rect.y = 0

    def movedown(self, pix):
        self.rect.y += pix
        # Check that you are not going too far (off the screen)
        if self.rect.y > 400:
            self.rect.y = 400


class Xpaddle(pygame.sprite.Sprite):

    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)

        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    def moveleft(self, pix):
        self.rect.x -= pix
        if self.rect.x < 350:
            self.rect.x = 350

    def moveright(self, pix):
        self.rect.x += pix
        # Check that you are not going too far (off the screen)
        if self.rect.x > 600:
            self.rect.x = 600


class compXpaddle(pygame.sprite.Sprite):

    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)

        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    def moveleft(self, pix):
        self.rect.x -= pix
        if self.rect.x < 0:
            self.rect.x = 0

    def moveright(self, pix):
        self.rect.x += pix
        # Check that you are not going too far (off the screen)
        if self.rect.x > 250:
            self.rect.x = 250


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, w):
        super().__init__()
        self.color = color
        self.width = w

        self.image = pygame.Surface([w, w])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, color, [0, 0, w, w])
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        collision = pygame.sprite.spritecollideany(ball, spritelist)
        if collision:
            if collision == playery:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
                pygame.mixer.music.load('bloop.ogg')
                pygame.mixer.music.play(0)
            if collision == playerx:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('bloop.ogg')
                pygame.mixer.music.play(0)
            if collision == playerx2:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('bloop.ogg')
                pygame.mixer.music.play(0)
            if collision == compy:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
                pygame.mixer.music.load('bloop.ogg')
                pygame.mixer.music.play(0)
            if collision == compx:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('bloop.ogg')
                pygame.mixer.music.play(0)
            if collision == compx2:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('bloop.ogg')
                pygame.mixer.music.play(0)


pygame.init()

imgy = pygame.image.load("woody.png")
imgx = pygame.image.load("woodx.png")
imgey = pygame.image.load("enemywoody.png")
imgex = pygame.image.load("enemywoodx.png")

imgball = pygame.image.load("ball2.png")

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('3 PADDLE PONG')

playery = Ypaddle(BLACK, 10, 100)
playerx = Xpaddle(BLACK, 100, 10)
playerx2 = Xpaddle(BLACK, 100, 10)

playerx.rect.x = 600
playerx.rect.y = 10

playerx2.rect.x = 600
playerx2.rect.y = 480

playery.rect.x = 680
playery.rect.y = 200

compy = Ypaddle(BLACK, 10, 100)
compy.rect.x = 10
compy.rect.y = 200

compx = compXpaddle(BLACK, 100, 10)
compx.rect.x = 20
compx.rect.y = 10

compx2 = compXpaddle(BLACK, 100, 10)
compx2.rect.x = 20
compx2.rect.y = 480

ball = Ball(BLACK, 20)
ball.rect.x = 345
ball.rect.y = 195

playery.image = imgy
compy.image = imgey
playerx.image = imgx
playerx2.image = imgx
compx.image = imgex
compx2.image = imgex
ball.image = imgball



spritelist = pygame.sprite.Group()
spritelist.add(playery)
spritelist.add(playerx)
spritelist.add(playerx2)
spritelist.add(compy)
spritelist.add(compx)
spritelist.add(compx2)
spritelist.add(ball)

playerwins = 0
compwins = 0
playersets = 0
compsets = 0

score = scoreboard()
clock = pygame.time.Clock()

foo = 0
fum = 0


while True:
    keys = pygame.key.get_pressed()
    # check for the quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    if keys[pygame.K_UP]:
        playery.moveup(5)
    if keys[pygame.K_DOWN]:
        playery.movedown(5)
    if keys[pygame.K_RIGHT]:
        playerx.moveright(5)
        playerx2.moveright(5)
    if keys[pygame.K_LEFT]:
        playerx.moveleft(5)
        playerx2.moveleft(5)



    if compy.rect.y < ball.rect.y:
        compy.movedown(5)
    if compy.rect.y > ball.rect.y:
        compy.moveup(5)
    if compx.rect.x < ball.rect.x or compx2.rect.x < ball.rect.x and x < 350:
        compx.moveright(5)
        compx2.moveright(5)
    if (compx.rect.x > ball.rect.x or compx2.rect.x > ball.rect.x) and x < 350:
        compx.moveleft(5)
        compx2.moveleft(5)

    if ball.velocity[0] < 0 and ball.velocity[1] > 0:
        compx.moveright(5)
        compx2.moveright(5)
    if ball.velocity[0] < 0 and ball.velocity[1] < 0:
        compx.moveleft(5)
        compx2.moveleft(5)

    spritelist.update()
    gameDisplay.fill(GREEN)

    pygame.draw.line(gameDisplay, BLACK, [349, 0], [349, 500], 5)
    x = 0
    while x < 1000:
        pygame.draw.line(gameDisplay, GREEN, [0, x], [500, x], 20)
        x = x + 50

    if ball.rect.x >= 690:
        compwins += 1
        pygame.mixer.music.load('comppoint.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(4, 8)
        ball.velocity[1] = random.randint(-8, 8)
    if ball.rect.x > 350 and (ball.rect.y < 10 or ball.rect.y > 490):
        compwins += 1
        pygame.mixer.music.load('comppoint.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(4, 8)
        ball.velocity[1] = random.randint(-8, 8)
    if ball.rect.x <= 0:
        playerwins += 1
        pygame.mixer.music.load('playerpoint.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(-8, -4)
        ball.velocity[1] = random.randint(-8, 8)
    if ball.rect.x < 350 and (ball.rect.y < 10 or ball.rect.y > 490):
        playerwins += 1
        pygame.mixer.music.load('playerpoint.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(-8, -4)
        ball.velocity[1] = random.randint(-8, 8)

    if compwins >= 11 and compwins > playerwins + 2:
        compwins = 0
        playerwins = 0
        compsets += 1
    if playerwins >= 11 and playerwins > compwins + 2:
        compwins = 0
        playerwins = 0
        playersets += 1

    font = pygame.font.Font(None, 50)
    text = font.render(str(compwins), 1, WHITE)

    if playersets == 3:
        if foo == 0:
            pygame.mixer.music.load('victory.ogg')
            pygame.mixer.music.play(0)
            foo = 1
        ball.velocity[0] = 0
        ball.velocity[1] = 0
        text = font.render(str('PLAYER WINS PLAY AGAIN? y/n'), 1, WHITE)
        gameDisplay.blit(text, (0, 250))
        if keys[pygame.K_n]:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if keys[pygame.K_y]:
            ball.velocity[0] = random.randint(4, 8)
            ball.velocity[1] = random.randint(-8, 8)
            pygame.mixer.music.stop()
            compsets = 0
            compwins = 0
            playerwins = 0
            playersets = 0
            foo = 0

    if compsets == 3:
        if foo == 0:
            pygame.mixer.music.load('loser.ogg')
            pygame.mixer.music.play(0)
            foo = 1
        ball.velocity[0] = 0
        ball.velocity[1] = 0
        text = font.render(str('COMPUTER WINS PLAY AGAIN? y/n'), 1, WHITE)
        gameDisplay.blit(text, (0, 250))
        if keys[pygame.K_n]:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if keys[pygame.K_y]:
            pygame.mixer.music.stop()
            ball.velocity[0] = random.randint(4, 8)
            ball.velocity[1] = random.randint(-8, 8)
            compsets = 0
            compwins = 0
            playerwins = 0
            playersets = 0
            foo = 0

    score.updatescore(compwins, playerwins, compsets, playersets)
    spritelist.draw(gameDisplay)
    pygame.display.flip()
    clock.tick(60)
