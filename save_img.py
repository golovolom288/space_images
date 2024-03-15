import requests, os


def save_img(url, filepath, api_key=""):
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs("images", exist_ok=True)
    with open(filepath, 'wb') as file:
        file.write(response.content)





