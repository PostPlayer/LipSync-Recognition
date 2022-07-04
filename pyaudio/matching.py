import pyaudio
import wave
import numpy as np
from pynput import keyboard
from threading import Thread
import cv2
from matplotlib import pyplot as plt
from IPython import display 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"
NOISE_MININUM_VALUE = 250

#def show():
    

def on_press(key):
    if key == keyboard.Key.esc:
        print("Recording is finished.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        exit()    
    print("key : ", type(key), key)
    
def keyint():
    with keyboard.Listener(
        on_press=on_press,
    ) as listener:
        listener.join()

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Start to record the audio.")

frames = []

Thread(target=keyint, daemon=False)
while True:
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    if(int(np.average(np.abs(data))) > NOISE_MININUM_VALUE):
        # print(int(np.average(np.abs(data))))
        frames.extend(data)
        # print("length : ", len(frames))
        if (1000>int(np.average(np.abs(data))) > 700):
            image = cv2.imread("state/state_lough.png", cv2.IMREAD_UNCHANGED)
            cv2.imshow("ough", image)

            cv2.waitKey(0)
            cv2.destroyAllWindows() 
            
        if (int(np.average(np.abs(data))) > 250):
            image = cv2.imread("state/state_OH.png", cv2.IMREAD_UNCHANGED)
            cv2.imshow("OH", image)

            cv2.waitKey(0)
            cv2.destroyAllWindows() 
