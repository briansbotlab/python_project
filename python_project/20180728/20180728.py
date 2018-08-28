'''
from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
print(chatbot.get_response("Are you kidding?"))



'''
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class AlphaBOT:
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # 這個 ChatBot 的名字叫做 AlphaBOT
        "AlphaBOT",
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 AlphaBOT_DB.json
        database = "./AlphaBOT_DB.sqlite3"    
    )

    def __init__(self):
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.corpus.chinese")

    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

if __name__ == "__main__":
    bot = AlphaBOT()
    var = input()
    while (var != 'exit'):
        
        print(bot.getResponse(var))
        var = input()

