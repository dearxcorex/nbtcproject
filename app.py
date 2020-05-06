from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from config import  Channel_access_token,Channel_secret
from SyncFirebase.sync_database import air_frq
app = Flask(__name__)

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #input and pasing data
    REPLY_TOKEN = event.reply_token
    MESSAGE_FROM_USER = event.message.text
    UID = event.source.user_id

    if MESSAGE_FROM_USER:
        air_frq(float(MESSAGE_FROM_USER))
        line_bot_api.reply_message(REPLY_TOKEN,TextSendMessage("กรมสื่อสารทหารอากาศ"))














if __name__ == "__main__":
    app.run(port=8080,debug=True)





