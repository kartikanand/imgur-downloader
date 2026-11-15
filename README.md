# imgur-downloader

A Python script that downloads every image in an Imgur album. Images are fetched in parallel threads, with a progress bar.

## Setup

```sh
pip install -r requirements.txt
export IMGUR_CLIENT_ID=<your client id>
export IMGUR_CLIENT_SECRET=<your client secret>
```

Register an application at https://api.imgur.com/oauth2/addclient to get the credentials.

## Usage

```sh
python album-downloader.py <album_id>
```

The album ID is the last part of the album URL (`imgur.com/a/<album_id>`). Images are saved to the current directory as `<image_id>.<ext>`.
