import random

from discord.ext import commands, tasks

from schoolbot.database import tests_collection
from schoolbot.helpers import time_to_emoji, config
if config["iserv"]["fake"]:
    from iservscrapping.fake import FakeIserv as Iserv
else:
    from iservscrapping import Iserv

from schoolbot.language import _
iserv_cfg = config["iserv"]
iserv = Iserv(iserv_cfg["url"], iserv_cfg["username"], iserv_cfg["password"], cache=False)


class SchoolCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass
        self.check_tests.start()
        self.auto_plan.start()

    @commands.command()
    async def get_tests(self, ctx):
        iserv.login()
        tests = iserv.get_next_tests()
        text = _(":newspaper: **Tests**\n\n")
        for test in tests:
            text = text + f"**{test['date']}**\n:point_right: {test['subject']},\n"
        await ctx.send(text)

    async def plan_function(self, class_="9f", day=1):
        print(type(day))
        print(day)

        if day == 1:
            url = config["plan"]["day1URL"]
            print("hi1")
        elif day == 2:
            url = config["plan"]["day2URL"]
            print("hi2")
        else:
            print("hi3")
            return _("Day must be either 1 or 2")
        plan, date, week = iserv.get_untis_substitution_plan(
            url)

        text = _(":newspaper: **Substitution Plan**   |   ")
        text = text + f":family: {class_}   |   " \
                      f":calendar: {week}   |   " \
                      f":calendar_spiral: {date}\n\n"
        if class_ in plan.keys():
            for item in plan[class_]:
                time_emoji = time_to_emoji(f"{random.randint(1, 12)}:{random.randint(0, 60)}")
                text = text + f"> {time_emoji} **{_('Lesson')} {item['time']}**\n" \
                              f"> :abc: {item['subject']}\n" \
                              f"> :green_square: {item['room']}\n" \
                              f"> :{random.choice(['man', 'woman'])}_teacher: {item['teacher']}\n" \
                              f"> :family: {item['course']}\n\n"
        else:
            text = text + "Nothing found."

        return text

    @commands.command()
    async def plan(self, ctx, class_="9f", day=1):
        text = await self.plan_function(class_=class_, day=day)
        await ctx.send(text)

    @tasks.loop(minutes=config["autoPlan"]["interval"])
    async def auto_plan(self):

        auto_plan_config = config["autoPlan"]
        channel = self.bot.get_channel(auto_plan_config["channel"])
        text = await self.plan_function(class_=auto_plan_config["class"],
                                        day=auto_plan_config["day"])
        await channel.send(text)

    @tasks.loop(minutes=config["autoTests"]["interval"])
    async def check_tests(self):
        iserv.login()
        current_tests = iserv.get_next_tests()
        last_tests = tests_collection.find()
        last_tests_formatted = [
            {
                'date': i['date'],
                'time': i['time'],
                'class': i['class'],
                'subject': i['subject']
            }
            for i in last_tests]

        for test in current_tests:
            if test not in last_tests_formatted:
                print("new!")
                subject = test["subject"]
                date = test["date"]
                time = test["time"]
                time_emoji = time_to_emoji(time)
                course = test["class"]
                text = f"> **:pencil: {_('New test announced!')} :pencil:**\n" \
                       f"> :abc: {subject}\n" \
                       f"> :calendar: {date}\n" \
                       f"> {time_emoji} {time}\n" \
                       f"> :family: {course}\n"
                await self.bot.get_channel(config["autoTests"]["channel"]).send(text)
                tests_collection.insert_one(test)
        for test in last_tests_formatted:
            if test not in current_tests:
                tests_collection.delete_one(test)
                print("deleted!")
