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

    
소스코드 블록은 다음과 같이 작성할 수 있습니다.

```c
#include <stdio.h>

int main(void) {
  printf("Hello World!");
  return 0;
}
```
## Environment
실행환경에 대해 작성하면 된다. OS나 컴파일러 혹은 Hardware와 관련된 환경을 작성하면 된다. Multicore 환경에서 돌아가는 프로그램이라면 CPU나 RAM 같은 것들을 작성해도 좋다.

## Prerequisite
작성한 코드를 실행하기 전에 설치해야할 pakage나 의존성이 걸리는 문제들을 설명하면 된다.

## Usage
작성한 코드를 어떻게 실행해야 하는지에 대한 가이드라인이다. Usage Example을 함께 작성하면 좋다.

# Convention
Refer to the Google Style Guide.

## Files And DataStructure
중요한 코드 파일들 몇 개를 대상으로 해당 파일이 어떠한 역할을 하는 파일인지를 간단히 설명


링크는 다음과 같이 작성할 수 있습니다.

[작업 노션 주소](https://www.notion.so/80000coding/d9a17941d33849049d587d60e2675df7)

순서 없는 목록은 다음과 같이 작성할 수 있습니다.



인용 구문은 다음과 같이 작성할 수 있습니다.

> '공부합시다.' - 나동빈 - 
