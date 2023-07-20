from api.spotify import track_info, playlist_info


def url_to_songs(url: str) -> str | None:
    if url is None:
        return None

    if "https://www.youtu" in url or "https://youtu.be" in url:
        return url

    if "https://open.spotify.com/track" in url:
        return track_info(url)

    if "https://open.spotify.com/playlist" in url or "https://open.spotify.com/album" in url:
        return playlist_info(url)

    # If no match
    return None
