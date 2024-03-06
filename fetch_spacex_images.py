import requests
from save_img import save_img


def fetch_spacex_last_launch():
    spacex = requests.get("https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a")
    urlssx = spacex.json()["links"]["flickr"]["original"]
    for count, urlsx in enumerate(urlssx, start=1):
        filepath = f"images/spacex_{count}.jpg"
        save_img(urlsx, filepath)


if __name__ == "__main__":
    fetch_spacex_last_launch()