import datetime
import json

import discord


def time_to_emoji(time: str):
    parts = time.split(":")
    hour = int(parts[0])
    minute = int(parts[1])

    if minute < 15:
        minute = ""
    elif minute < 45:
        minute = 30
    else:
        minute = ""
        hour = hour + 1
    if hour > 12:
        hour = hour - 12
    return f":clock{hour}{minute}:"


def get_next_datetime(time: datetime.time):
    time = time.replace(second=0)
    now = datetime.datetime.now()
    if datetime.datetime.now().time() > time:
        date = now.replace(day=now.day + 1)
    else:
        date = now
    return date.replace(hour=time.hour, second=time.second, minute=time.minute,
                        microsecond=time.microsecond)


def first_char_cap(string):
    new_string = ""
    capital = False
    for letter in string:
        if not capital:
            new_string += letter.capitalize()
            capital = True
        else:
            new_string += letter
    return new_string


def get_pre_mention(ctx, message):
    if isinstance(ctx.channel, discord.DMChannel):
        pre = ""
    else:
        pre = f"{ctx.author.mention}, "
    return first_char_cap(f"{pre}{message}")


class Config:
    """
    Don't ask me why i wanted to use a class for this lol
    """

    def __init__(self):
        self.data = {}
        self.read_file()

    def __getitem__(self, item):
        return self.data[item]

    def read_file(self):
        with open("data/config.json", "r") as file:
            self.data = json.loads(file.read())


config = Config()
