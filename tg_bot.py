from dotenv import load_dotenv
import telegram
import os
import time
import random


def send_photo_tg_bot(directrory="images/"):
    load_dotenv()
    hours = int(os.environ["TG_TIME"])
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    photos = os.listdir(directrory)
    random.shuffle(photos)
    bot = telegram.Bot(token=tg_bot_token)
    chat_id = os.environ["TG_GROUP_ID"]
    while True:
        for photo in photos:
            photo_path = os.path.join(directrory, photo)
            with open(photo_path, "rb") as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(int(hours*3600))


if __name__ == "__main__":
    send_photo_tg_bot()