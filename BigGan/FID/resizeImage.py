import os
from PIL import Image

source_imgs_dir='./FID/realImage2048/'
target_imgs_dir='./FID/resizedRealImage2048/'
print(target_imgs_dir)
for file in os.listdir(source_imgs_dir):
    # print(file)
    try:
        im = Image.open(source_imgs_dir + file)
        rgb_im = im.convert('RGB')
        out = rgb_im.resize((128, 128), Image.ANTIALIAS)
        out.save(target_imgs_dir + file)
    except:
        continue
