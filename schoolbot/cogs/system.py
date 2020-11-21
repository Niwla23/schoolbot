from discord.ext import commands

from schoolbot.helpers import config
from schoolbot.language import _

if config["iserv"]["fake"]:
    from iservscrapping.fake import FakeIserv as Iserv
else:
    from iservscrapping import Iserv
import datetime

iserv_cfg = config["iserv"]
iserv = Iserv(iserv_cfg["url"], iserv_cfg["username"], iserv_cfg["password"], cache=False)


class SystemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(_("Pong!"))

    @commands.command()
    async def iserv_speedtest(self, ctx):
        message = await ctx.send("Testing login speed....")
        start_time = datetime.datetime.now()
        iserv.login()
        duration = datetime.datetime.now() - start_time
        await message.edit(
            content=_("Logging into iserv took {seconds}.{microseconds} seconds.").format(
                seconds=duration.seconds,
                microseconds=duration.microseconds))
