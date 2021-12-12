import defectio
from defectio import ext
from defectio.ext import commands


class FunRevolt(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @defectio.ext.commands.command()
    async def ghr(self, ctx, name: str, repo: str):
        await ctx.reply(
            "[Here you go. If nothing shows up, then it's an invalid repo.](https://github.com/" + name + "/" + repo + ")",
            mention=True)


def setup(bot: defectio.ext.commands.Bot):  # actually register the command
    bot.add_cog(FunRevolt(bot))
