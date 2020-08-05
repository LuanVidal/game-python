import pygame
from random import randint
from pygame import mixer
mixer.init()
pygame.init()
mixer.music.load('ex0000.mp3')
mixer.music.play()
x = 350
y = 120
pos_x = 200
pos_y = 800
pos_y_a = 800
pos_y_c = 800
timer = 0
tempo_segundo = 0

velocidade = 15
velocidade_outros = 20

fundo = pygame.image.load('imagem.png')
corrida = pygame.image.load('carroV.png')
policia = pygame.image.load('carroA.png')
cinza = pygame.image.load('carroZ.png')
carroP = pygame.image.load('carro1.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render('Tempo: ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela = pygame.display.set_mode((800,585))
pygame.display.set_caption('formula 5')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x<= 520:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 160:
        x -= velocidade

    if(x + 90 > pos_x and y + 190 > pos_y):
        y = 1200

    if (pos_y <=  - 80) :
        pos_y = randint(800, 1000)
    if  ( pos_y_a < -180) :
        pos_y_a = randint(1300, 2000)
    if   (pos_y_c < -180):
        pos_y_c = randint(2200, 2500)


    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render('Tempo: '+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0


    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_c -= velocidade_outros + 5  # carro preto



    janela.blit(fundo, (0,0))
    janela.blit(corrida, (x - 2, y))
    janela.blit(policia, (pos_x + 10, pos_y  ))
    janela.blit(cinza, (pos_x + 150, pos_y_a ))
    janela.blit(carroP, (pos_x + 285, pos_y_c ))
    janela.blit(texto, pos_texto)
    pygame.display.update()
pygame.quit()