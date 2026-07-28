from telegram import (
Update,
ReplyKeyboardMarkup,
InlineKeyboardButton,
InlineKeyboardMarkup
)

from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
CallbackQueryHandler,
ContextTypes,
filters
)

from config import BOT_TOKEN

#==========================

CHANNELS

#==========================

CHANNELS = [
("🕊️ ቃሉን አነባለሁ", "@kalun_anebalew"),
("🎵 ቅኔ ለእግዚአብሔር", "@getami_daniel"),
("🌅 መንፈስ ቅዱስ", "@morning_messages1"),
]

#==========================

MAIN MENU

#==========================

keyboard = [
["📖 የዕለቱ ቃል", "🙏 የጸሎት ጥያቄ"],
["🎶 መዝሙሮች", "🛐 የሕይወት ምስክርነት"],
["⛓️ ከሱስ ነፃ ለመውጣት"],
["🌍 ቋንቋ", "🤝 አገልግሎቱን ይደግፉ"],
["💰 ገቢ ያግኙ", "ℹ️ ስለ Dani Hub Ministry"],
["📞 አስተዳዳሪ"]
]

reply_markup = ReplyKeyboardMarkup(
keyboard,
resize_keyboard=True
)

#==========================

START

#==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

user = update.effective_user  
name = user.first_name  

welcome = f"""

🕊️ በጌታ የተወደድክ/የተወደድሽ ወንድም/እህት {name}

እንኳን ወደ
DANI HUB MINISTRY 🌐
በደህና መጣህ/መጣሽ!

DANI HUB MINISTRY 🌐
በ2018 ዓ.ም.
በወንድም ዳኒኤል አበራ
የተመሰረተ
የፕሮቴስታንት
ክርስቲያን
ዲጂታል
አገልግሎት ነው።

🙏 ከመቀጠልዎ በፊት
ከታች ያሉትን
የDANI HUB MINISTRY
ዋና ቻናሎች
ይቀላቀሉ።
"""

buttons = []  

for title, username in CHANNELS:  

    buttons.append([  
        InlineKeyboardButton(  
            title,  
            url=f"https://t.me/{username.replace('@','')}"  
        )  
    ])  

buttons.append([  
    InlineKeyboardButton(  
        "✅ ተቀላቅያለሁ",  
        callback_data="verify"  
    )  
])  

await update.message.reply_text(  
    welcome,  
    reply_markup=InlineKeyboardMarkup(buttons)  
)

#==========================

VERIFY

#==========================

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):

query = update.callback_query  

await query.answer()  

user = query.from_user  

for _, channel in CHANNELS:  

    member = await context.bot.get_chat_member(  
        chat_id=channel,  
        user_id=user.id  
    )  

    if member.status == "left":  

        await query.message.reply_text(  
            "⚠️ እባክዎ መጀመሪያ ሁሉንም ቻናሎች ይቀላቀሉ።"  
        )  

        return  

await query.message.reply_text(  
    "🎉 እንኳን ደስ አለዎት!\n\nDANI HUB MINISTRY 🌐 አገልግሎቶችን አሁን መጠቀም ይችላሉ።",  
    reply_markup=reply_markup  
)

#==========================

ABOUT MINISTRY

#==========================

async def about(update: Update):

