# encoding: utf-8

from schoolbot.cogs.help import HelpCog
from schoolbot.cogs.system import SystemCog
from schoolbot.cogs.school import SchoolCog
from schoolbot.cogs.errors import ErrorCog
from schoolbot.helpers import config

from discord.ext import commands


def main():
    bot = commands.Bot(command_prefix=['!'])

    server_ids = [664105827069591602]

    bot.add_cog(SchoolCog(bot))
    bot.add_cog(SystemCog(bot))
    bot.add_cog(HelpCog(bot))
    bot.add_cog(ErrorCog(bot))
    bot.run(config["token"])


if __name__ == '__main__':
    main()
