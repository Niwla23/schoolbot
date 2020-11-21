# encoding: utf-8
from discord.ext import commands
import discord


class HelpCommand(commands.MinimalHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        self.commands_heading = "Befehle:"
        self.no_category = "Sonstiges:"
        self.command_attrs = {"name": "help", "aliases": ["hilfe"]}

    def get_opening_note(self):
        """Returns help command's opening note. Overriding to have it in german.
        """
        command_name = self.invoked_with
        return "Benutze `{0}{1} [command]` für genauere Hilfe zu einem Befehl.\n" \
               "Du kannst auch `{0}{1} [category]` benutzen um Hilfe für eine Kategorie zu bekommen.".format(
            self.clean_prefix,
            command_name)

    def get_ending_note(self):
        """Returns help command's ending note. This is mainly useful to override for i18n purposes."""
        return "Viel Spaß mit dem Bot!.\n" \
               "Programmiert von: Niwla23 (Alwin Lohrie)"

    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = HelpCommand()
        bot.help_command.cog = self
        self.bot = bot

    def cog_unload(self):
        self.bot.help_command = self._original_help_command
