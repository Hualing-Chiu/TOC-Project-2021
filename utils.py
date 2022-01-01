import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, URITemplateAction, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
menu = 0

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        type='image',
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def send_restaurant_info(reply_token, image_url, info_url, map_url, menu_url):
    global menu
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='餐廳資訊',
            text='點擊看介紹、地圖、更多推薦!',
            thumbnail_image_url=image_url,
            actions=[
                URITemplateAction(
                    label='介紹',
                    uri = info_url
                ), URITemplateAction(
                    label='菜單',
                    uri = menu_url
                ), URITemplateAction(
                    label='地圖',
                    uri = map_url
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='用餐時段',
            text='點擊選擇想用餐的時段',
            thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2020/04/Da-Tung-Food-Banner-e1588216225724.jpg',
            actions=[
                MessageTemplateAction(
                    label='早餐',
                    text='breakfast'
                ),
                MessageTemplateAction(
                    label='午餐/晚餐',
                    text='lunchdinner'
                ),
                MessageTemplateAction(
                    label='宵夜',
                    text='snack'
                )
            ]
        )
    )
    line_bot_api.push_message(id, buttons_template)

    return "OK"

def send_breakfast(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='早餐',
                    text='點擊看餐廳介紹',
                    thumbnail_image_url='https://cc.tvbs.com.tw/img/program/_data/i/upload/2019/12/02/20191202180950-569b8e0f-me.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='少爺蛋餅',
                            text='breakfast_restaurant1'
                        ),
                        MessageTemplateAction(
                            label='緹克廚房',
                            text='breakfast_restaurant2'
                        ),
                        MessageTemplateAction(
                            label='六吋盤',
                            text='breakfast_restaurant3'
                        )
                    ]
                ),
                CarouselColumn(
                    title='早餐',
                    text='點擊看餐廳介紹',
                    thumbnail_image_url='https://cc.tvbs.com.tw/img/program/_data/i/upload/2019/12/02/20191202180950-569b8e0f-me.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='良辰吉食',
                            text='breakfast_restaurant4'
                        ),
                        MessageTemplateAction(
                            label='海鷗牌餐飲城',
                            text='breakfast_restaurant5'
                        ),
                        MessageTemplateAction(
                            label='謝家飯糰',
                            text='breakfast_restaurant6'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_restaurant_type(reply_token,id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img.tiffany0118.com/uploads/20200303002842_52.jpg',
                    title='餐廳推薦',
                    text='點擊選擇餐廳類型',
                    actions=[
                        MessageTemplateAction(
                            label='西式',
                            text='western'
                        ),
                        MessageTemplateAction(
                            label='日式',
                            text='japanese'
                        ),
                        MessageTemplateAction(
                            label='韓式',
                            text='korean'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/TU6ESPm.jpg',
                    title='餐廳推薦',
                    text='點擊選擇餐廳類型',
                    actions=[
                        MessageTemplateAction(
                            label='泰式',
                            text='thai'
                        ),
                        MessageTemplateAction(
                            label='水煮健康餐',
                            text='healthy'
                        ),
                        MessageTemplateAction(
                            label='排隊美食',
                            text='tainan'
                        ),
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token,message)

    return "OK"

def send_snack(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='宵夜',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://gwan.tw/wp-content/uploads/20190310174718_54.jpg',
            actions=[
                MessageTemplateAction(
                    label='一點刈包',
                    text='snack_restaurant1'
                ),
                MessageTemplateAction(
                    label='咕嚕叫土司',
                    text='snack_restaurant2'
                ),
                MessageTemplateAction(
                    label='紅記早點',
                    text='snack_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_western(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='西式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/mupVQCY.jpg',
            actions=[
                MessageTemplateAction(
                    label='V餐館',
                    text='western_restaurant1'
                ),
                MessageTemplateAction(
                    label='庫肯花園餐廳',
                    text='western_restaurant2'
                ),
                MessageTemplateAction(
                    label='Is義式餐廳',
                    text='western_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_japanese(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='日式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2019/12/F1.jpg',
            actions=[
                MessageTemplateAction(
                    label='石火山碳燒蓋飯',
                    text='japanese_restaurant1'
                ),
                MessageTemplateAction(
                    label='井選日式定食',
                    text='japanese_restaurant2'
                ),
                MessageTemplateAction(
                    label='肉肉控',
                    text='japanese_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_korean(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='韓式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2020/03/C1.jpg',
            actions=[
                MessageTemplateAction(
                    label='歐巴不是阿啾喜',
                    text='korean_restaurant1'
                ),
                MessageTemplateAction(
                    label='大韓名鍋',
                    text='korean_restaurant2'
                ),
                MessageTemplateAction(
                    label='韓朝',
                    text='korean_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_thai(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='泰式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://hululu.tw/wp-content/uploads/20190103162941_48.jpg',
            actions=[
                MessageTemplateAction(
                    label='珍妮花與南洋杉',
                    text='thai_restaurant1'
                ),
                MessageTemplateAction(
                    label='BITCH小姐',
                    text='thai_restaurant2'
                ),
                MessageTemplateAction(
                    label='Nest de 后院泰式餐廳',
                    text='thai_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_healthy(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='水煮健康餐',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.6435-9/50466375_800215856987428_4821153458943950848_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=e3f864&_nc_ohc=QkpHpJcUAlUAX8Byb1s&_nc_ht=scontent.fkhh1-2.fna&oh=00_AT-A9mkY6008CIAt9bC4WXocl8mjc6QB2FkNxpomnUaGrw&oe=61F5F942',
            actions=[
                MessageTemplateAction(
                    label='就4水煮餐',
                    text='healthy_restaurant1'
                ),
                MessageTemplateAction(
                    label='大口咬定',
                    text='healthy_restaurant2'
                ),
                MessageTemplateAction(
                    label='輕水煮 x Light Food',
                    text='healthy_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_tainan(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='排隊美食',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://cc.tvbs.com.tw/img/program/upload/2018/10/09/20181009212526-e8f06146.jpg',
            actions=[
                MessageTemplateAction(
                    label='雙生綠豆沙',
                    text='tainan_restaurant1'
                ),
                MessageTemplateAction(
                    label='文章牛肉湯',
                    text='tainan_restaurant2'
                ),
                MessageTemplateAction(
                    label='王氏魚皮',
                    text='tainan_restaurant3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"
"""
def send_image_url(id, img_url):
    pass
def send_button_message(id, text, buttons):
    pass
"""
