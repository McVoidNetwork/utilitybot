import discord
from discord.ext import commands

class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
def setup(bot):
    bot.add_cog(Hypixel(bot))
    bot.logger.info('$GREENLoaded $BLUE"hypixel" $GREENcog!')