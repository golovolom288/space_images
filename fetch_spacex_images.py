import requests
from save_img import save_img


def fetch_spacex_last_launches(id):
    spacex_response = requests.get(f"https://api.spacexdata.com/v4/launches/{id}")
    spacex_response.raise_for_status()
    photo_urls = spacex_response.json()["links"]["flickr"]["original"]
    for count, photo_url in enumerate(photo_urls, start=1):
        filepath = f"images/spacex_{count}.jpg"
        save_img(photo_url, filepath)


if __name__ == "__main__":
    fetch_spacex_last_launches(id="5eb87d47ffd86e000604b38a")