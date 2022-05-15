import discord
from discord.ext import commands
from dislash import InteractionClient, Option, OptionType, OptionChoice

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
guild_ids = [975132627000508447]
slash = InteractionClient(client, test_guilds=guild_ids)
token = "OTc1MjE2MzYwNjM4NTE3Mjk4.GtjqcJ.AKjgUpj045_3MehRuwwCTiV7_57fNZB6veAQJE"
intro_chat = 975219722989744128



@slash.slash_command(
    name="verify",
    description="Verify your account.",
    guild_ids=guild_ids,
    options=[
        Option(
            "name",
            description="Your name.",
            type=OptionType.STRING,
            required=True,
        ),
        Option(
            "program",
            description="Program you plan to attend",
            type=OptionType.STRING,
            required=True,
            choices=[
                OptionChoice("Computer Science", "Computer Science"),
                OptionChoice("Math", "Math"),
                OptionChoice("AFM", "AFM"),
                OptionChoice("Management Engineering", "Management Engineering"),
                OptionChoice("Systems Design Engineering", "Systems Design Engineering"),
                OptionChoice("Software Engineering", "Software Engineering"),
                OptionChoice("Biomedical Engineering", "Biomedical Engineering"),
                OptionChoice("Computer Engineering", "Computer Engineering"),
                OptionChoice("Electrical Engineering", "Electrical Engineering"),
                OptionChoice("Mechanical Engineering", "Mechanical Engineering"),
                OptionChoice("Civil Engineering", "Civil Engineering"),
                OptionChoice("Chemical Engineering", "Chemical Engineering"),
                OptionChoice("Architectural Engineering", "Architectural Engineering"),
                OptionChoice("Mechatronics Engineering", "Mechatronics Engineering"),
                OptionChoice("Nanotechnology Engineering", "Nanotechnology Engineering"),
                OptionChoice("Environmental Engineering", "Environmental Engineering"),
                OptionChoice("CFM", "CFM"),
                OptionChoice("Biology", "Biology"),
                OptionChoice("Chemistry", "Chemistry"),
                OptionChoice("Physics", "Physics"),
                OptionChoice("Psychology", "Psychology"),
                OptionChoice("Economics", "Economics"),
                OptionChoice("FARM", "FARM"),
                OptionChoice("Other", "Other")
            ],
        ),
        Option(
            "year",
            description="Year you plan to attend",
            type=OptionType.STRING,
            required=True,
            choices=[
                OptionChoice("incoming", "Incoming"),
                OptionChoice("Upper Year", "Upper Year"),
            ],
        ),
        Option(
            "about",
            description="About you.",
            type=OptionType.STRING,
            required=True
        ),
        Option(
            "instagram",
            description="Instagram username.",
            type=OptionType.STRING,
            required=False
        ),
        Option(
            "linkedin",
            description="Link to your LinkedIn profile.",
            type=OptionType.STRING,
            required=False
        ),
        Option(
            "github",
            description="Link to your GitHub profile.",
            type=OptionType.STRING,
            required=False
        ),
        Option(
            "other",
            description="Other links to your profile.",
            type=OptionType.STRING,
            required=False
        ),

    ]
)
async def verify(ctx, name, program, about, year, instagram="N/A", linkedin="N/A", github="N/A", other="N/A"):
    titlee = name + " - " + program + " (" + year + ")"
    embed = discord.Embed(title=titlee, description=about)
    embed.add_field(name="Linkedin", value=linkedin, inline=True)
    embed.add_field(name="Instagram", value=instagram, inline=True)
    embed.add_field(name="Github", value=github, inline=True)
    embed.add_field(name="Other", value=other, inline=True)
    embed.set_footer(text=str(ctx.author.name))

    # if program is not a role then create role 
    if program not in [role.name for role in ctx.guild.roles]:
        await ctx.guild.create_role(name=program)
        # get role by name
        role = discord.utils.get(ctx.guild.roles, name=program)
        await ctx.author.add_roles(role)

        try:
            await ctx.author.edit(nick=name)
        except:
            print("couldnt change nickname")

    # if program is a role then add role to user
    else:
        role = discord.utils.get(ctx.guild.roles, name=program)
        await ctx.author.add_roles(role)
    
    veirified_role = discord.utils.get(ctx.guild.roles, name="Verified")
    await ctx.author.add_roles(veirified_role)

    
    channel = client.get_channel(intro_chat)

    await channel.send(embed=embed)



client.run(token)
