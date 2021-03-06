import defectio
from defectio import ext
from defectio.ext import commands
from loguru import logger

from mainRevolt import botPrefix


class HelpRevolt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.reply(
            "| Command Name    | Description                         | Command                                         |\n" +
            "|-----------------| ------------------------------------|-------------------------------------------------|\n" +
            f"| **hello**      | Hello Command                       | {botPrefix}hello                            |\n" +
            f"| **httpcat**    | HTTP Cats go brrr                   | {botPrefix}httpcat [http code]              |\n" +
            f"| **ghr**        | Preview a Github Repo               | {botPrefix}ghr [username/orgname] [reponame]|\n" +
            f"| **memoryleak** | SEGFAULT moment.                    | {botPrefix}memoryleak                       |\n" +
            f"| **gasp**       | Just find out for yourself.         | {botPrefix}gasp                             |\n" +
            f"| **token**      | So about that funky config.toml... | {botPrefix}token                            |\n\n" +
            "Bot writen by **HiItsDevin_**, powered by **[defectio](https://github.com/Darkflame72/defectio)**, a Revolt Python bot library. Written with 💖!",
            mention=True)


def setup(bot):
    bot.add_cog(HelpRevolt(bot))
    logger.debug("Help Cog loaded.")
