# -*- coding: utf-8 -*-
"""
Created on Sat May  8 02:30:18 2021

@author: SCS
"""


from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify

import live_predictions
import rec_audio

classifier = rec_audio.EmotionClassifier()
app = Flask(__name__)

@app.route("/home", methods=['GET'])
def index():
    return render_template("semo.html")            

@app.route("/about")
def about():
    return render_template("about.html")
          
@app.route("/home", methods=['GET'])
def home():
    return render_template("semo.html")   

  
          
@app.route("/record", methods=['GET'])
def record():  
    classifier.record_audio()    
    live_prediction=live_predictions.LivePredictions(file='F:\semo_webapp\live_audio.wav')
    print(live_prediction.make_predictions())
        
    return render_template('result.html',names=live_prediction.make_predictions())
'''
@app.route("/show", methods=['POST'])
def show():  
       
    live_prediction=live_predictions.LivePredictions(file='\semo_webapp\live_audio.wav')
    output=live_prediction.make_predictions()
        
    return jsonify(output)
'''

if __name__ == "__main__":
    app.run()
