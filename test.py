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
from player import Playing
from client_single import socket_response
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


    def __init__(self,count):

        super(AnimatedSprite, self).__init__()
        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (100,100) 
        #캐릭터 사이즈
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
        images5 = []
        images5.append(pygame.image.load('state/logout.png'))
        speech = []
        speech.append(pygame.image.load('state/text.png'))
        text = []
        text.append(pygame.image.load('state/headphones.png'))
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
        self.exit_rect = pygame.Rect((100,100),size)
        self.rab_rect = pygame.Rect((200,200),size)
        self.cat_rect = pygame.Rect((400,200),size)
        self.cow_rect = pygame.Rect((600,200),size)
        self.rat_rect = pygame.Rect((800,200),size)
        self.speech_rect = pygame.Rect((200,100),size)
        self.text_rect = pygame.Rect((300,100),size)
        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.image_nomal = [pygame.transform.scale(image, size) for image in image_nomal]
        self.images1 = [pygame.transform.scale(image1, size) for image1 in images1]
        self.images2 =[pygame.transform.scale(image2,size) for image2 in images2]
        self.images3 =[pygame.transform.scale(image3,size) for image3 in images3]
        self.images4 =[pygame.transform.scale(image4,size) for image4 in images4]
        self.images5 = [pygame.transform.scale(image5,size) for image5 in images5]
        self.speech = [pygame.transform.scale(speech1,size) for speech1 in speech]
        self.text =[pygame.transform.scale(text1,size) for text1 in text]
        # 캐릭터의 첫번째 이미지
        self.index1 = 0
        self.index2 = 0
        self.index3 = 0
        self.index4 = 0
        #배열지정
        self.image1 = images1[self.index1]
        self.image2 = images2[self.index2]
        self.image3 = images3[self.index3]
        self.image4 = images4[self.index4]
        self.image5 = images5[0]
        self.speech_set = speech[0]
        self.text_set = text[0]
        
        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.image_nomal * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0
        self.font_name = pygame.font.match_font(FONT_NAME)
        
                
        
    def draw(self):
        SCREEN.fill((255,255,255))
        SCREEN.blit(self.image1, self.rab_rect) 
        SCREEN.blit(self.image2,self.cat_rect)
        SCREEN.blit(self.image3,self.cow_rect)
        SCREEN.blit(self.image4,self.rat_rect)
        SCREEN.blit(self.image5, self.exit_rect)
        SCREEN.blit(self.speech_set,self.speech_rect)
        SCREEN.blit(self.text_set,self.text_rect)
        pygame.display.flip()                           
                
                      
    def update(self, mt, noise,count):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.
        
        # loop 시간 더하기
        self.current_time += mt
        
        
        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0
           
            if(noise=="ㅗ" or noise == "ㅛ"):
                if(count == 1):
                    self.index1 = 4
                if(count == 2):
                    self.index2 = 4
                if(count == 3):
                    self.index3 = 4
                if(count == 4):
                    self.index4 = 4
                    
            elif(noise == "ㅏ"or noise == "ㅑ"):
                if(count == 1):
                    self.index1 = 1
                if(count == 2):
                    self.index2 = 1
                if(count == 3):
                    self.index3 = 1
                if(count == 4):
                    self.index4 = 1

            elif(noise == "ㅔ"or noise == "ㅐ"or noise == "ㅒ"):
                if(count == 1):
                    self.index1 = 2
                if(count == 2):
                    self.index2 = 2
                if(count == 3):
                    self.index3 = 2
                if(count == 4):
                    self.index4 = 2
                    
            elif(noise == "ㅣ"or noise == "ㅡ"):
                if(count == 1):
                    self.index1 = 3
                if(count == 2):
                    self.index2 = 3
                if(count == 3):
                    self.index3 = 3
                if(count == 4):
                    self.index4 = 3

            elif(noise == "ㅜ"or noise == "ㅠ"):
                if(count == 1):
                    self.index1 = 5
                if(count == 2):
                    self.index2 = 5
                if(count == 3):
                    self.index3 = 5
                if(count == 4):
                    self.index4 = 5

            elif(noise == "ㅓ"or noise == "ㅕ"or noise == "ㅖ"):
                if(count == 1):
                    self.index1 = 4
                if(count == 2):
                    self.index2 = 4
                if(count == 3):
                    self.index3 = 4
                if(count == 4):
                    self.index4 = 4

            else:
                if(count == 1):
                    self.index1 = 0
                if(count == 2):
                    self.index2 = 0
                if(count == 3):
                    self.index3 = 0
                if(count == 4):
                    self.index4 = 0
            
            #if self.index >= len(self.image_nomal):
            #   self.index = 1
            self.image1 = self.images1[self.index1]
            self.image2 = self.images2[self.index2]
            self.image3 = self.images3[self.index3]
            self.image4 = self.images4[self.index4]
 
 
    def select(self):
        pygame.init()
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        set_count = 0
        player = []
        player.append(pygame.image.load("state/bunnyFace_Mute.png"))
        player.append(pygame.image.load("state/catFace_Mute.png"))
        player.append(pygame.image.load("state/cowFace_Mute.png"))
        player.append(pygame.image.load("state/mouseFace_Mute.png"))
        player.append(pygame.image.load("state/logout.png"))
        player[0] = pygame.transform.scale(player[0], (100, 100))
        player[1] = pygame.transform.scale(player[1],(100,100))
        player[2] = pygame.transform.scale(player[2],(100,100))
        player[3] = pygame.transform.scale(player[3],(100,100))
        player[4] = pygame.transform.scale(player[4],(50,50))
        
        player_Rect = player[0].get_rect()
        cat_Rect = player[1].get_rect()
        cow_Rect = player[2].get_rect()
        mouse_Rect = player[3].get_rect()
        end_Rect = player[4].get_rect()
        
        player_Rect.centerx = 200
        player_Rect.centery = 200
        cat_Rect.centerx = 400
        cat_Rect.centery = 200
        
        cow_Rect.centerx = 600
        cow_Rect.centery = 200
        mouse_Rect.centerx = 800
        mouse_Rect.centery = 200
        
        end_Rect.centerx = 100
        end_Rect.centery = 100
        
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
                               
                    if mouse_pos[0] >end_Rect.left and mouse_pos[0] < end_Rect.right and mouse_pos[1] > end_Rect.top and mouse_pos[1] < end_Rect.bottom:
                        MOVE = True
                        set_count = 5
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
                SCREEN.blit(player[4],end_Rect)
                self.draw_text("Charater Seletion Page", 22,(0,0,0), 500, 400)
                pygame.display.flip()
                clock.tick(60)

    def draw_text(self, text, size, color, x, y):\
        
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        SCREEN.blit(text_surface, text_rect)
        
    

