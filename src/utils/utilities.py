from PIL import Image
import os
import requests

current_dir = os.getcwd()
os.chdir(current_dir + "/../")


def dir_check(dir_location):
    isExist = os.path.exists(dir_location)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir_location)
        print("The new directory is created!")
    else:
        print("directory already exists!")


def load_image(img_url):
    try:
        response = requests.get(img_url, stream=True, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            return Image.open(response.raw)
        print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    return None
