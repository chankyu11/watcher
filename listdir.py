import os
import cv2
from PIL import Image

file_path = "D:/googleImageDownloader-master/images/person/"

for m in os.listdir(file_path):
    im = Image.open(file_path + "/" +m)
    # print(im.size)
    re = im.resize((224,224))
    re.save(m)