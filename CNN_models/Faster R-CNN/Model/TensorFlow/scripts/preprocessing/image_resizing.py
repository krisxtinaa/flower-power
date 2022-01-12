from PIL import Image
import os

path = r'C:\Users\Philip Vangelov\PycharmProjects\pythonProject\TensorFlow\workspace\training_demo\images\flowers\Brown Knapweed\\'
dirs = os.listdir(path)

for item in dirs:
    if os.path.isfile(path + item):
        im = Image.open(path + item)
        f, e = os.path.splitext(path + item)
        imResize = im.resize((800, 600), Image.ANTIALIAS)
        imResize.save(f + '.jpg', 'JPEG', quality=90)

