import hashlib, io, requests, pandas as pd
from pathlib import Path
from PIL import Image

def save_images(results, name):
    for b in results:
        image_content = requests.get(b).content
        image = Image.open(io.BytesIO(image_content))
        image.save(f"images/{name}_{hashlib.md5(image_content).hexdigest()}.jpg")
