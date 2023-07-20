from __future__ import annotations

from api.youtube import YTDLSource


class MusicController:
    """
    Class to perform bot actions on separate discord guild instances
    """
    def __init__(self, ctx, bot):
        self.bot = bot
        self.ctx = ctx
        self.playlist = None

    async def play(self):
        """ Plays current song with YTDL by its name or youtube link"""
        async with self.ctx.typing():
            player = await YTDLSource.from_url(self.playlist.show_current(), loop=self.bot.loop)
            self.ctx.voice_client.play(player, after=lambda e: self.next_song(e))
        await self.ctx.send(f'Now playing: {player.title}')

    def next_song(self, error):
        """Invoked after a song is finished. Plays the next song if there is one."""
        next_song = None
        if not self.ctx.voice_client.is_playing():
            next_song = self.playlist.next_song()
        if next_song is None:
            return
        self.bot.loop.create_task(self.play())
