import random

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura_tela = 600
largura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))



corpo = [[200, 200], [210, 200], [220, 200]]

grid = 10

direcaox = grid
direcaoy = 0

relogio = pygame.time.Clock()

macax = random.randint(0, 600) // grid * grid
macay = random.randint(0, 600) // grid * grid

font = pygame.font.Font('freesansbold.ttf', 40)
font2 = pygame.font.Font('freesansbold.ttf', 20)

text = font.render('GAME OVER', True, (0, 0, 0))
text2 = font2.render('press "R" for restart', True, (255, 255, 255))

while True:
    relogio.tick(15)
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0),(macax, macay, grid, grid))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

        if evento.type == KEYDOWN:
            if evento.key == K_a and direcaoy != 0:
                direcaox = -grid
                direcaoy = 0
            if evento.key == K_d and direcaoy != 0:
                direcaox = grid
                direcaoy = 0
            if evento.key == K_w and direcaox != 0:
                direcaox = 0
                direcaoy = -grid
            if evento.key == K_s and direcaox != 0:
                direcaox = 0
                direcaoy = grid

    if corpo[-1] in corpo[:-1] or corpo[-1][0] < 0 or corpo[-1][0] > largura_tela or corpo[-1][1] < 0 or corpo[-1][1] > altura_tela: #Colisão com o corpo
        gameover = True
        while gameover:

            pygame.draw.rect(tela, (255, 0, 0), (5, altura_tela//2-50, largura_tela-10, 100))
            tela.blit(text, (largura_tela//2-120, altura_tela//2-15, largura_tela-10, 100))
            tela.blit(text2, (largura_tela//2-90, altura_tela//2+25, largura_tela, 100))
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        corpo = [[200, 200], [210, 200], [220, 200]]
                        gameover = False

    if corpo[-1] == [macax, macay]:
        corpo.append([corpo[-1][0] + direcaox, corpo[-1][1] + direcaoy])
        macax = random.randint(0, 600) // grid * grid
        macay = random.randint(0, 600) // grid * grid
    for i in corpo:
        pygame.draw.rect(tela, (0, 255, 0), (i[0], i[1], grid, grid))
    corpo.pop(0)
    corpo.append([corpo[-1][0]+direcaox, corpo[-1][1]+direcaoy])



    pygame.display.update()

