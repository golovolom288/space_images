from dotenv import load_dotenv
from save_img import save_img
from fetch_spacex_images import fetch_spacex_last_launches
from get_apod_photos import get_apod_photos
from get_epic_photos import get_epic_photos
from tg_bot import send_photos_tg_bot
import argparse
import os


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    hours = int(os.environ["TG_TIME"])
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    chat_id = os.environ["TG_GROUP_ID"]
    parser = argparse.ArgumentParser(description="Принимает количество нужных фотографий")
    parser.add_argument("--count_photo_apod", "-cpa", help="Число апод фотографий ", type=int)
    parser.add_argument("--count_photo_epic", "-cpe", help="Число эпик фотографий ", type=int)
    args = parser.parse_args()
    count_photos_apod = args.count_photo_apod
    count_photos_epic = args.count_photo_epic
    fetch_spacex_last_launches()
    get_epic_photos(count_photos_epic, nasa_token)
    get_apod_photos(count_photos_apod, nasa_token)
    send_photos_tg_bot(hours, tg_bot_token, chat_id, directory="images/")


