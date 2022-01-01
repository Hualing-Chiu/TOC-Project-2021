import os
import sys

from transitions.extensions import GraphMachine
import message_template
from utils import send_text_message,send_breakfast,send_restaurant_type,send_snack,send_western,send_japanese,send_korean,send_healthy,send_tainan, send_thai,send_restaurant_info, send_button_carousel
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage

load_dotenv()

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def on_enter_start(self, event):
        print("I'm entering go")

        userid = event.source.user_id
        send_button_carousel(userid)

    def is_going_to_breakfast(self, event):
        text = event.message.text
        return text.lower() == "breakfast"

    def on_enter_breakfast(self, event):
        print("I'm entering breakfast")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_breakfast(reply_token, userid)

    def is_going_to_lunchdinner(self, event):
        text = event.message.text
        return text.lower() == "lunchdinner"

    def on_enter_lunchdinner(self, event):
        print("I'm entering lunch dinner")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_restaurant_type(reply_token, userid)

    def is_going_to_snack(self, event):
        text = event.message.text
        return text.lower() == "snack"

    def on_enter_snack(self, event):
        print("I'm entering snack")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_snack(reply_token, userid)

    def is_going_to_western(self, event):
        text = event.message.text
        return text.lower() == "western"

    def on_enter_western(self, event):
        print("I'm entering western")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_western(reply_token, userid)

    def is_going_to_japanese(self, event):
        text = event.message.text
        return text.lower() == "japanese"

    def on_enter_japanese(self, event):
        print("I'm entering japanese")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese(reply_token, userid)

    def is_going_to_korean(self, event):
        text = event.message.text
        return text.lower() == "korean"

    def on_enter_korean(self, event):
        print("I'm entering korean")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_korean(reply_token, userid)

    def is_going_to_thai(self, event):
        text = event.message.text
        return text.lower() == "thai"

    def on_enter_thai(self, event):
        print("I'm entering thai")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_thai(reply_token, userid)

    def is_going_to_healthy(self, event):
        text = event.message.text
        return text.lower() == "healthy"

    def on_enter_healthy(self, event):
        print("I'm entering healthy")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_healthy(reply_token, userid)

    def is_going_to_tainan(self, event):
        text = event.message.text
        return text.lower() == "tainan"

    def on_enter_tainan(self, event):
        print("I'm entering tainan")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_tainan(reply_token, userid)

    def is_going_to_western_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "western_restaurant1"

    def on_enter_western_restaurant1(self, event):
        print("I'm entering western_restaurant1")
        reply_token = event.reply_token
        message = message_template.western1
        message_to_reply = FlexSendMessage("V餐館",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_western_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "western_restaurant2"

    def on_enter_western_restaurant2(self, event):
        print("I'm entering western_restaurant2")
        reply_token = event.reply_token
        message = message_template.western2
        message_to_reply = FlexSendMessage("庫肯花園",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_western_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "western_restaurant3"

    def on_enter_western_restaurant3(self, event):
        print("I'm entering western_restaurant3")
        reply_token = event.reply_token
        message = message_template.western3
        message_to_reply = FlexSendMessage("Is義式餐廳",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()
    
    def is_going_to_breakfast_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "breakfast_restaurant1"

    def on_enter_breakfast_restaurant1(self, event):
        print("I'm entering breakfast_restaurant1")
        reply_token = event.reply_token
        message = message_template.breakfast1
        message_to_reply = FlexSendMessage("少爺蛋餅",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_breakfast_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "breakfast_restaurant2"

    def on_enter_breakfast_restaurant2(self, event):
        print("I'm entering breakfast_restaurant2")
        reply_token = event.reply_token
        message = message_template.breakfast2
        message_to_reply = FlexSendMessage("緹克廚房",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_breakfast_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "breakfast_restaurant3"

    def on_enter_breakfast_restaurant3(self, event):
        print("I'm entering breakfast_restaurant3")
        reply_token = event.reply_token
        message = message_template.breakfast3
        message_to_reply = FlexSendMessage("六吋盤",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
        self.go_back()

    def is_going_to_breakfast_restaurant4(self, event):
        text = event.message.text
        return text.lower() == "breakfast_restaurant4"

    def on_enter_breakfast_restaurant4(self, event):
        print("I'm entering breakfast_restaurant4")
        reply_token = event.reply_token
        message = message_template.breakfast4
        message_to_reply = FlexSendMessage("良辰吉食",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()
    
    def is_going_to_breakfast_restaurant5(self, event):
        text = event.message.text
        return text.lower() == "breakfast_restaurant5"

    def on_enter_breakfast_restaurant5(self, event):
        print("I'm entering breakfast_restaurant5")
        reply_token = event.reply_token
        message = message_template.breakfast5
        message_to_reply = FlexSendMessage("海鷗牌餐飲城",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_breakfast_restaurant6(self, event):
        text = event.message.text
        return text.lower() == "breakfast_restaurant6"

    def on_enter_breakfast_restaurant6(self, event):
        print("I'm entering breakfast_restaurant6")
        reply_token = event.reply_token
        message = message_template.breakfast6
        message_to_reply = FlexSendMessage("謝家飯糰",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_japanese_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "japanese_restaurant1"

    def on_enter_japanese_restaurant1(self, event):
        print("I'm entering japanese_restaurant1")
        reply_token = event.reply_token
        message = message_template.japanese1
        message_to_reply = FlexSendMessage("石火山碳燒蓋飯",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_japanese_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "japanese_restaurant2"

    def on_enter_japanese_restaurant2(self, event):
        print("I'm entering japanese_restaurant2")
        reply_token = event.reply_token
        message = message_template.japanese2
        message_to_reply = FlexSendMessage("井選日式定食",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()
    
    def is_going_to_japanese_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "japanese_restaurant3"

    def on_enter_japanese_restaurant3(self, event):
        print("I'm entering japanese_restaurant3")
        reply_token = event.reply_token
        message = message_template.japanese3
        message_to_reply = FlexSendMessage("肉肉控",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_korean_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "korean_restaurant1"

    def on_enter_korean_restaurant1(self, event):
        print("I'm entering korean_restaurant1")
        reply_token = event.reply_token
        message = message_template.korean1
        message_to_reply = FlexSendMessage("歐八不是阿啾喜",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_korean_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "korean_restaurant2"

    def on_enter_korean_restaurant2(self, event):
        print("I'm entering korean_restaurant2")
        reply_token = event.reply_token
        message = message_template.korean2
        message_to_reply = FlexSendMessage("大韓名鍋",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_korean_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "korean_restaurant2"

    def on_enter_korean_restaurant3(self, event):
        print("I'm entering korean_restaurant3")
        reply_token = event.reply_token
        message = message_template.korean3
        message_to_reply = FlexSendMessage("韓朝",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_thai_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "thai_restaurant1"

    def on_enter_thai_restaurant1(self, event):
        print("I'm entering thai_restaurant1")
        reply_token = event.reply_token
        message = message_template.thai1
        message_to_reply = FlexSendMessage("珍妮花與南洋杉",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_thai_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "thai_restaurant2"
    
    def on_enter_thai_restaurant2(self, event):
        print("I'm entering thai_restaurant2")
        reply_token = event.reply_token
        message = message_template.thai2
        message_to_reply = FlexSendMessage("BITCH小姐",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_thai_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "thai_restaurant3"

    def on_enter_thai_restaurant3(self, event):
        print("I'm entering thai_restaurant3")
        reply_token = event.reply_token
        message = message_template.thai3
        message_to_reply = FlexSendMessage("Nest de 后院泰式餐廳",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_healthy_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "healthy_restaurant1"
    
    def on_enter_healthy_restaurant1(self, event):
        print("I'm entering healthy_restaurant1")
        reply_token = event.reply_token
        message = message_template.healthy1
        message_to_reply = FlexSendMessage("就4水煮餐",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_healthy_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "healthy_restaurant2"

    def on_enter_healthy_restaurant2(self, event):
        print("I'm entering healthy_restaurant2")
        reply_token = event.reply_token
        message = message_template.healthy2
        message_to_reply = FlexSendMessage("大口咬定",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_healthy_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "healthy_restaurant3"
    
    def on_enter_healthy_restaurant3(self, event):
        print("I'm entering healthy_restaurant3")
        reply_token = event.reply_token
        message = message_template.healthy3
        message_to_reply = FlexSendMessage("輕水煮xLight Food",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_tainan_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "tainan_restaurant1"

    def on_enter_tainan_restaurant1(self, event):
        print("I'm entering tainan_restaurant1")
        reply_token = event.reply_token
        message = message_template.tainan1
        message_to_reply = FlexSendMessage("雙生綠豆沙牛奶",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_tainan_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "tainan_restaurant2"

    def on_enter_tainan_restaurant2(self, event):
        print("I'm entering tainan_restaurant2")
        reply_token = event.reply_token
        message = message_template.tainan2
        message_to_reply = FlexSendMessage("文章牛肉湯",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_tainan_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "tainan_restaurant3"

    def on_enter_tainan_restaurant3(self, event):
        print("I'm entering tainan_restaurant3")
        reply_token = event.reply_token
        message = message_template.tainan3
        message_to_reply = FlexSendMessage("王氏魚皮",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_snack_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "snack_restaurant1"

    def on_enter_snack_restaurant1(self, event):
        print("I'm entering snack_restaurant1")
        reply_token = event.reply_token
        message = message_template.snack1
        message_to_reply = FlexSendMessage("一點刈包",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()

    def is_going_to_snack_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "snack_restaurant2"

    def on_enter_snack_restaurant2(self, event):
        print("I'm entering snack_restaurant2")
        reply_token = event.reply_token
        message = message_template.snack2
        message_to_reply = FlexSendMessage("咕嚕叫土司",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()
    
    def is_going_to_snack_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "snack_restaurant3"

    def on_enter_snack_restaurant3(self, event):
        print("I'm entering snack_restaurant3")
        reply_token = event.reply_token
        message = message_template.snack3
        message_to_reply = FlexSendMessage("紅記早點",message)
        # send_text_message(reply_token,message_to_reply)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

        self.go_back()
