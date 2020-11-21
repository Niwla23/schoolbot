from discord.ext import commands

from schoolbot.helpers import get_pre_mention
from schoolbot.language import _


class ErrorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        err = getattr(error, "original", error)

        if isinstance(err, commands.CommandNotFound):
            await ctx.send(get_pre_mention(ctx, "dieses Kommando existiert nicht!"), delete_after=5)
        elif isinstance(err, commands.CommandOnCooldown):
            await ctx.send(
                'Dieses Kommando hat einen Cooldown. Versuche es nochmal in {:.2f} Sekunden!'.format(
                    error.retry_after))
        elif isinstance(err, commands.NoPrivateMessage):
            await ctx.send(get_pre_mention(ctx, _("command can not be used in DMs")),
                           delete_after=5)
        elif isinstance(err, commands.errors.MissingRequiredArgument):
            await ctx.send(
                get_pre_mention(ctx, _("the argument {0} is missing").format(
                    err.args[0].split(" ")[0])))
        elif isinstance(err, commands.errors.MissingPermissions):
            await ctx.send(
                get_pre_mention(ctx, _("you are missing these permissions: {0}").format(
                    ", ".join(err.missing_perms))))
        elif isinstance(err, commands.errors.MissingRole):
            await ctx.send(
                get_pre_mention(ctx, _("you are missing these permissions: {0}").format(
                    err.missing_role)))
        elif isinstance(err, commands.errors.BadArgument):
            await ctx.send(get_pre_mention(ctx, _("the argument {0} must be of type {1}")
                                           .format(err.args[0].split(" ")[-1][:-1],
                                                   err.args[0].split(" ")[2])))
        else:
            await ctx.send(_("an error occurred"))
            raise error