text = """

🕊️ DANI HUB MINISTRY 🌐
"""
text += """

━━━━━━━━━━━━━━━

DANI HUB MINISTRY 🌐
በ2018 ዓ.ም.
በወንድም ዳኒኤል አበራ
የተመሰረተ
የፕሮቴስታንት
ክርስቲያን
ዲጂታል
አገልግሎት ነው።

━━━━━━━━━━━━━━━

🌐 ራዕያችን

በቴክኖሎጂ እየተጠቀምን
የእግዚአብሔርን ቃል
ለዓለም ማድረስ፣
ሕይወቶችን
በክርስቶስ ፍቅር
ማበረታታት
እና
በመንፈሳዊ ሕይወት
ማሳደግ።

━━━━━━━━━━━━━━━

🎯 ተልዕኳችን

📖 የእግዚአብሔርን ቃል
በዲጂታል መድረኮች
ማስፋፋት።

🙏 የጸሎት ድጋፍ
ለአማኞች
መስጠት።

🎶 መዝሙሮችን
ለሁሉም
በነፃ
ማድረስ።

🛐 የሕይወት
ምስክርነቶችን
ማጋራት።

⛓️ ከሱስ
ነፃ ለመውጣት
መንፈሳዊ
ድጋፍ
መስጠት።

━━━━━━━━━━━━━━━

🙏
በDANI HUB MINISTRY
ማግኘት
የሚችሉት

📖 የዕለቱ ቃል

🙏 የጸሎት ጥያቄ

🎶 መዝሙሮች

🛐 የሕይወት
ምስክርነት

⛓️ ከሱስ
ነፃ ለመውጣት

🌍 ቋንቋ
መቀየር

🤝 አገልግሎቱን
መደገፍ

💰 ገቢ
ያግኙ

━━━━━━━━━━━━━━━

📖
"ሂዱና
ወደ ዓለም ሁሉ
ወንጌልን
ስበኩ።"

— ማርቆስ 16፥15

❤️ DANI HUB MINISTRY 🌐

እግዚአብሔርን ማገልገል
• ተስፋን ማድረስ
• እምነትን መገንባት
"""

await update.message.reply_text(text)

#==========================

BUTTONS

#==========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

text = update.message.text  

if text == "📖 የዕለቱ ቃል":  
    await update.message.reply_text(  
        "📖 ይህ አገልግሎት በቀጣይ እንጨምራለን።"  
    )  

elif text == "🙏 የጸሎት ጥያቄ":  
    await update.message.reply_text(  
        "🙏 የጸሎት አገልግሎት በቀጣይ እንጨምራለን።"  
    )  

elif text == "🎶 መዝሙሮች":  
    await update.message.reply_text(  
        "🎶 የመዝሙር አገልግሎት በቅርቡ ይጨመራል።"  
    )  

elif text == "🛐 የሕይወት ምስክርነት":  
    await update.message.reply_text(  
        "🛐 የምስክርነት አገልግሎት በቅርቡ ይጨመራል።"  
    )  

elif text == "⛓️ ከሱስ ነፃ ለመውጣት":  
    await update.message.reply_text(  
        "⛓️ ይህ አገልግሎት በቅርቡ ይጨመራል።"  
    )  

elif text == "ℹ️ ስለ Dani Hub Ministry":  
    await about(update)  
elif text == "🌍 ቋንቋ":  
    await update.message.reply_text(  
        "🌍 የቋንቋ አገልግሎት በቅርቡ ይጨመራል።"  
    )  

elif text == "🤝 አገልግሎቱን ይደግፉ":  
    await update.message.reply_text(  
        "🤝 የአገልግሎቱ ድጋፍ አገልግሎት በቅርቡ ይጨመራል።"  
    )  

elif text == "💰 ገቢ ያግኙ":  
    await update.message.reply_text(  
        "💰 የሪፈራል ስርዓት በቅርቡ ይጨመራል።"  
    )  

elif text == "📞 አስተዳዳሪ":  
    await update.message.reply_text(  
        "👤 አስተዳዳሪ\n\n"  
        "Telegram: @mr_dani10"  
    )  

else:  
    await update.message.reply_text(  
        "🙏 እባክዎ ከሜኑ ውስጥ አንዱን ይምረጡ።"  
    )

#==========================

BOT START

#==========================

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
CommandHandler(
"start",
start
)
)

app.add_handler(
CallbackQueryHandler(
verify,
pattern="verify"
)
)

app.add_handler(
MessageHandler(
filters.TEXT & ~filters.COMMAND,
buttons
)
)

print("🕊️ DANI HUB MINISTRY BOT STARTED")

app.run_polling()