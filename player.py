import pyaudio
import wave
import sys

CHUNK = 1024
def Playing():  
    if len('test.wav') < 2:
        print("Plays a wave file.\n\nUsage: test.wav filename.wav")
        sys.exit(-1)

    wf = wave.open('test.wav')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()