from discord.ext import commands


class FunDiscord(commands.Cog):  # this defines what "class" things will be in, can be completely custom, ie Util, Admin, etc.
    def __init__(self, client):
        self.client = client

    @commands.command()  # says its a command
    async def hello(self, ctx):  # self always needs to be before ctx in cogs
        await ctx.send("howdy nerd", mention_author=True)


def setup(client):  # actually register the command
    client.add_cog(FunDiscord(client))  # add the cog, you need to use the same thing in the cog as the class above