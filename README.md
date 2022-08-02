# LipSync-Recognition

YU Graduate Project [suhshin, PostPlayer, emptyhead, @홍서경]

| suhshin                             | PostPlayer                               | emptyhead                                |
| -------------------------------- | ------------------------------------ | -------------------------------------- |
| @rkskekzzz                           | @INSU                             | @hyung6370                             |
| ![suhshinprofile](./asset/suhshin.png) | ![postplayerprofile](./asset/postplayer.jpeg) | ![emptyheadprofile](./asset/emptyhead.jpeg) |


# Introduction
### ___YU Graduate Project___
Realtime lipsync API that utilizes E2E speech recognition engine. This repository is application part.


## Description 

이 프로젝트는 딥러닝으로 학습된 모델을 통해 실제 사용자가 말하는 음성을 실시간으로 받아들여, 사용자의 캐릭터가 사람이 직접 앞에서 말하는 듯한 효과를  줄 수 있는 서비스이다. 이 프로젝트는 다양한 서비스에서 모두 사용할 수 있는 API로 제작 될 것이다.

# Engine Function
### TTI (Text To Image)
* 문자 입력을 받아서 립싱크 이미지를 출력한다
### STI (Speech To Image)
* 말하는 음성을 실시간으로 립싱크 이미지를 출력한다
### Two-way & Realtime Communication
* 실시간으로 양방향으로 소통이 가능하다
* 서로의 캐릭터의 입모양이 움직이는 것이 보인다
### STT (Speech To Text)
* 음성 입력을 받아서 텍스트로 출력한다
### RNN-T Korean
* 한국어로 번역해주는 기능 

