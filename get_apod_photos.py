import requests
from urllib.parse import urlparse
from save_img import save_img
import argparse
from dotenv import load_dotenv
import os


def get_apod_photos(nasa_token, count):
    params = {
        "api_key": nasa_token,
        "count": count
    }
    nasa_url = "https://api.nasa.gov/planetary/apod"
    nasa_apod_response = requests.get(nasa_url, params=params)
    nasa_apod_response.raise_for_status()
    apod_photos = nasa_apod_response.json()
    for count, apod_photo in enumerate(apod_photos):
        apod_photo_url = apod_photo["url"]
        file_extension = os.path.splitext(urlparse(apod_photo_url).path)[1]
        save_img(apod_photo_url, f"images/apod_photo_{count + 1}{file_extension}")


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser()
    parser.add_argument("--count_photos", type=int)
    args = parser.parse_args()
    count_photos = args.count_photos
    get_apod_photos(nasa_token, count_photos)
