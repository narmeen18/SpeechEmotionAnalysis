# -*- coding: utf-8 -*-
"""
Created on Sat May  8 01:45:44 2021

@author: SCS
"""

import keras
import librosa
import numpy as np


class LivePredictions:

    def __init__(self, file):
        self.file = file
        self.path = 'C:/Users/SCS/FYP2/saved_models/Audio_Emotion_Model_2ds_best.h5'
        #location: C:\Users\SCS\FYP2\saved_models\Audio_Emotion_Model_2ds.h5 
        self.loaded_model = keras.models.load_model(self.path)
        
    def make_predictions(self):
        data, sampling_rate = librosa.load(self.file)
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
        x = np.expand_dims(mfccs, axis=1)
        x = np.expand_dims(x, axis=0)
        predictions = self.loaded_model.predict_classes(x)
        print( "Prediction is", " ",self.convert_class_to_emotion( predictions))
        return self.convert_class_to_emotion(predictions)
    
    @staticmethod
    def convert_class_to_emotion(pred):
        label_conversion = {'0': 'angry',
                            '1': 'calm',
                            '2': 'disgust',
                            '3': 'fear',
                            '4': 'happy',
                            '5': 'neutral',
                            '6': 'sad',
                            '7': 'surprise'}

        for key, value in label_conversion.items():
            if int(key) == pred:
                label = value
        return label

if __name__ == '__main__':
    live_prediction = LivePredictions(file='F:/semo_webapp/live_audio.wav')

    live_prediction.make_predictions()