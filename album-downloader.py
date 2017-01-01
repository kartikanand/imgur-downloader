#! /usr/bin/env python

import os
import re
import sys

import requests

from imgurpython import ImgurClient

regex = re.compile(r'\.(\w+)$')
def get_extension(link):
    ext = regex.search(link).group()

    return ext


try:
    album_id = sys.argv[1]
except IndexError:
    raise Exception('Please specify an album id')

client_id = os.getenv('IMGUR_CLIENT_ID')
client_secret = os.getenv('IMGUR_CLIENT_SECRET')

client = ImgurClient(client_id, client_secret)

img_lst = client.get_album_images(album_id)

for i in img_lst:
    file_ext = get_extension(i.link)
    resp = requests.get(i.link, stream=True)

    # create unique name by combining file id with its extension
    file_name = i.id + file_ext

    with open(file_name, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            f.write(chunk)


