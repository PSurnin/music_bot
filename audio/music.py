from typing import Dict

import discord
from discord.ext import commands

import audio.configs as config
from audio.controller import MusicController
from audio.playlist import Playlist
from audio.utils import url_to_songs

_controllers: Dict[str, MusicController] = {}
_playlists: Dict[str, Playlist] = {}


class MusicCommands(commands.Cog):
    def __init__(self, bot_instance: commands.Bot):
        self.bot = bot_instance

    @commands.command(description=config.PLAY_DESC, help=config.PLAY_HELP)
    async def play(self, ctx, *, url):
        """ Creates controller and playlist for each guild and streams music """
        if ctx.guild in _controllers:
            controller = _controllers[ctx.guild]
        else:
            controller = MusicController(ctx, bot)
            _controllers[ctx.guild] = controller

        songs = url_to_songs(url)
        if isinstance(songs, str):
            songs = [songs]

        if ctx.guild in _playlists:
            playlist = _playlists[ctx.guild]
            playlist.add(songs)
        else:
            controller.playlist = _playlists[ctx.guild] = Playlist(songs)
            await controller.play()

    @commands.command(description=config.STOP_DESC, help=config.STOP_HELP)
    async def stop(self, ctx):
        """ Stops and disconnects the bot from voice """
        # TODO: fix bug - after calling this command - MusicController.next_song is called
        if ctx.guild in _playlists:
            del _playlists[ctx.guild]
        if ctx.guild in _controllers:
            del _controllers[ctx.guild]
        await ctx.voice_client.disconnect()

    @commands.command(description=config.PAUSE_DESC, help=config.PAUSE_HELP)
    async def pause(self, ctx):
        """ Pause music with discord methods """
        if ctx.voice_client is None or not ctx.voice_client.is_playing():
            return
        ctx.voice_client.pause()
        await ctx.send("Playback Paused :pause_button:")

    @commands.command(description=config.RESUME_DESC, help=config.RESUME_HELP)
    async def resume(self, ctx):
        """ Resume music with discord methods """
        if ctx.voice_client is None or ctx.voice_client.is_playing():
            return
        ctx.voice_client.resume()
        await ctx.send("Resumed playback :arrow_forward:")

    # PLAYLIST SECTION
    @commands.command(description=config.NEXT_DESC, help=config.NEXT_HELP)
    async def next(self, ctx):
        """ Skip current song """
        if ctx.voice_client is None or not ctx.voice_client.is_playing():
            return
        await ctx.voice_client.stop()
        await ctx.send("Skipped")

    @commands.command(description=config.QUEUE_DESC, help=config.QUEUE_HELP)
    async def queue(self, ctx):
        """ Show 5 or all songs after current one """
        if ctx.voice_client is None:
            return
        if ctx.guild in _playlists:
            playlist = _playlists[ctx.guild]
            queue = playlist.show_queue()
            await ctx.send(queue)
        else:
            await ctx.send('Is empty')

    # CHECKS SECTION
    @play.before_invoke
    async def ensure_voice(self, ctx):
        """ Check voice channel connection before taking commands """
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Relatively simple music bot example',
    intents=intents,
)


@bot.event
async def on_ready():
    """ Start message for console """
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
