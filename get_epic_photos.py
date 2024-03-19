import requests, os
from save_img import save_img
import argparse
from dotenv import load_dotenv



def get_epic_photos(count_photos, token):
    params = {
        "api_key": token,
    }
    nasa_url = "https://api.nasa.gov/EPIC/api/natural/images"
    nasa_epic_response = requests.get(nasa_url, params=params)
    nasa_epic_response.raise_for_status()
    epic_photos = nasa_epic_response.json()[:count_photos]
    for image in epic_photos:
        img_name = image["image"]
        img_date = image["date"].split()[0]
        img_date = img_date.replace("-", "/")
        epic_photo_url = f"https://api.nasa.gov/EPIC/archive/natural/{img_date}/png/{img_name}.png"
        file_name = f"images/epic_photo_{img_name}.png"
        save_img(epic_photo_url, file_name, token)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser(description="Принимает количество нужных фотографий")
    parser.add_argument("--count_photos_epic", help="Число апод фотографий ", type=int)
    args = parser.parse_args()
    count_photos_epic = args.count_photos_epic
    get_epic_photos(count_photos_epic, nasa_token)