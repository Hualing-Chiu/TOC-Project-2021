import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn
from fsm import TocMachine
from utils import send_text_message, send_image_message

load_dotenv()


machine = TocMachine(
    states=["user", "start","breakfast","lunchdinner","snack","breakfast_restaurant1","breakfast_restaurant2","breakfast_restaurant3","breakfast_restaurant4","breakfast_restaurant5","breakfast_restaurant6",
            "western","japanese","korean","thai","healthy","tainan","snack_restaurant1","snack_restaurant2","snack_restaurant3","western_restaurant1","western_restaurant2","western_restaurant3",
            "japanese_restaurant1","japanese_restaurant2","japanese_restaurant3","korean_restaurant1","korean_restaurant2","korean_restaurant3","thai_restaurant1","thai_restaurant2","thai_restaurant3",
            "healthy_restaurant1","healthy_restaurant2","healthy_restaurant3","tainan_restaurant1","tainan_restaurant2","tainan_restaurant3"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "breakfast",
            "conditions": "is_going_to_breakfast",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "lunchdinner",
            "conditions": "is_going_to_lunchdinner",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "snack",
            "conditions": "is_going_to_snack",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_restaurant1",
            "conditions": "is_going_to_breakfast_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_restaurant2",
            "conditions": "is_going_to_breakfast_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_restaurant3",
            "conditions": "is_going_to_breakfast_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_restaurant4",
            "conditions": "is_going_to_breakfast_restaurant4",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_restaurant5",
            "conditions": "is_going_to_breakfast_restaurant5",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_restaurant6",
            "conditions": "is_going_to_breakfast_restaurant6",
        },
        {
            "trigger": "advance",
            "source": "lunchdinner",
            "dest": "western",
            "conditions": "is_going_to_western",
        },
        {
            "trigger": "advance",
            "source": "lunchdinner",
            "dest": "japanese",
            "conditions": "is_going_to_japanese",
        },
        {
            "trigger": "advance",
            "source": "lunchdinner",
            "dest": "korean",
            "conditions": "is_going_to_korean",
        },
        {
            "trigger": "advance",
            "source": "lunchdinner",
            "dest": "thai",
            "conditions": "is_going_to_thai",
        },
        {
            "trigger": "advance",
            "source": "lunchdinner",
            "dest": "healthy",
            "conditions": "is_going_to_healthy",
        },
        {
            "trigger": "advance",
            "source": "lunchdinner",
            "dest": "tainan",
            "conditions": "is_going_to_tainan",
        },
        {
            "trigger": "advance",
            "source": "snack",
            "dest": "snack_restaurant1",
            "conditions": "is_going_to_snack_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "snack",
            "dest": "snack_restaurant2",
            "conditions": "is_going_to_snack_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "snack",
            "dest": "snack_restaurant3",
            "conditions": "is_going_to_snack_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "western",
            "dest": "western_restaurant1",
            "conditions": "is_going_to_western_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "western",
            "dest": "western_restaurant2",
            "conditions": "is_going_to_western_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "western",
            "dest": "western_restaurant3",
            "conditions": "is_going_to_western_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "japanese",
            "dest": "japanese_restaurant1",
            "conditions": "is_going_to_japanese_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "japanese",
            "dest": "japanese_restaurant2",
            "conditions": "is_going_to_japanese_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "japanese",
            "dest": "japanese_restaurant3",
            "conditions": "is_going_to_japanese_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "korean",
            "dest": "korean_restaurant1",
            "conditions": "is_going_to_korean_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "korean",
            "dest": "korean_restaurant2",
            "conditions": "is_going_to_korean_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "korean",
            "dest": "korean_restaurant3",
            "conditions": "is_going_to_korean_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "thai",
            "dest": "thai_restaurant1",
            "conditions": "is_going_to_thai_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "thai",
            "dest": "thai_restaurant2",
            "conditions": "is_going_to_thai_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "thai",
            "dest": "thai_restaurant3",
            "conditions": "is_going_to_thai_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "healthy",
            "dest": "healthy_restaurant1",
            "conditions": "is_going_to_healthy_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "healthy",
            "dest": "healthy_restaurant2",
            "conditions": "is_going_to_healthy_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "healthy",
            "dest": "healthy_restaurant3",
            "conditions": "is_going_to_healthy_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "tainan",
            "dest": "tainan_restaurant1",
            "conditions": "is_going_to_tainan_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "tainan",
            "dest": "tainan_restaurant2",
            "conditions": "is_going_to_tainan_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "tainan",
            "dest": "tainan_restaurant3",
            "conditions": "is_going_to_tainan_restaurant3",
        },
        {"trigger": "go_back", "source": ["start","breakfast","lunchdinner","snack","breakfast_restaurant1","breakfast_restaurant2","breakfast_restaurant3","breakfast_restaurant4","breakfast_restaurant5","breakfast_restaurant6",
         "western","japanese","korean","thai","healthy","tainan","snack_restaurant1","snack_restaurant2","snack_restaurant3","western_restaurant1","western_restaurant2","western_restaurant3","japanese_restaurant1","japanese_restaurant2","japanese_restaurant3",
         "korean_restaurant1","korean_restaurant2","korean_restaurant3","thai_restaurant1","thai_restaurant2","thai_restaurant3","healthy_restaurant1","healthy_restaurant2","healthy_restaurant3","tainan_restaurant1","tainan_restaurant2","tainan_restaurant3"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if event.message.text.lower() == 'fsm':
                send_image_message(event.reply_token,
                                   'https://nckubestrestaurant.herokuapp.com/show-fsm')
            elif machine.state != 'user' and event.message.text.lower() == 'restart':
                send_text_message(event.reply_token,"想了解成大周邊美食嗎? 輸入『start』來尋找成大周邊美食!")
                machine.go_back()
            else:
                send_text_message(event.reply_token,"想了解成大周邊美食嗎? 輸入『start』來尋找成大周邊美食!\n 輸入『restart』可以從頭開始")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
