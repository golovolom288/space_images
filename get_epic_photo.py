import requests, os
from save_img import save_img

def get_epic_photo():
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        "api_key": nasa_token,
    }
    nasa_url = "https://api.nasa.gov/EPIC/api/natural/images"
    nasa_epic_json = requests.get(nasa_url, params=params)
    nasa_epic_json.raise_for_status()
    epic_photos = nasa_epic_json.json()[:5]
    for image in epic_photos:
        img_name = image["image"]
        img_date = image["date"].split()[0]
        img_date = img_date.replace("-", "/")
        url_epic_photo = f"https://api.nasa.gov/EPIC/archive/natural/{img_date}/png/{img_name}.png?api_key={nasa_token}"
        file_name = f"images/epic_photo_{img_name}.png"
        save_img(url_epic_photo, file_name)


if __name__ == "__main__":
    get_epic_photo()