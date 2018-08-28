import speech_recognition
e =speech_recognition.Recognizer()
AUDIO_FILE = "C:\\Users\\admin\\Downloads\\welcome.wav"
'''
with speech_recognition.Microphone() as source:
    audio = e.listen(source)

'''
with speech_recognition.AudioFile(AUDIO_FILE) as source:
    audio = e.record(source)
  
#t = e.recognize_google(audio,language='zh-TW')
t = e.recognize_google(audio)
print(t)



