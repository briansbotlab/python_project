import sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from gtts import gTTS 
from pygame import mixer
import tempfile

import speech_recognition


def Listening():
    e = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = e.listen(source)
    
    value = e.recognize_google(audio,language='zh-TW')
    return value


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh-TW')
        tts.save("{}.mp3".format(fp.name))
        
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()


class KantaiBOT:
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # 這個 ChatBot 的名字叫做 KantaiBOT
        "KantaiBOT",
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 db.json
        database = "./db.sqlite3"    
    )

    def __init__(self):
        
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.corpus.chinese")

    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

if __name__ == "__main__":
    bot = KantaiBOT()
    while True:
        #value = input()
        value=Listening()
        print(value)
        print(bot.getResponse(value))
        speak(str(bot.getResponse(value)))
        