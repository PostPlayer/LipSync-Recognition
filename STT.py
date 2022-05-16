import pyaudio
import wave
import time
import numpy as np
import scipy.io.wavfile as sw
import librosa
import scipy
import sys
from scipy.io.wavfile import write


############ Global variables ###################
filename = 'output.wav' #Test file
chunk = 512 #frame size
#Conversion from np to pyAudio types
np_to_pa_format = {
    np.dtype('float32') : pyaudio.paFloat32,
    np.dtype('int32') : pyaudio.paInt32,
    np.dtype('int16') : pyaudio.paInt16,
    np.dtype('int8') : pyaudio.paInt8,
    np.dtype('uint8') : pyaudio.paUInt8
}
np_type_to_sample_width = {
    np.dtype('float32') : 4,
    np.dtype('int32') : 4,
    np.dtype('int16') : 3,
    np.dtype('int8') : 1,
    np.dtype('uint8') : 1
}
STEREO = 2 #channels
#################################################

# Simple class which reads an input test wav file and reproduce it in a real time fashion. Used to test real time functioning.
class Player:
    # Loading the input test file. Crop to 30 seconds length
    def __init__(self):
        self.input_array, self.sample_rate = librosa.load(filename, sr=44100, dtype=np.float32, duration=60)

        #print(self.sample_rate)
        #print(self.input_array.shape)
        self.cycle_count = 0
        self.highcut = 300

    def bandPassFilter(self,signal, highcut):
        fs = 44100
        lowcut = 20
        highcut = highcut

        nyq= 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq

        order = 2

        b, a = scipy.signal.butter(order, [low,high], 'bandpass', analog=False)
        y = scipy.signal.filtfilt(b,a,signal, axis=0)
        return(y)

    def pyaudio_callback(self,in_data, frame_count, time_info, status):
        audio_size = np.shape(self.input_array)[0]
        #print(audio_size)
        print('frame count: ', frame_count)

        if frame_count*self.cycle_count > audio_size:
            # Processing is complete.
            print('processing complete')
            return (None, pyaudio.paComplete)
        elif frame_count*(self.cycle_count+1) > audio_size:
            # Last frame to process.
            print('1 left frame')
            frames_left = audio_size - frame_count*self.cycle_count
        else:
            # Every other frame.
            print('everyotherframe')
            frames_left = frame_count

        data = self.input_array[frame_count*self.cycle_count:frame_count*self.cycle_count+frames_left]
        data = self.bandPassFilter(data, self.highcut)
        if(self.highcut<20000):
            self.highcut += 10

        print('len of data', data.shape)

        #write('test.wav', 44100, data) #Saves correctly the file!
        out_data = data.astype(np.float32).tobytes()
        print('printing length: ',len(out_data))
        #print(out_data)
        self.cycle_count+=1
        print(self.cycle_count)
        print('pyaudio continue value: ',pyaudio.paContinue)
        return (out_data, pyaudio.paContinue)





    def start_non_blocking_processing(self, save_output=True, frame_count=2**10, listen_output=True):
        '''
        Non blocking mode works on a different thread, therefore, the main thread must be kept active with, for example:
            while processing():
                time.sleep(1)
        '''
        self.save_output = save_output
        self.frame_count = frame_count

        # Initiate PyAudio
        self.pa = pyaudio.PyAudio()
        # Open stream using callback
        self.stream = self.pa.open(format=np_to_pa_format[self.input_array.dtype],
                        channels=1,
                        rate=self.sample_rate,
                        output=listen_output,
                        input=not listen_output,
                        stream_callback=self.pyaudio_callback,
                        frames_per_buffer=frame_count)

        # Start the stream
        self.stream.start_stream()


    def processing(self):
        '''
        Returns true if the PyAudio stream is still active in non blocking mode.
        MUST be called AFTER self.start_non_blocking_processing.
        '''
        return self.stream.is_active()

    def terminate_processing(self):
        '''
        Terminates stream opened by self.start_non_blocking_processing.
        MUST be called AFTER self.processing returns False.
        '''
        # Stop stream.
        self.stream.stop_stream()
        self.stream.close()

        # Close PyAudio.
        self.pa.terminate()

        # Resets count.
        self.cycle_count = 0
        # Resets output.
        self.output_array = np.array([[], []], dtype=self.input_array.dtype).T



if __name__ == "__main__":
    print('RUNNING MAIN')
    player = Player()
    player.start_non_blocking_processing()
    while(player.processing()):
        time.sleep(0.1)
    player.terminate_processing()