import pygame
from time import sleep

a = int(input('\033[1;34mDigite \033[35m1 \033[1;34mpara escutar Anne lister andando na velocidade da luz: '))
print('\033[1;35mPROCESSANDO...')
sleep(2)
if a == 1:
    print('\033[1;34m [Jaunty music]')
    pygame.mixer.init()
    pygame.mixer.music.load('ex022.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():pass
