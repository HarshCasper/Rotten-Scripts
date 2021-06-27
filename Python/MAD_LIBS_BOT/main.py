import discord
import asyncio
import random
import os
from discord.ext import commands
from keep_alive import keep_alive


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True,intents=intents)
@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----")


@bot.event
async def on_command_error(ctx, error):
    # Ignore these errors
    if isinstance(error, commands.CommandOnCooldown):
        # If the command is currently on cooldown trip this
        m, s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if int(h) == 0 and int(m) == 0:
            await ctx.send(f" You must wait {int(s)} seconds to use this command!")
        elif int(h) == 0 and int(m) != 0:
            await ctx.send(
                f" You must wait {int(m)} minutes and {int(s)} seconds to use this command!"
            )
        else:
            await ctx.send(
                f" You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!"
            )
    else:
      embed = discord.Embed(color=0xE74C3C, 
          description=f"<:dnd:840490624670892063> | Error: `{error}`")
      await ctx.send(embed=embed)

@bot.command(name="ping")
async def ping(ctx):
  await ctx.send(f"Ping! {round(bot.latency * 1000)}")

@bot.command(name="!MAD_LIBS")
@commands.cooldown(1, 120, commands.BucketType.user)
async def input(ctx):
    await ctx.send("You have to answer some questions and I will Give you a fun phrase ")
    try:
        await ctx.send("Tell me a plural-noun")
        plural_noun = await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=10)
        plural_noun = plural_noun.content

        await ctx.send("Tell me  an adjective")
        adjective = await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        adjective = adjective.content

        await ctx.send("Tell me an animal name")
        animal = await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        animal = animal.content

        await ctx.send("Tell me a color")
        color= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        color = color.content

        await ctx.send("Tell me a noun")
        noun= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        noun = noun.content

        await ctx.send("Tell me a verb")
        verb= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        verb = verb.content

        await ctx.send("Tell me a song ")
        song_name= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        song_name = song_name.content

        await ctx.send("Tell me a funny number")
        funny_number= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        funny_number = funny_number.content

        await ctx.send("Tell me a celebrity name")
        celebrity_name= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        celebrity_name = celebrity_name.content

        await ctx.send("Tell me a color")
        color= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        color = color.content

        await ctx.send("send an character name")
        character= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        character = character.content

        await ctx.send("send an company name")
        company= await bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=30)
        company = company.content

        phrases=[f"Unicorns aren't like other `{plural_noun}` they're `{adjective}`.They look like `{animal}` ,with `{plural_noun}` for feet and a `{adjective}` mane of hair.But unicorns are `{color}`  and have a `{adjective}` `{noun}` on their heads.Some `{plural_noun}` don't believe uniorns are `{adjective}` but I believe in them. I would love to `{verb}` a unicorn to faraway `{plural_noun}`. One thing I've always `{adjective}` about is whether unicorns `{verb}` rainbows, or is their `{noun}` `{adjective}` like any other animal's?" ,f"Hello everyone my name is `{song_name}`.I'm going to be talking about `{funny_number}`.now what is a `{celebrity_name}`, It is the most important `{animal}` that runs on a `{character}` which manages all the `{color}` memory and provessors,as well as its `{plural_noun}` and `{celebrity_name}` allows you to `{funny_number}` with a computer without knowing how to `{company}` the computer `{song_name}` without a `{animal}`, a `{celebrity_name}` is useless ."]

        #await ctx.send(f"{random.choice(phrases)}")
        embed = discord.Embed(title="An Random funny Story", description=random.choice(phrases), color=0x1ABC9C)
        embed.set_footer(text=f"An Story made by {ctx.author.display_name}")
        await ctx.send(embed=embed)
    except asyncio.TimeoutError:
        await ctx.send("welll TimeoutError")

keep_alive()
bot.run('TOKEN') #replace this token with yours 
