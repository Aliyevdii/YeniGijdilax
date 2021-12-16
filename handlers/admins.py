from asyncio.queues import QueueEmpty
 
from pyrogram import Client, filters 
from pyrogram.types import Message
from cache.admins import admins

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'Duraklatıldı'
    ):
        await message.reply_text("❗ heç nə oynamır!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("▶️ **Musiqi dayandırıldı!**\n\n• **musiqi istifadə etməyə davam etmək üçün » İrəli**") 


@Client.on_message(command("dur") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'Oynanıyor'
    ):
         await message.reply_text("❗ Hiçbir şey duraklatılmadı!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("⏸ **Musiqi davam edir!**\n\n• **istifadəni dayandırmaq əmri » durdur**")


@Client.on_message(command("bitir") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Heç nə dərc olunmur!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("✅ **Musiqi dayandırıldı!**\n\n• **Userbotun səsli söhbəti kəsilib**")


@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Keçiləcək musiqi yoxdur!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("⏭️ **Mahnı növbəti növbəyə keçdi**")

@Client.on_message(command("ver"))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("Səlahiyyətli İstifadəçiyə cavab verin!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("istifadəçi icazəlidir.")
    else:
        await message.reply("✔ İstifadəçi Artıq Səlahiyyətlidir!")


@Client.on_message(command("al"))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✘ İstifadəçinin icazəsini ləğv etmək üçün mesaja cavab verin!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("icazəsiz istifadəçi")
    else:
        await message.reply("✔ İstifadəçi icazəlidir!")


@Client.on_message(command(["ses"]) & other_filters)
@authorized_users_only
async def ses(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"✅ **vahid kimi təyin edin:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**xəta:** {e}")
