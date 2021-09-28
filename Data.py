#Start Message

from unzipbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:

    START = "Hello {}. \n\nWelcome to {}" \
            "\nI can unzip & unrar files which you send me & I will upload them to you." \
            "alsoI will total the contents & number of files."

    if Config.OWNER_ID != 0:

        if Config.OWNER_NAME:
            START += \
            (
                f"\n\nCreator & Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print\
                (
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers."
            )
            print("Quitting the bot")
            raise SystemExit("\nSomething went wrong.\nPlease try again.")
    else:
        START += f"\n\nBy @abolfazleshun"


    ABOUT = \
        "*************************************************" \
        "\n\t    *** About This Bot & Owner ***           " \
        "\n\t* This is an Private source Unzip bot        " \
        "\n\t* Framework : [Pyrogram](docs.pyrogram.org)  " \
        "\n\t* Language : [Python](www.python.org)        " \
        "\n\t* Developer : Abolfazl Omidiyan              " \
        "\n\t* https://github.com/AbolfazlOmidiyan        " \
        "\n*************************************************"



    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit("\nSomething went wrong.\nPlease try again.")


# Deploy
    DEPLOY = """
**Would yuo like create your own such bot??** 

This is made by python and this source code is private.
"""

    HELP = """
**Do You Need Help ?? **

Send any Zip/Rar File then choose a Mode and your work is done! 
I'll unzip/unrar it and return you it's contents.

**Available Commands** :-
/modes - Know about both modes.
/about - About this bot and source code.
/help - This Message.
/start - Check if bot is alive.

contact owner @abolfazleshun 
"""

    MODES = """
**What are Modes ❔**

1) **Tortoise 🐢**
Bit Slow but Steady. 

While using this mode you will can be notified about the all progresses happening.

Progresses include:
- downloaded so far
- contents in provided file
- number of files in provided file
- uploaded too far with number of the file being uploaded

It doesn't take too much time than other mode and is the recommended method. 

2) ** Rabbit 🐇**
Bit Fast but less user friendly.

While using this mode you won't be notified about any progresses that go on. Just download completion and upload completion will be notified. 

This is bit fast but only recommended for larger files as smaller files won't have much time difference.   
    """

    CHOOSE_MODE = "**CHOOSE MODE **" \
                  "\nChoose a mode from below to start extracting files..."


    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Home 🏠", callback_data="home")]]


    # Modes Buttons
    modes_buttons = [
        [
            InlineKeyboardButton("Tortoise 🐢", callback_data="tortoise"),
            InlineKeyboardButton("Rabbit 🐇", callback_data="rabbit")
        ],
        [InlineKeyboardButton("What are Modes ⁉️", callback_data="modes")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("What are Modes ❔", callback_data="modes"),
            InlineKeyboardButton("🤔 About🤔", callback_data="about"),
        ],
        [InlineKeyboardButton("How to Use me ❓", callback_data="help")],
        [InlineKeyboardButton("👨‍💻Developer👨‍💻", url="https://t.me/abolfazleshun")],
        [InlineKeyboardButton("👨‍🔧updates channel👨‍🔧", url="https://t.me/pishro_hack")],
        [InlineKeyboardButton("🤖support group🤖", url="https://t.me/pishro_hack")],
    ]
