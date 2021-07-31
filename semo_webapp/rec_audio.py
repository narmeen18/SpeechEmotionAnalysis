# -*- coding: utf-8 -*-
"""
Created on Sat May  8 01:46:07 2021

@author: SCS
"""

import pyaudio
import wave
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras import backend as K
from keras.models import load_model
from keras.optimizers import RMSprop


class EmotionClassifier():

        # For recording audio
    def record_audio(self):
        CHUNK = 1024 
        FORMAT = pyaudio.paInt16 #paInt8
        CHANNELS = 2 
        RATE = 44100 #sample rate
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "live_audio.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            
            frames.append(data) # 2 bytes(16 bits) per channel

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        return True;