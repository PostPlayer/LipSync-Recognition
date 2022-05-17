import pygame
import pyaudio
import wave
import numpy as np
from pynput import keyboard
from threading import Thread
import cv2
from matplotlib import pyplot as plt
from IPython import display 

# 스크린 전체 크기 지정

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 480
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"
NOISE_MININUM_VALUE = 250

 

# pygame 초기화

pygame.init()

def keyint():
    with keyboard.Listener(
        on_press=on_press,
    ) as listener:
        listener.join()


# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 120

frames = []

BACKGROUND_COLOR = pygame.Color('white')

 

class AnimatedSprite(pygame.sprite.Sprite):

 

    def __init__(self, position):

        super(AnimatedSprite, self).__init__()

 

        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (680, 472)

 

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []
        images.append(pygame.image.load('state/state_surprise.png'))
        
        image_nomal = []
        image_nomal.append(pygame.image.load('state/state_nomal.png'))
        image_nomal.append(pygame.image.load('state/state_surprise.png'))
        image_nomal.append(pygame.image.load('state/state_gloomy.png'))
        image_nomal.append(pygame.image.load('state/state_lough.png'))
        image_nomal.append(pygame.image.load('state/state_OH.png'))
        image_nomal.append(pygame.image.load('state/state_happy.png'))

        # rect 만들기
        self.rect = pygame.Rect(position, size)

        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]
        self.image_nomal = [pygame.transform.scale(image, size) for image in image_nomal]
 

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = image_nomal[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.image_nomal * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0

 

 

    def update(self, mt, noise):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.

        # loop 시간 더하기
        self.current_time += mt


        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0
           
            if(noise>250):
                self.index +=1
            if(noise<250):
               self.index = 0
            
            if self.index >= len(self.image_nomal):
                self.index = 1

            self.image = self.image_nomal[self.index]

 

 

def main():

    # player 생성
    player = AnimatedSprite(position=(100, 8))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group(player)  

 
    Thread(target=keyint, daemon=False)
    running = True
    while running:
        mt = clock.tick(60) / 1000
        
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        noise = int(np.average(np.abs(data)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        all_sprites.update(mt,noise)
                # 배경색
        SCREEN.fill(BACKGROUND_COLOR)
                # 모든 sprite 화면에 그려주기
        all_sprites.draw(SCREEN)
        pygame.display.update()
 

        # all_sprites 그룹안에 든 모든 Sprite update
 

if __name__ == '__main__':
    main()