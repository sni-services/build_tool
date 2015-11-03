import requests
import wget
import os
from clint.textui import progress

url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'

# filename = wget.download(url)
#
# print filename
#
# os.unlink("razorback.mp3")

r = requests.get(url, stream=True)
with open("razorback.mp3", 'wb') as f:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()
