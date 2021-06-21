from discord.ext import commands
from datetime import datetime
import json
import discord

with open("package.json", "r") as f:
    data = json.load(f)
PREFIX = data["prefix"]
TOKEN = data["token"]
f.close()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(f"{PREFIX}"))
bot.launch_time = datetime.utcnow()


@bot.event
async def on_ready():
    print(f"Logged In as {bot.user}\n ID: {bot.user.id}")


@bot.event
async def on_connect():
    print("Connected to discord api\n Please wait for the bot to be ready!")


@commands.bot_has_guild_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
@commands.guild_only()
@bot.command()
async def softban(ctx, member: discord.Member, *, reason=None):
    if ctx.author == member:
        await ctx.send(f"You Can't do that", delete_after=5)
        return
    if (
        member.guild_permissions.administrator
        or member.guild_permissions.kick_members
        or member.guild_permissions.kick_members
    ):
        await ctx.send(
            f"That User is a Administrator/Moderator so i cant {ctx.command.name} that user",
            delete_after=7,
        )
        return
    if ctx.guild.me.top_role.position < member.top_role.position:
        await ctx.send(
            f"My Role Is Not High Enough To {ctx.command.name} This User",
            delete_after=7,
        )
        return
    if not reason:
        reason = "None"
    embed = discord.Embed(colour=discord.Color.red(), timestamp=ctx.message.created_at)
    await member.ban(reason=reason, delete_message_days=7)
    await member.unban(reason="Soft-Banned")
    await ctx.message.delete()
    embed.set_author(name=f"{member} Was Softbanned")
    await ctx.send(embed=embed)


@commands.bot_has_guild_permissions(manage_messages=True)
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@bot.command(aliases=["purge"])
async def clear(ctx, number: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=number)


@commands.bot_has_guild_permissions(kick_members=True)
@commands.has_permissions(kick_members=True)
@commands.guild_only()
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author == member:
        await ctx.send(f"You Can't do that", delete_after=5)
        return
    if (
        member.guild_permissions.administrator
        or member.guild_permissions.kick_members
        or member.guild_permissions.kick_members
    ):
        await ctx.send(
            f"That User is a Administrator/Moderator so i cant {ctx.command.name} that user",
            delete_after=7,
        )
        return
    if ctx.guild.me.top_role.position < member.top_role.position:
        await ctx.send(
            f"My Role Is Not High Enough To {ctx.command.name} This User",
            delete_after=7,
        )
        return
    if not reason:
        reason = "None"
    try:
        await member.send(
            f"You have been kicked from `{ctx.guild.name}` Reason: \n{reason}"
        )
    except discord.Forbidden:
        pass
    finally:
        embed = discord.Embed(
            colour=discord.Color.red(), timestamp=ctx.message.created_at
        )
        await member.kick(reason=reason)
        await ctx.message.delete()
        embed.set_author(name=f"{member} Was kicked")
        embed.set_footer(
            text=f"Executor: {ctx.author} ID: {ctx.author.id}",
            icon_url=ctx.author.avatar_url,
        )
        await ctx.send(embed=embed)


@commands.bot_has_guild_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
@commands.guild_only()
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author == member:
        await ctx.send(f"You Can't do that", delete_after=5)
        return
    if (
        member.guild_permissions.administrator
        or member.guild_permissions.kick_members
        or member.guild_permissions.kick_members
    ):
        await ctx.send(
            f"That User is a Administrator/Moderator so i cant {ctx.command.name} that user",
            delete_after=7,
        )
        return
    if ctx.guild.me.top_role.position < member.top_role.position:
        await ctx.send(
            f"My Role Is Not High Enough To {ctx.command.name} This User",
            delete_after=7,
        )
        return
    if not reason:
        reason = "None"
    embed = discord.Embed(colour=discord.Color.red(), timestamp=ctx.message.created_at)

    try:
        await member.send(
            f"You have been banned from `{ctx.guild.name}`\n Reason: \n{reason}"
        )
    except discord.Forbidden:
        pass
    finally:
        await member.ban(reason=reason)
        await ctx.message.delete()
        embed.set_author(name=f"{member} Was banned")
        embed.set_footer(
            text=f"{ctx.author} ID: {ctx.author.id}", icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=embed)


@commands.bot_has_guild_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
@commands.guild_only()
@bot.command()
async def unban(ctx, member, *, reason=None):
    if reason is None:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member} Has Been Unbanned By {ctx.author}")


@commands.guild_only()
@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(
        title="Server Infomations",
        color=discord.Colour.blue(),
        timestamp=ctx.message.created_at,
    )
    statues = [
        len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),
    ]
    online = 0
    for i in ctx.guild.members:
        if (
            str(i.status) == "online"
            or str(i.status) == "idle"
            or str(i.status) == "dnd"
        ):
            online += 1
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Server Name:", value=ctx.guild.name)
    embed.add_field(name="Server ID:", value=ctx.guild.id)
    embed.add_field(name="Server Owner:", value=ctx.message.guild.owner.mention)
    embed.add_field(name="Total Members:", value=ctx.guild.member_count)
    embed.add_field(
        name="Server Verification Level", value=ctx.guild.verification_level
    )
    embed.add_field(name="Currently Online", value=str(online))
    embed.add_field(
        name="Statues",
        value=f"🟢 {statues[0]} 🌙 {statues[1]}\n🔴 {statues[2]} ⚪ {statues[3]}",
    )
    embed.add_field(
        name="Server Created at",
        value=ctx.guild.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC (Universal Time Coordinated)"
        ),
    )
    embed.add_field(name="Server Region", value=ctx.guild.region)
    embed.add_field(name=" Custom Emojis:", value=str(len(ctx.guild.emojis)))
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


@commands.guild_only()
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)


@commands.guild_only()
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    embed = discord.Embed(
        color=discord.Colour.blue(),
        timestamp=ctx.message.created_at,
        title="User Information",
    )
    if not member:
        member = ctx.author
    roles = [role for role in member.roles]
    join_position = (
        sorted(ctx.guild.members, key=lambda m: m.joined_at).index(member) + 1
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Name of the user:", value=(member.name))
    embed.add_field(name="In Server username:", value=member.display_name)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(
        name="Joined Server At:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
    )
    embed.add_field(name="Join Position", value=str(join_position))
    embed.add_field(
        name="Account Created On:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
    )
    embed.add_field(
        name="All Roles:", value="".join([role.mention for role in roles]), inline=False
    )
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NoPrivateMessage):
        return await ctx.send("This command dont work in dms channel")
    elif isinstance(error, commands.MissingPermissions):
        return await ctx.send(
            f"It looks like you are missing some permissions\n `{', '.join(error.missing_perms)}`"
        )
    elif isinstance(error, commands.BotMissingPermissions):
        string = error.missing_perms
        return await ctx.send(f"Bot Missing Permissions\n`{','.join(string)}`")


bot.run(TOKEN)
