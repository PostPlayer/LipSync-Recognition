import argparse
import re
import eng_to_ipa
from numpy import character 

class KoreanToRoman(object):


    def __init__(self, **ksargs):

        self.options = {
            'unravel': False,
            'separator': False,
            'capital': False,
            'transliterate': False
        }

        self.reconfigure(ksargs)

        if self.options['unravel']:
            # 초성 19 자
            self.Ls = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ','ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
            # 중성 21 자
            self.Vs = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
            # 종성 28 자
            self.Ts = ['', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
        else:
            self.Ls = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ','ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
            self.Vs = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
            self.Ts = ['', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']


    def reconfigure(self, options) -> None:

        for key in self.options.keys():
            if key in options:
                self.options[key] = options.get(key)


        # 음운 변화
    def phonetic_change(self) -> None:
        #쌍받침
        self.transcribed= re.sub('ㄺ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄳ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄱ', self.transcribed)
        self.transcribed= re.sub('ㅄ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㅂ', self.transcribed)
        self.transcribed= re.sub('ㅀ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄶ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄴ', self.transcribed)
        self.transcribed= re.sub('ㄵ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄴ', self.transcribed)
        self.transcribed= re.sub('ㄻ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄼ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄽ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄾ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄿ(!=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㄹ', self.transcribed)

        #겹받침 된소리 처리
        self.transcribed= re.sub('ㄺ/ㄱ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅋ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㄲ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅆ', 'ㄹ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅅ', 'ㄹ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅊ', 'ㄹ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅉ', 'ㄹ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅈ', 'ㄹ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㄸ', 'ㄹ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅌ', 'ㄹ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㄷ', 'ㄹ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅃ', 'ㄹ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄺ/ㅂ', 'ㄹ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄳ/ㄱ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄳ/ㄱ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㅀ/ㄱ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅋ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㄲ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅅ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅈ', 'ㄹ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅊ', 'ㄹ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅉ', 'ㄹ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㄷ', 'ㄹ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅌ', 'ㄹ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㄸ', 'ㄹ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅂ', 'ㄹ/ㅂ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅃ', 'ㄹ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㅀ/ㅆ', 'ㄹ/ㅆ', self.transcribed)
           
        
        self.transcribed= re.sub('ㄶ/ㄱ', 'ㄴ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄵ', 'ㄴ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄻ', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄼ', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄽ', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄾ', 'ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        self.transcribed= re.sub('ㄿ/ㄱ', 'ㄹ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅋ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄲ', 'ㄱ/ㄲ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅆ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅅ', 'ㄱ/ㅆ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅊ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅉ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅈ', 'ㄱ/ㅉ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄸ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅌ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㄷ', 'ㄱ/ㄸ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅃ', 'ㄱ/ㅃ', self.transcribed)
        self.transcribed= re.sub('ㄳ/ㅂ', 'ㄱ/ㅃ', self.transcribed)
        
        
        # 받침 및 쌍받침
        self.transcribed= re.sub('(?<!n)ㅈ(?=/[gkndlmbsjcktph]|$)', 'ㄱ', self.transcribed)
        self.transcribed= re.sub('ㄷ(?=/[gkndlmbsjcktph]|$)', 'ㄷ', self.transcribed)
        self.transcribed= re.sub('ㅂ(?=/[ㅂㅈㄷㄱㄲㅅㅁㄴㅇㄹㅃㅎㅋㅌㅊㅍ]|$)', 'ㅍ', self.transcribed)
        self.transcribed= re.sub('ㅆ/ㅇ(?=[ㅏㅓㅣㅗㅜㅖㅔㅒㅐ])', 'ㅅ/ㅅ', self.transcribed)
        self.transcribed= re.sub('ㅆ(?=/&&!=/ㅇ|$)|ㅅ(?=/|$)', 'ㄷ', self.transcribed)
        self.transcribed= re.sub('(?<!ㄴ)ㅈ(?=/|$)', 'ㄷ', self.transcribed)
        self.transcribed= re.sub('ㅊ(!=/ㅇ|$)', 'ㄷ', self.transcribed)
        
        # 리을
        self.transcribed= re.sub('ㄹ/ㅇ', 'ㄹ/ㄹ', self.transcribed) # 알약
        self.transcribed= re.sub('ㄹ(?=[aeiouwy])', 'ㄴ', self.transcribed)
        self.transcribed= re.sub('ㄹ/(?=[aeiouwy])', '/ㄹ', self.transcribed)
        self.transcribed= re.sub('ㄹ/ㄴ', 'ㄹ/ㄹ', self.transcribed)
        
        # # 자음 동화
        self.transcribed= re.sub('ㄱ/ㅁ', 'ㅇ/ㅁ', self.transcribed) # 백마
        self.transcribed= re.sub('ㄱ/ㄴ', 'ㅇ/ㄴ', self.transcribed) 
        self.transcribed= re.sub('(?<!ㄴ)ㄱ/ㅇ', 'ㅇ/ㄴ', self.transcribed) # 학여울
        self.transcribed= re.sub('ㄴ/ㄹ(?=ㅏ|ㅖ)', 'ㄹ/ㄹ', self.transcribed) # 대관령, 신라
        self.transcribed= re.sub('ㄹ/ㄴ', 'ㄴ/ㄴ', self.transcribed) # 신문로
        self.transcribed= re.sub('ㅍ/ㄴ', 'ㅁ/ㄴ', self.transcribed) # 왕십리
        self.transcribed= re.sub('ㄹ/ㄴ', 'ㄹ/ㄹ', self.transcribed) # 별내
        self.transcribed= re.sub('ㅇ/ㄹ', 'ㅇ/ㄴ', self.transcribed) # 종로
        self.transcribed= re.sub('ㄱ/ㄹ', 'ㅇ/ㄴ', self.transcribed) # 독립문
        self.transcribed= re.sub('ㅂ/ㅁ', 'ㅁ/ㅁ', self.transcribed) # 독립문
        
        # 구개음화
        self.transcribed= re.sub('ㅊ/ㅇ', '/ㅊ', self.transcribed) # 꽃이
        self.transcribed= re.sub('ㄷ/ㅇ', '/ㅈ', self.transcribed) # 해돋이
        self.transcribed= re.sub('ㄷ/ㅎ', '/ㅊ', self.transcribed) # 굳히다
        self.transcribed= re.sub('ㅌ/ㅎ', '/ㅊ', self.transcribed) # 궅히다
        self.transcribed= re.sub('ㅌ/ㅇ', '/ㅊ', self.transcribed) # 같이
        self.transcribed= re.sub('ㅂ/ㅎ', '/ㅍ', self.transcribed) # 잡혀
        
        # 격음화
        self.transcribed= re.sub('ㄱ/ㅋ', '/ㅋ', self.transcribed) 
        self.transcribed= re.sub('ㅋ/ㅎ', '/ㅋ', self.transcribed) 
        self.transcribed= re.sub('ㅎ/ㄷ', '/ㅌ', self.transcribed) 
        self.transcribed= re.sub('ㅂ/ㅎ', '/ㅍ', self.transcribed) 
        self.transcribed= re.sub('ㅎ/ㅈ', '/ㅊ', self.transcribed) 
        self.transcribed= re.sub('ㄱ/ㅎ', '/ㅋ', self.transcribed) 
        self.transcribed= re.sub('ㄲ/ㅋ', '/ㅋ', self.transcribed) 
        self.transcribed= re.sub('ㅎ/ㅌ', '/ㅌ', self.transcribed)
        
        #쌍모음처리
        self.transcribed= re.sub('ㅚ', 'ㅗㅣ', self.transcribed) 
        self.transcribed= re.sub('ㅙ', 'ㅗㅐ', self.transcribed) 
        self.transcribed= re.sub('ㅘ', 'ㅗㅏ', self.transcribed) 
        self.transcribed= re.sub('ㅝ', 'ㅜㅓ', self.transcribed) 
        self.transcribed= re.sub('ㅞ', 'ㅜㅔ', self.transcribed) 
        self.transcribed= re.sub('ㅟ', 'ㅜㅣ', self.transcribed) 
        self.transcribed= re.sub('ㅢ', 'ㅡㅣ', self.transcribed) 
        
        

    def transcribe(self, word, **options) -> str:

        self.reconfigure(options)

        characters = []
        ci = 0
        for i, c in enumerate(word):
            #i는 숫자 c는 단어를 말함
            if i == 0:
                characters.append(c)
            elif ord(c) >= 0xAC00 and ord(c) <= 0xDC73:
                if ord(characters[ci][0]) >= 0xAC00 and ord(characters[ci][0]) <= 0xDC73:
                    characters[ci] +=  c
                else:
                    characters.append(c)
                    ci += 1 
            else:
                characters.append(c)
                ci += 1 
                
        for i, c in enumerate(characters):
            if ord(c[0]) >= 0xAC00 and ord(c[0]) <= 0xDC73:
                characters[i] = self.transcribe_hangul(c)
                

        return ''.join(characters)

    def transcribe_hangul(self, word) -> str:

        syllable = ''
        syllables = []
        self.transcribed = ''

        # 낱자를 자모로 분해
        for c in word:
            code_point =  ord(c) - 0xAC00
            L = int(code_point / (21*28))
            V = int(code_point % (21*28) / 28) 
            T = code_point % 28

            # 로마자로 치환
            syllable = self.Ls[L] + self.Vs[V] + self.Ts[T]
            syllables.append(syllable)
            

        if self.options['unravel']:
            if self.options['separator']:
                self.transcribed = '/'.join(syllables)
            else:
                self.transcribed = ''.join(syllables)
            return self.transcribed
        else:
            # 음절 구분 기호 삽입
            self.transcribed = '/'.join(syllables)
        #print(self.transcribed)
        # 음운 변화
        if not self.options['transliterate']:
            self.phonetic_change()

        if not self.options['separator']:
            self.transcribed= re.sub('a/e', 'a-e', self.transcribed) 
            self.transcribed= re.sub('e/e', 'e-e', self.transcribed) 
            self.transcribed= re.sub('ng/(?=[aeiouwy])', 'ng-', self.transcribed) 
            self.transcribed= re.sub('n/g', 'n-g', self.transcribed) 
            self.transcribed = self.transcribed.replace('/', '')
        if self.options['capital']:
            self.transcribed = self.transcribed.upper()
        
        return self.transcribed


class EnglishToHangul(object):

    def __init__(self, **kwargs):

        self.options = {
            'phonetic': False,
            'derivative': False,
            'debug': False
        }

        self.reconfigure(kwargs)

        self.consonants = {
            # consonants
            'p':'ㅍ', 'b':'ㅂ', 't':'ㅌ', 'd':'ㄷ', 'k':'ㅋ', 'g':'ㄱ', 'f':'ㅍ', 'v':'ㅂ', 'θ':'ㅅ',
            'ð':'ㄷ', 's':'ㅅ', 'z':'ㅈ', 'ʃ':'S', 'ʒ':'ㅈ', 'ʦ':'ㅊ', 'ʣ':'ㅈ', 'ʧ':'ㅊ', 'ʤ':'ㅈ',
            'm':'ㅁ', 'n':'ㄴ', 'ɲ':'N', 'ŋ':'ㅇ', 'l':'ㄹ', 'r':'ㄹ', 'h':'ㅎ', 'ç':'ㅎ', 'x':'ㅎ',
            # semivowels
            'j':'ㅣ', 'ɥ':'ㅟ', 'w':'ㅜ'
        }
        self.vowels = {
            # vowels 
            'i':'ㅣ', 'ɪ':'ㅣ', 'y':'ㅟ', 'e':'ㅔ', 'ø':'ㅚ', 'ɛ':'ㅔ', 'ɛ̃':'E', 'œ':'ㅚ', 'æ':'ㅐ',
            'a':'ㅏ', 'ɑ':'ㅏ', 'ɑ̃':'A', 'ʌ':'ㅓ', 'ɔ':'ㅗ', 'ɔ̃':'O', 'o':'ㅗ', 'ə':'ㅓ', 'ɚ':'ㅓ',
            'ʊ':'ㅜ', 'u':'ㅜ'
        }
        self.consonant_symbols = self.consonants.keys()
        self.vowel_symbols = self.vowels.keys()

        self.Ls = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ','ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        self.Vs = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        self.Ts = [' ', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

        self.errata = {
            'our': 'auər',
            'penguin':'peŋgwin',
            'to': 'tu',
            'when': 'wen'
        }


    def reconfigure(self, options) -> None:

        for key in self.options.keys():
            if key in options:
                self.options[key] = options.get(key)


    # 음절 구분
    def syllabify(self) -> None:

        # 각 발음 기호를 자음(C)과 모음(V)으로 구분
        self.CV = ''
        phonetic = ''
        for i in self.phonetic:
            if i in self.consonant_symbols:
                self.CV += 'C'
                phonetic += i
            elif i in self.vowel_symbols:
                self.CV += 'V'
                phonetic += i

        # 발음 음절 식별
        self.CV = re.sub('CVCV', 'CV/CV', self.CV)
        self.CV = re.sub('CCC', 'C/C/C', self.CV)
        self.CV = re.sub('CVCC', 'CVC/C', self.CV)
        self.CV = re.sub('CCV', 'C/CV', self.CV)
        self.CV = re.sub('CVVCV', 'CV/V/CV', self.CV)
        self.CV = re.sub('VCV', 'V/CV', self.CV)
        self.CV = re.sub('CVVVC', 'CV/V/VC', self.CV)
        self.CV = re.sub('VCC', 'VC/C', self.CV)
        self.CV = re.sub('CVVC', 'CV/VC', self.CV)
        self.CV = re.sub('VVC', 'V/VC', self.CV)
        self.CV = re.sub('CVVV', 'CV/VV', self.CV)
        self.CV = re.sub('CVV', 'CV/V', self.CV)
        self.CV = re.sub('VV', 'V/V', self.CV)

        # 발음 음절 나누기
        CV_syllabic = self.CV
        self.phonetic_syllabic = ''
        while len(CV_syllabic) > 0:
            if CV_syllabic[0:1] == '/':
                self.phonetic_syllabic += '/'
            else:
                self.phonetic_syllabic += phonetic[0:1]
                phonetic = phonetic[1:]
            CV_syllabic = CV_syllabic[1:]


        # 음운 변화
        self.phonetic_syllabic = re.sub('(?<=[pbtdkgfvθðszʃʒʦʣʧʤɲŋlrhçx])/l', 'l/l', self.phonetic_syllabic) # plural
        self.phonetic_syllabic = re.sub('(?<=[iɪyeøɛœæaɑʌɔoəɚu])([pbtdkgfvθðszʃʒʦʣʧʤɲŋlrhçx])l', '/\\1l', self.phonetic_syllabic) 
        self.phonetic_syllabic = re.sub('(?<=[iɪyeøɛœæaɑʌɔoəɚu])/l', 'l/l', self.phonetic_syllabic) 
        self.phonetic_syllabic = re.sub('l/m$', 'l/lm', self.phonetic_syllabic) # film
        # 파열음
        self.phonetic_syllabic = re.sub('(?<=/[iɪyeøɛœæaɑʌɔoəɚu])([bdgptkszfvθð])(?=$)', '/\\1', self.phonetic_syllabic) 
        self.phonetic_syllabic = re.sub('([ptk])(?=/[lrmn])', '/\\1', self.phonetic_syllabic) 
        self.phonetic_syllabic = re.sub('(?<!^)s(?=/[tkp])', '/s', self.phonetic_syllabic) 
        self.phonetic_syllabic = re.sub('(?<=[əʊu])s$', '/s', self.phonetic_syllabic) 
        self.phonetic_syllabic = re.sub('(?<=[iɪyeøɛœæaɑʌɔoəɚu])([bgdzfv])(?=/|$)', '/\\1', self.phonetic_syllabic) 
        # 마찰음과 파찰음
        self.phonetic_syllabic = re.sub('ʒ$', '/ʒi', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('ʤ$', '/ʤi', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('ʧ(?=/|$)', '/ʧi', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('ʃ$', '/ʃ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('ʃ/', 'ʃu/', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('d/z', '/z', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('t/s', '/ʦ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('s$', '/s', self.phonetic_syllabic)

        # 반모음 w, j
        self.phonetic_syllabic = re.sub('w/?[əɔo]', 'wə', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('w/?[ɑa]', 'wa', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('w/?æ', 'wæ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('w/?ɛ', 'wɛ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('w/?[iɪ]', 'wi', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('w/?[ʊu]', 'u', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('(?<=[pbtdfvθðszʃʒʦʣʧʤɲŋlrçx])w', '/w', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?[ɑa]', 'jɑ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?æ', 'jæ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?ə', 'jə', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?ɛ', 'jɛ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?[oɔ]', 'jo', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?[ʊu]', 'ju', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('j/?[iɪ]', 'ɪ', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('(?<=[dln])jə', 'i/ə', self.phonetic_syllabic)
        # 장음
        self.phonetic_syllabic = re.sub('ur$', 'u/ə', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('(?<=[aɑəɔo])r/(?=n)', '', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('(?<=[aɑəɔo])r', '', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('(?<=o)/ʊ', '/', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('(?<=[əo])ʊ$', '', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('/l$', 'l', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('ʊ/ə', 'wə', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('ɪr', 'i/ə', self.phonetic_syllabic)

        self.phonetic_syllabic = re.sub('/ŋ', 'ŋ/', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('//', '/', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('^/', '', self.phonetic_syllabic)
        self.phonetic_syllabic = re.sub('/$', '', self.phonetic_syllabic)


    # 첫가끝 결합
    def compose(self, jamo) -> str:

        s = len(jamo)
        if s == 3:
            L = jamo[0]
            V = jamo[1]
            T = jamo[2]
        elif s == 2:
            if jamo[0] in self.Ls and jamo[1] in self.Vs:
                L = jamo[0]
                V = jamo[1]
                T = ' '
            elif jamo[0] in self.Ls and jamo[1] in self.Ts:
                L = jamo[0]
                V = 'ㅡ'
                T = jamo[1]
            else:
                L = 'ㅇ'
                V = jamo[0]
                T = jamo[1]
        else:
            if jamo in self.Ls:
                L = jamo
                V = 'ㅡ'
                T = ' '
            else:
                L = 'ㅇ'
                V = jamo
                T = ' '

        code_point = (self.Ls.index(L) * 21 + self.Vs.index(V)) * 28 + self.Ts.index(T) + 0xAC00
        return chr(code_point)

    # 음운 변화
    def phonetic_change(self) -> None:

        # 받침
        self.transcribed = re.sub('(?<=[ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅞㅠㅡㅢㅣ])[ㅋ]', 'ㄱ', self.transcribed)
        self.transcribed = re.sub('(?<=[ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅞㅠㅡㅢㅣ])[ㅍ]', 'ㅂ', self.transcribed)
        self.transcribed = re.sub('(?<=[ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅞㅠㅡㅢㅣ])[ㅌ]', 'ㅅ', self.transcribed)
        # 리을
        self.transcribed = re.sub('ㄹ/(?=[ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅞㅠㅡㅢㅣ])', 'ㄹ/ㄹ', self.transcribed)
        # 어말
        self.transcribed = re.sub('(?<=[ㅋㅌㅍ])$', 'ㅡ', self.transcribed)
        # ʃ
        self.transcribed = re.sub('S(?=$)', 'ㅅㅣ', self.transcribed)
        self.transcribed = re.sub('Sㅏ', 'ㅅㅑ', self.transcribed)
        self.transcribed = re.sub('Sㅐ', 'ㅅㅒ', self.transcribed)
        self.transcribed = re.sub('Sㅓ', 'ㅅㅕ', self.transcribed)
        self.transcribed = re.sub('Sㅔ', 'ㅅㅖ', self.transcribed)
        self.transcribed = re.sub('Sㅗ', 'ㅅㅛ', self.transcribed)
        self.transcribed = re.sub('Sㅜ', 'ㅅㅠ', self.transcribed)
        self.transcribed = re.sub('S(?=[ㄱㄴㄷㄹㅁㅂㅈㅊㅋㅌㅍㅎ])', 'ㅅㅠ', self.transcribed)
        self.transcribed = re.sub('S', 'ㅅ', self.transcribed)
        # 중모음
        self.transcribed = re.sub('ㅜㅓ', 'ㅝ', self.transcribed)
        self.transcribed = re.sub('ㅜㅏ', 'ㅘ', self.transcribed)
        self.transcribed = re.sub('ㅜㅐ', 'ㅙ', self.transcribed)
        self.transcribed = re.sub('ㅜㅔ', 'ㅞ', self.transcribed)
        self.transcribed = re.sub('ㅜㅣ', 'ㅟ', self.transcribed)
        
        self.transcribed = re.sub('ㅣㅏ', 'ㅑ', self.transcribed)
        self.transcribed = re.sub('ㅣㅐ', 'ㅒ', self.transcribed)
        self.transcribed = re.sub('ㅣㅓ', 'ㅕ', self.transcribed)        
        self.transcribed = re.sub('ㅣㅔ', 'ㅖ', self.transcribed)
        self.transcribed = re.sub('ㅣㅗ', 'ㅛ', self.transcribed)
        self.transcribed = re.sub('ㅣㅜ', 'ㅠ', self.transcribed)


    def transcribe(self, word, **options) -> str:

        self.reconfigure(options)

        letters = []
        li = 0

        for i, l in enumerate(word):
            if i == 0:
                letters.append(l)
            elif (ord(l) >= 0x41 and ord(l) <= 0x5A) or (ord(l) >= 0x61 and ord(l) <= 0x7A):
                if (ord(letters[li][0]) >= 0x41 and ord(letters[li][0]) <= 0x5A) or (ord(letters[li][0]) >= 0x61 and ord(letters[li][0]) <= 0x7A):
                    letters[li] += l
                else:
                    letters.append(l)
                    li += 1
            else:
                letters.append(l)
                li += 1

        for i, l in enumerate(letters):
            if (ord(l[0]) >= 0x41 and ord(l[0]) <= 0x5A) or (ord(l[0]) >= 0x61 and ord(l[0]) <= 0x7A):
                letters[i] = self.transcribe_english(l)

        letters = ''.join(letters)
        letters = letters.replace("'에스", "'스")
        return letters


    def transcribe_english(self, word) -> str:

        # 발음 구하기
        self.phonetic = eng_to_ipa.convert(word)
        if '*' in self.phonetic:
            return word

        if self.errata.get(word):
            self.phonetic = self.errata.get(word)

        # 음절 나누기
        self.syllabify()
        # for bug tracking
        if self.options['debug']:
            print(self.phonetic, self.phonetic_syllabic, self.CV)

        # 한글로 치환
        self.transcribed = ''
        for i in self.phonetic_syllabic:
            if i == '/':
                self.transcribed += i
            else:
                if self.consonants.get(i):
                    self.transcribed += self.consonants.get(i)
                elif self.vowels.get(i):
                    self.transcribed += self.vowels.get(i)

        # 음운 변화
        self.phonetic_change()
        hangul = ''
        # 첫가끝 결합
        for i in self.transcribed.split('/'):
            hangul += self.compose(i)

        if self.options['derivative']:
            output = '[{}]<{}>{}'.format(self.phonetic, self.phonetic_syllabic, hangul)
        elif self.options['phonetic']:
            output = '[{}]{}'.format(self.phonetic, hangul)
        else:
            output = hangul 
        return output


def arg_parse() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description = "Romanize Korean words, or transcribe English words into Hangul."
    )
    parser.add_argument(
        'words',
        nargs = '+',
        help = 'Enter one or more Hangul or English words.'
    )
    parser.add_argument(
        '-s',
        dest = 'separator',
        action = 'store_true',
        default = False,
        help = 'Show syllable separators when transcribing into Roman.'
    )
    parser.add_argument(
        '-c',
        dest = 'capital',
        action = 'store_true',
        default = False,
        help = 'Capitalize the output when transcribing into Roman.'
    )
    parser.add_argument(
        '-l',
        dest = 'transliterate',
        action = 'store_true',
        default = False,
        help = 'Do not transcribe but transliterate to Roman.'
    )
    parser.add_argument(
        '-u',
        dest = 'unravel',
        action = 'store_true',
        default = False,
        help = 'Unravel hangul characters into LVT and do not transcribe.'
    )
    parser.add_argument(
        '-p',
        dest = 'phonetic',
        action = 'store_true',
        default = False,
        help = 'Show phonetic symbols.'
    )
    parser.add_argument(
        '-d',
        dest = 'derivative',
        action = 'store_true',
        default = False,
        help = 'Show derivatives made in process when transcribing into Hangul.'
    )
    parser.add_argument(
        '-b',
        dest = 'debug',
        action = 'store_true',
        default = False,
        help = 'Track bugs when transcribing into Hangul.'
    )

    return parser.parse_args()


if __name__ == '__main__':
    #args = arg_parse()
    K2R = KoreanToRoman(unravel = False)
    E2H = EnglishToHangul()
    count = "굳이 니가 나한테 온다고"
    p = re.compile('[a-zA-Z]')
    output = []
    sentence = []

    words = count.split(' ')
    output.clear()
    for word in words:
        output.append(K2R.transcribe(word, separator= False,capital = False,transliterate = False))
       # output.append(E2H.transcribe(word, phonetic=False, derivative=False, debug=False))
    sentence = ''.join(output)
    print(sentence)
