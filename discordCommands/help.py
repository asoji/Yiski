import discord
from discord.ext import commands
from mainDiscord import botPrefix
from loguru import logger


class HelpDiscord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        yiskiHelpEmbed = discord.Embed(title="Yiski Help",
                                       description="Here's the commands you can use on Yiski. Note that the Discord version won't be well maintained, as Revolt is the primary goal for this bot.",
                                       color=0x00a86b)
        yiskiHelpEmbed.add_field(name="hello", value=f"- Hello Command\n- `{botPrefix}hello`")
        yiskiHelpEmbed.add_field(name="httpcat", value=f"- HTTP Cats go brrr\n- `{botPrefix}httpcat [http code]`")
        yiskiHelpEmbed.add_field(name="ghr",
                                 value=f"- Preview a GitHub Repo\n- `{botPrefix}ghr [username/orgname] [reponame]`")
        yiskiHelpEmbed.add_field(name="memoryleak",
                                 value=f"- Funni Memory Leak video go brrr\n- `{botPrefix}memoryleak`")
        yiskiHelpEmbed.add_field(name="gasp",
                                 value=f"- Just find out for yourself.\n- `{botPrefix}gasp`")
        yiskiHelpEmbed.add_field(name="token",
                                 value=f"- So about that funky config.toml...\n- `{botPrefix}token`")
        yiskiHelpEmbed.add_field(name="devtools",
                                 value=f"- Discord disabled devtools by default, here's how to get it back.\n- `{botPrefix}devtools`")

        yiskiHelpEmbed.set_footer(
            text="Bot writen by HiItsDevin_, powered by Py-cord, a Discord.py continuation of the original Discord.py library. Written with 💖!")

        await ctx.reply(embed=yiskiHelpEmbed)


def setup(client):
    client.add_cog(HelpDiscord(client))
    logger.debug("Help Cog loaded.")
