# -*- coding: utf-8 -*-
from gtts import gTTS 
from pygame import mixer
import tempfile
'''
tts = gTTS(text="hello world", lang='en')
tts.save("welcome.mp3")

'''
def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='en')
        tts.save('{}.mp3'.format(fp.name))
        
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

speak('Google')
