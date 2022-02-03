#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👥 Join Discussion Group", url = "https://t.me/HEO_TRADING")
                    ]
                ]
            )
       
   
