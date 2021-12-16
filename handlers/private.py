from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as BN
from helpers.filters import command, other_filters2


@Client.on_message(command(["start", f"start"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""**Salam, {message.from_user.mention} 🎵
Telegram qruplarında səsli söhbətdə musiqi səsləndirmək üçün yaradılmışam\n\n✅ Ətraflı məlumat üçün /bilgi'yazın.
 **""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Qurupa əlavə et", url="https://t.me/NexusMusiicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💭 Söhbət gurupu", url="https://t.me/iron_Bloos_Gurup" 
                    ),
                    InlineKeyboardButton(
                        "👨🏻‍💻 Sahibi", url="https://t.me/A_l_i_y_e_v_d_i"
                    ),
                    InlineKeyboardButton(
                        "🦹 Asistan", url="https://t.me/NexusAsistan") 
                ],
                [
                    InlineKeyboardButton(
                        "⚕️ Əmirlər", url="https://t.me/NEXUS_MMC/9" 
                    ),
                    InlineKeyboardButton(
                        "🌐 Support", url="https://t.me/NEXUS_MMC" 
                    )
                    )
                ]
            ]
        ), 
     disable_web_page_preview=True
   ) 

@Client.on_message(command(["bilgi"])) 
async def bilgi(_, message: Message):
      await message.reply_text(f"**Merhaba {message.from_user.mention}!\n Bu botun bilgi menüsü 📚\n\n ▶️ /play - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /play <song name> - istediğiniz şarkıyı çalınız\n 🔴 /ytplay <Sorgu> - youtube üzerinden çalar\n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n Yalnızca yöneticiler için..\n ⏩ /resume - şarkı çalmaya devam et\n ⏹ /end - müzik botunu kapatmak için\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n 🎚 /ses asistan hesabın ses seviyesini kontrol et\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨🏻‍💻 Sahibi", url="https://t.me/A_l_i_y_e_v_d_i")
                 ]
             ]
         )
    )
