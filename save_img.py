import requests, os


def save_img(url, filepath):
    response = requests.get(url)
    response.raise_for_status()
    if not os.path.exists("images"):
        os.mkdir("images")
    with open(filepath, 'wb') as file:
        file.write(response.content)





