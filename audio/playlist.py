class Playlist:
    def __init__(self, list_of_songs: list):
        self.current_song = list_of_songs[0]
        self.list_of_songs = list_of_songs

    def show_current(self) -> str:
        """ Return name and author of current song """
        return self.current_song

    def show_queue(self) -> str:
        """ Return a few songs after current """
        position = self.list_of_songs.index(self.current_song)
        if position != len(self.list_of_songs)-1:
            try:
                queue = self.list_of_songs[position+1:position+6]
            except IndexError:
                queue = self.list_of_songs[position+1:]
            queue = ' '.join(queue)
        else:
            queue = 'Is empty!'
        return queue

    def add(self, songs: list) -> None:
        """ Add another songs or song to current playlist """
        self.list_of_songs += songs

    def next_song(self) -> str | None:
        """ Changes current song to next, returns it """
        position = self.list_of_songs.index(self.current_song)
        try:
            self.current_song = self.list_of_songs[position+1]
        except IndexError:
            return None
        return self.current_song

    def previous_song(self) -> str | None:
        """ Changes current song to prev, returns it """
        position = self.list_of_songs.index(self.current_song)
        try:
            self.current_song = self.list_of_songs[position-1]
        except IndexError:
            return None
        return self.current_song
