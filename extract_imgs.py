import io, requests
from pathlib import Path
from PIL import Image

def save_images(results, name):
    number = 1
    for b in results:
        image_content = requests.get(b).content
        image = Image.open(io.BytesIO(image_content))
        image.save(f"images/{name}_{number}.jpg")
        number += 1
