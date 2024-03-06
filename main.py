from dotenv import load_dotenv
from save_img import save_img
from fetch_spacex_images import fetch_spacex_last_launch
from get_apod_photo import get_url_apod_photo
from get_epic_photo import get_epic_photo
from tg_bot import send_photo_tg_bot
import argparse


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    filename = 'images/hubble.jpeg'
    url_hubble = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    save_img(url_hubble, filename)
    fetch_spacex_last_launch()
    get_epic_photo()
    get_url_apod_photo(input("Введите количество картинок: "))
    send_photo_tg_bot(directory="images/")


