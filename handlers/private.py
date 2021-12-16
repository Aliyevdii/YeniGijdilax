from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
#Bir_Beyfendi

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(client: Client, message: Message):
    await message.reply_text(f"**Salam {message.from_user.mention} 🎵\n Mən {bot}!\nTelegram qruplarında səsli söhbətdə musiqi səsləndirmək üçün yaradılmışam.\n✅ Ətraflı məlumat üçün /bilgi yazın\n\nPowered by @NEXUS_MMC **",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Qurupa əlavə et", url="https://t.me/NexusMusiicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💭 Söhbət Grubu", url="https://t.me/iron_Blood_Gurup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨🏻‍💻 Sahibi", url = "https://t.me/A_l_i_y_e_v_d_i"
                    ),
                    InlineKeyboardButton(
                        "👨🏻‍🎤 Asistan" , url = "https://t.me/NexusAsistan"
                    )
                ],
                [ 
                    InlineKeyboardButton(
                        "🌀 Əmirlər" , url = "https://t.me/NEXUS_MMC/9"
                    ),
                    InlineKeyboardButton(
                        "🌐 ⲛ ⲉ ⲭ υ ⲋ", url="https://t.me/NEXUS_MMC"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(f"**Salam {message.from_user.mention}!\nⲛ  ⲉ  ⲭ  υ  ⲋ Music Yardım Panelinə Xoş Gəldin 🤓\n\n ▶️ /oynat - mahnı oxutmaq üçün youtube url və ya mahnı faylına cavab verin\n ▶️ /oynat <mahnı adı> - istədiyiniz mahnını ifa edin\n 🔴 /ytp <Sorgu> - youtube-da oynayın\n 🎵 /bul <mahnı adı> - istədiyiniz mahnıları tez tapın\n 🎵 /vbul istədiyiniz videoları tez tapın\n 🔍 /ara <query> - youtube-da təfərrüatlı videolar axtarın\n\n Yalnız adminlər üçündür..\n ▶️ /devam - mahnını ifa etməyə davam edin\n ⏹ /bitir - musiqi çalmağı dayandırın\n 🔼 /ver istifadəçiyə icazə verin ki, bot yalnız administrator üçün mövcud olan əmrlərdən istifadə edə bilsin\n 🔽 /al botun admin əmrlərindən istifadə edə bilən istifadəçi al\n 🎚 /ses köməkçi hesabınızın həcminə nəzarət edin\n\n ⚪ /katil - Musiqi köməkçisi qrupunuza qoşulur\n ⚫ /ayril - Musiqi köməkçisi qrupunuzu tərk edir.\n\n ❗ Diqqət:\n Botun aktiv işləməsi üçün aşağıdakı üç imtiyaz tələb olunur:\n - Mesajları silmək səlahiyyəti,\n - Link vasitəsilə dəvət etmək səlahiyyəti,\n - Səsli çatı idarə etmək səlahiyyəti.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨🏻‍💻 Sahibi", url="https://t.me/A_l_i_y_e_v_d_i")
                 ]
             ]
         )
    )
