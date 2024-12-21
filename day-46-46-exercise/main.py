import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import pprint
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
URI = "http://example.com"

billboard_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

travel_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{travel_year}"
YYYY = travel_year[:4]
billboard_response = requests.get(url=URL, headers=billboard_header)
billboard_response.raise_for_status()
html_text = billboard_response.text

soup = BeautifulSoup(html_text, "html.parser")
titles = soup.select("#title-of-a-story.c-title.a-no-trucate")
titles_text = [title.getText().strip() for title in titles]
print(titles_text)
scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=URI,
        show_dialog=True,
        cache_path=".cache")
)
user_id = sp.current_user()["id"]
track_spotify_uri = []

for query in titles_text:
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = f"track: {query} year: {YYYY}"
    result = sp.search(search_str, type="track")
    pprint.pprint(result)
    try:
        get_the_uri = result["tracks"]["items"][0]["uri"]
        track_spotify_uri.append(get_the_uri)
        print("done")
    except IndexError:
        print(f"{query} doesn't exist in Spotify. Skipped.")

print(track_spotify_uri)
create_playlist = sp.user_playlist_create(user=user_id, name=f"{YYYY}-MM-DD Billboard 100", public=False)
playlist_id = create_playlist["id"]
add_to_playlist = sp.playlist_add_items(playlist_id=playlist_id, items=track_spotify_uri)
