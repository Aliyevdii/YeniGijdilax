from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"DeYeRliM'h VaR'h QaaŞ'h @A_l_i_y_e_v_d_i 💋❤️\n\n")
  return                      
