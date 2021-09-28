# About Message

from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.private & filters.command(["about"]))
async def about(unzipbot, msg):
    await msg.reply(
        text=Data.ABOUT,
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button),
    )