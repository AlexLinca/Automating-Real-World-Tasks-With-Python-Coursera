import PIL
from PIL import Image
import os

old_path = os.path.expanduser('~') + "/images/"
new_path = "/opt/icons/"
for file in os.listdir(old_path):
    if file.endswith(".tiff"):
        im = Image.open(file)
        im.rotate(270).resize((128,128)).convert("RGB").save(new_path+os.path.splitext(file)[0],".jpeg")
