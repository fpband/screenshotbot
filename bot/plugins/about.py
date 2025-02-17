from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config
from bot.database.forcesub import ForceSub


BUTTONS = [[
    InlineKeyboardButton('🏡 Home', callback_data='home'),
    InlineKeyboardButton('🚸 Powered By', callback_data='t.me/MoviesFlixers_DL'),
    InlineKeyboardButton('♻ Help', callback_data='help')
]]

ABOUT_TEXT = """
╭────[🔅Sᴄʀᴇᴇɴsʜᴏᴛ Bᴏᴛ🔅]───⍟
│
├<b>🤖 Bot Name : <a href='https://t.me/TeleRoid_Screenshot_Bot'>@TeleRoid_Screenshot_Bot</a></b>
│
├<b>📢 Channel : <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a></b>
│
├<b>♂️ Support: <a href='https://t.me/TeleRoid14'>@TeleRoidSupport</a></b>
│
├<b>👥 Version : <a href='https://t.me/TeleRoid_Screenshot_Bot'>0.9.2 beta</a></b>
│
├<b>🛠 Source : <a href='https://github.com/PredatorHackerzZ'>Click Here</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://t.me/PredatorHackerZ'>Pred∆tor</a></b>
│
├<b>🚸 Powered By : <a href='https://t.me/Moviesflixers_DL'>@HindiWebNetwork</a></b>
│
╰────────[Thank Yiu]───⍟

__If issues persists contact my Master.__

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Since you are one of the admins, you can check /admin to view the admin commands."
)


@ScreenShotBot.on_message(filters.private & filters.command("about"))
async def about_(c, m):
    forcesub = await ForceSub(c, m,)
    if forcesub == 400:
        return
    await m.reply_text(
        text=ABOUT_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("about"))
)
async def about_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=ABOUT_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS)
    )
