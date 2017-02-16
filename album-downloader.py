#! /usr/bin/env python

import os
import re
import sys
import threading

import progressbar
import requests

from imgurpython import ImgurClient

regex = re.compile(r'\.(\w+)$')
def get_extension(link):
    ext = regex.search(link).group()

    return ext

lock = threading.Lock()

i = 1
def download_img(img):
    global i, bar

    file_ext = get_extension(img.link)
    resp = requests.get(img.link, stream=True)

    # create unique name by combining file id with its extension
    file_name = img.id + file_ext

    with open(file_name, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            f.write(chunk)

    with lock:
        bar.update(i)
        i += 1

try:
    album_id = sys.argv[1]
except IndexError:
    raise Exception('Please specify an album id')

client_id = os.getenv('IMGUR_CLIENT_ID')
client_secret = os.getenv('IMGUR_CLIENT_SECRET')

client = ImgurClient(client_id, client_secret)

img_lst = client.get_album_images(album_id)
bar = progressbar.ProgressBar(max_value=len(img_lst))

threads = []
for img in img_lst:
    t = threading.Thread(target=download_img, args=(img,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()


