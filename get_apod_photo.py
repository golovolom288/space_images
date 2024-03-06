import requests, os
from urllib.parse import urlparse
from save_img import save_img


def get_url_apod_photo(count):
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        "api_key": nasa_token,
        "count": count
    }
    nasa_url = "https://api.nasa.gov/planetary/apod"
    nasa_apod_json = requests.get(nasa_url, params=params)
    nasa_apod_json.raise_for_status()
    apod_photo = nasa_apod_json.json()
    for count in range(len(apod_photo)):
        url_apod_photo = apod_photo[count]["url"]
        file_extension = os.path.splitext(urlparse(url_apod_photo).path)[1]
        save_img(url_apod_photo, f"images/apod_photo_{count+1}{file_extension}")


if __name__ == "__main__":
    get_url_apod_photo(input("Количество фотографий: "))
