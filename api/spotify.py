import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def track_info(url: str) -> str:
    results = client.track(url)
    return f"{results['artists'][0]['name']} {results['name']}"


def playlist_info(url: str) -> list:
    results = client.playlist_items(url, fields='items(track(artists, name))')
    r = [f"{res['track']['artists'][0]['name']} {res['track']['name']}" for res in results['items']]
    return r
