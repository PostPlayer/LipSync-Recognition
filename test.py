from pickle import FALSE, TRUE
from turtle import Screen, delay
from xml.dom.minidom import CharacterData
import pygame
import pyaudio
import wave
import numpy as np
from pynput import keyboard
from threading import Thread
import cv2
from matplotlib import pyplot as plt
from IPython import display 
import speech_recognition as sr
import time
from jamo import h2j, j2hcj
from trance import KoreanToRoman,arg_parse
import re
from Player import Playing
# 스크린 전체 크기 지정

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 480
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "test.wav"
NOISE_MININUM_VALUE = 250
FONT_NAME = 'arial'
# pygame 초기화

pygame.init()

def keyint():
    with keyboard.Listener(
        on_press=on_press,
    ) as listener:
        listener.join()



SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("음성인식 테스트")
# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 120

frames = []


BACKGROUND_COLOR = pygame.Color('White')

class AnimatedSprite(pygame.sprite.Sprite):


    def __init__(self, position,count):

        super(AnimatedSprite, self).__init__()
        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (600,400)
        #pygame.transform.scale(pygame.Surface,size,DestSurface = None)
 

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images1 = []
        images1.append(pygame.image.load('state/bunnyFace_Mute.png'))
        images1.append(pygame.image.load('state/bunnyFace_A.png'))
        images1.append(pygame.image.load('state/bunnyFace_E.png'))
        images1.append(pygame.image.load('state/bunnyFace_I.png'))
        images1.append(pygame.image.load('state/bunnyFace_O.png'))
        images1.append(pygame.image.load('state/bunnyFace_U.png'))
        images2 = []
        images2.append(pygame.image.load('state/catFace_Mute.png'))
        images2.append(pygame.image.load('state/catFace_A.png'))
        images2.append(pygame.image.load('state/catFace_E.png'))
        images2.append(pygame.image.load('state/catFace_I.png'))
        images2.append(pygame.image.load('state/catFace_O.png'))
        images2.append(pygame.image.load('state/catFace_U.png'))
        images3 = []
        images3.append(pygame.image.load('state/cowFace_Mute.png'))
        images3.append(pygame.image.load('state/cowFace_A.png'))
        images3.append(pygame.image.load('state/cowFace_E.png'))
        images3.append(pygame.image.load('state/cowFace_I.png'))
        images3.append(pygame.image.load('state/cowFace_O.png'))
        images3.append(pygame.image.load('state/cowFace_U.png'))
        images4 = []
        images4.append(pygame.image.load('state/mouseFace_Mute.png'))
        images4.append(pygame.image.load('state/mouseFace_A.png'))
        images4.append(pygame.image.load('state/mouseFace_E.png'))
        images4.append(pygame.image.load('state/mouseFace_I.png'))
        images4.append(pygame.image.load('state/mouseFace_O.png'))
        images4.append(pygame.image.load('state/mouseFace_U.png'))
        
        image_nomal = []
        
        if count == 1:
            image_nomal = images1
        if count == 2:    
            image_nomal = images2   
        if count == 3:   
            image_nomal = images3
        if count == 4:    
            image_nomal = images4     
        # rect 만들기
        self.rect = pygame.Rect(position, size)

        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        #self.images = [pygame.transform.scale(image, size) for image in images]
        self.image_nomal = [pygame.transform.scale(image, size) for image in image_nomal]
 

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = image_nomal[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.image_nomal * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0
        self.font_name = pygame.font.match_font(FONT_NAME)
        
                
        

    def update(self, mt, noise):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.
        
        # loop 시간 더하기
        self.current_time += mt
        
        
        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0
           
            if(noise=="ㅗ" or noise == "ㅛ"):
                self.index = 4
            elif(noise == "ㅏ"or noise == "ㅑ"):
                self.index = 1
            elif(noise == "ㅔ"or noise == "ㅐ"or noise == "ㅒ"):
                self.index = 2
            elif(noise == "ㅣ"or noise == "ㅡ"):
                self.index = 3
            elif(noise == "ㅜ"or noise == "ㅠ"):
                self.index = 5
            elif(noise == "ㅓ"or noise == "ㅕ"or noise == "ㅖ"):
                self.index = 4
            else:
               self.index = 0
            
            #if self.index >= len(self.image_nomal):
            #   self.index = 1

            self.image = self.image_nomal[self.index]
 
 
    def select(self):
        pygame.init()
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        set_count = 0
        player = []
        player.append(pygame.image.load("state/bunnyFace_Mute.png"))
        player.append(pygame.image.load("state/catFace_Mute.png"))
        player.append(pygame.image.load("state/cowFace_Mute.png"))
        player.append(pygame.image.load("state/mouseFace_Mute.png"))
        player[0] = pygame.transform.scale(player[0], (100, 100))
        player[1] = pygame.transform.scale(player[1],(100,100))
        player[2] = pygame.transform.scale(player[2],(100,100))
        player[3] = pygame.transform.scale(player[3],(100,100))
        
        player_Rect = player[0].get_rect()
        cat_Rect = player[1].get_rect()
        cow_Rect = player[2].get_rect()
        mouse_Rect = player[3].get_rect()
        
        player_Rect.centerx = 200
        player_Rect.centery = 200
        cat_Rect.centerx = 400
        cat_Rect.centery = 200
        
        cow_Rect.centerx = 600
        cow_Rect.centery = 200
        mouse_Rect.centerx = 800
        mouse_Rect.centery = 200
        
        MOVE = False
        
        
        
        playing = TRUE
        while playing:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_rel()         
                    mouse_pos = pygame.mouse.get_pos()

                    if mouse_pos[0] > player_Rect.left and mouse_pos[0] < player_Rect.right and mouse_pos[1] > player_Rect.top and mouse_pos[1] < player_Rect.bottom:
                        MOVE = True
                        set_count = 1
                        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        
                    if mouse_pos[0] > cat_Rect.left and mouse_pos[0] < cat_Rect.right and mouse_pos[1] > cat_Rect.top and mouse_pos[1] < cat_Rect.bottom:
                        MOVE = True
                        set_count = 2
                        pygame.mouse.set_cursor(*pygame.cursors.broken_x)    
                        
                    if mouse_pos[0] > cow_Rect.left and mouse_pos[0] < cow_Rect.right and mouse_pos[1] > cow_Rect.top and mouse_pos[1] < cow_Rect.bottom:
                        MOVE = True
                        set_count = 3
                        pygame.mouse.set_cursor(*pygame.cursors.broken_x) 
                    
                    if mouse_pos[0] > mouse_Rect.left and mouse_pos[0] < mouse_Rect.right and mouse_pos[1] > mouse_Rect.top and mouse_pos[1] < mouse_Rect.bottom:
                        MOVE = True
                        set_count = 4
                        pygame.mouse.set_cursor(*pygame.cursors.broken_x)       
                          
                if event.type == pygame.MOUSEBUTTONUP:
                    MOVE = False
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    
                if MOVE:
                    playing = False
                    return set_count
                
                SCREEN.fill((255,255,255))
                SCREEN.blit(player[0], player_Rect) 
                SCREEN.blit(player[1],cat_Rect)   
                SCREEN.blit(player[2],cow_Rect)
                SCREEN.blit(player[3],mouse_Rect)
                self.draw_text("Charater Seletion Page", 22,(0,0,0), 500, 400)
                pygame.display.flip()
                clock.tick(60)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        SCREEN.blit(text_surface, text_rect)
    

def main():
    
    #Rcoding()
    count = 1
    # player 생성
    player = AnimatedSprite(position=(100, 8),count=(count))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group(player)  
    
    count = player.select()
    
    Thread(target=keyint, daemon=False)
    
    player = AnimatedSprite(position=(100, 8),count=(count))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group(player)  
    #Playing()
    running = True
    while running:
# 스크린 객체 저장
        r = sr.Recognizer()
        mt = clock.tick(60) / 1000
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.
        #data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        
        #for i in vToText:
        # int(np.average(np.abs(data)))
        with sr.AudioFile('test.wav') as source:
            audio = r.record(source, duration=120)
        
        noise = r.recognize_google(audio_data=audio, language='ko-KR')
        hello = KoreanToRoman(unravel = False)
        output = []
        p = re.compile('[a-zA-Z]')
        output.clear()
        words = noise.split(' ')
        for word in words:
            output.append(hello.transcribe(word,separator= False,capital = False,transliterate = False))
       
        jamo_str = ''.join(output)
        
        print(jamo_str)
        for  i in jamo_str:
            time.sleep(0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            all_sprites.update(mt,i)
                # 배경색
            SCREEN.fill(BACKGROUND_COLOR)
                # 모든 sprite 화면에 그려주기
            all_sprites.draw(SCREEN)
            pygame.display.update()
    
        #jamo_str = j2hcj(h2j(noise))
        # all_sprites 그룹안에 든 모든 Sprite update
 

if __name__ == '__main__':
    main()