def main():

    speech_count = 1
    text_count = 0
    
    testing = True
    while testing:
        pygame.init()
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("음성인식 테스트")
        # FPS를 위한 Clock 생성
        clock = pygame.time.Clock()
        #Rcoding()
        count = 1
        # player 생성
        player = AnimatedSprite(count=(count))
        # 생성된 player를 그룹에 넣기
        #all_sprites = pygame.sprite.Group(player)  
        count = player.select()
    
        Thread(target=keyint, daemon=False)
        
        if count == 5:
            break
        
        player = AnimatedSprite(count=(count))
        setcount = 0
        sentence = '으'
        playing_count =0
        
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
            
            words = sentence.split(' ')
            words2 = noise.split(' ')
            
            if speech_count == 1 and text_count == 0:
                for word in words2:
                    output.append(hello.transcribe(word,separator= False,capital = False,transliterate = False))
            
            elif speech_count == 0 and text_count == 1:    
                for word in words:
                    output.append(hello.transcribe(word,separator= False,capital = False,transliterate = False))
       
            jamo_str = ''.join(output)
            print(jamo_str);
            for  i in jamo_str:
                time.sleep(0.1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                   
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mouse.get_rel()         
                        mouse_pos = pygame.mouse.get_pos()
                
                        if mouse_pos[0] > pygame.Rect((100,100),(100,100)).left and mouse_pos[0] < pygame.Rect((100,100),(100,100)).right and mouse_pos[1] > pygame.Rect((100,100),(100,100)).top and mouse_pos[1] < pygame.Rect((100,100),(100,100)).bottom:
                            setcount = 1
                            pygame.mouse.set_cursor(*pygame.cursors.broken_x)   
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mouse.get_rel()         
                        mouse_pos = pygame.mouse.get_pos()
                
                        if mouse_pos[0] > pygame.Rect((200,100),(100,100)).left and mouse_pos[0] < pygame.Rect((200,100),(100,100)).right and mouse_pos[1] > pygame.Rect((200,100),(100,100)).top and mouse_pos[1] < pygame.Rect((200,100),(100,100)).bottom:
                            speech_count = 0
                            text_count = 1
                            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                            sentence = input()
                            socket_response(sentence)   
                                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mouse.get_rel()         
                        mouse_pos = pygame.mouse.get_pos()
                
                        if mouse_pos[0] > pygame.Rect((300,100),(100,100)).left and mouse_pos[0] < pygame.Rect((300,100),(100,100)).right and mouse_pos[1] > pygame.Rect((300,100),(100,100)).top and mouse_pos[1] < pygame.Rect((300,100),(100,100)).bottom:
                            speech_count = 1
                            text_count = 0
                            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                            
                    if event.type == pygame.MOUSEBUTTONUP:
                        setcount = 0
                        pygame.mouse.set_cursor(*pygame.cursors.arrow)
 
                    if setcount == 1:
                        running = False    
            
                player.update(mt,i,count)
                setcount = player.draw() 
                
         
            
        
 

if __name__ == '__main__':
    main()