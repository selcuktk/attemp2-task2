from PIL import Image
import os
import requests

current_dir = os.getcwd()
os.chdir(current_dir + "/../")


def load_image(img_url):
    try:
        response = requests.get(img_url, stream=True, headers={
                                "User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            return Image.open(response.raw)
        print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    return None
