#Abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.mixer.init() #inicia
pygame.mixer.music.load('exer021.mp3') #carrega a music
pygame.mixer.music.play() #toca a musica

input('Agora é só relaxar')