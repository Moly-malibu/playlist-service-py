# https://github.com/mcrute/pydora
# https://github.com/mcrute/pydora/blob/master/tests/test_pandora/test_clientbuilder.py
# https://6xq.net/pandora-apidoc/json/partners/#partners
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/clientbuilder.py#L77-L114
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/transport.py#L27
# https://github.com/mcrute/pydora/blob/f6d1613deb7ec23d38b3d7d2c20b065f3457c8b8/pandora/errors.py

import os
import pprint
from dotenv import load_dotenv
import pydora # allows importing of the "pandora" sub-package
import pandora.clientbuilder as cb

pp = pprint.PrettyPrinter(indent=4)

load_dotenv()

PANDORA_USERNAME = os.environ.get("PANDORA_USERNAME", "OOPS")
PANDORA_PASSWORD = os.environ.get("PANDORA_PASSWORD", "OOPS")

client_settings = {
    "DECRYPTION_KEY": "R=U!LH$O2B#",
    "ENCRYPTION_KEY": "6#26FRL$ZWD",
    "PARTNER_USER": "android",
    "PARTNER_PASSWORD": "AC7IBG09A3DTSYM4R41UJWL07VLN8JI7",
    "DEVICE": "android-generic"
} # FYI: these are generic device settings not personal private info (see: https://6xq.net/pandora-apidoc/json/partners/#partners)
client = cb.SettingsDictBuilder(client_settings).build()
print("---------------------------")
print("CLIENT:", type(client)) #> <class 'pandora.client.APIClient'>
pp.pprint(dir(client))

print("---------------------------")
print("LOGGING IN...")
login_response = client.login(PANDORA_USERNAME, PANDORA_PASSWORD)
pp.pprint(login_response)

print("---------------------------")
print("GETTING BOOKMARKS...")
bookmarks_response = client.get_bookmarks()
print(type(bookmarks_response))
pp.pprint(dir(bookmarks_response))

print(f"FOUND {len(bookmarks_response.songs)} BOOKMARKS:")
for song in bookmarks_response.songs:
    song_info = {
        "title": song.song_name,
        "artist": song.artist_name,
        "album": song.album_name,
        "bookmarked_on": song.date_created.strftime("%Y-%m-%d")
    }
    pp.pprint(song_info)
