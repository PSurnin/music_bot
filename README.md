This discord bot plays music from
- Spotify
- Youtube

### How to connect to spotify:
1. Open your account dashboard https://developer.spotify.com/dashboard
2. Create an app
3. Take name of artist and track with API and send it to yt-dlp

Spotify API is needed to connect and extract data for artis name and track name
Since Spotify doesn't allow to stream music from them directly - this bot uses youtube with Artis-Track names

### Usage

To use this bot you should crete a .env file with these values
- `SPOTIPY_CLIENT_ID='example_id'`
- `SPOTIPY_CLIENT_SECRET='example_secret'`
- `BOT_TOKEN = 'example_token'`

And then just launch `python3 main.py`

### List of commands:
- _play_ : play a link or song name, adds it to queue
- _stop_ : disconnects bot from channel and erases playlist
- _pause_ : stops music
- _resume_: resumes music
- _next_: skips current song
- _queue_: shows next few songs in a playlist