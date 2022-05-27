import pyaudio
import wave
import numpy as np
from pynput import keyboard
from threading import Thread


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"
NOISE_MININUM_VALUE = 250

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
count = 5
i =0

Thread(target=keyint, daemon=False)
while True:
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        if(int(np.average(np.abs(data))) > NOISE_MININUM_VALUE):
        # print(int(np.average(np.abs(data))))
            frames.extend(data)
        # print("length : ", len(frames))
            if len(frames) > 10:
                print(frames)
                frames = []

            
            
    