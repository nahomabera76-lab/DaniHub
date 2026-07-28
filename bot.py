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


CHANNELS = [
    ("🕊️ ቃሉን አነባለሁ", "@kalun_anebalew"),
    ("🎵 ቅኔ ለእግዚአብሔር", "@getami_daniel"),
    ("🌅 መንፈስ ቅዱስ", "@morning_messages1")
]


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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    name = user.first_name

    welcome = f"""
🕊️ በጌታ የተወደድክ/የተወደድሽ ወንድም/እህት {name}

እንኳን ወደ DANI HUB MINISTRY 🌐
በሰላም መጣህ/መጣሽ።

DANI HUB MINISTRY 🌐
በ2018 ዓ.ም በወንድም ዳኒኤል አበራ
የተመሰረተ የፕሮቴስታንት
ክርስቲያን ዲጂታል አገልግሎት ነው።

የእግዚአብሔርን ቃል በቴክኖሎጂ
ለብዙዎች ለማድረስ፣
ሕይወቶችን ለማበረታታት
እና መንፈሳዊ ድጋፍ ለመስጠት
የተመሰረተ አገልግሎት ነው።

🙏 ለመቀጠል እባክዎ
የDANI HUB MINISTRY ዋና ቻናሎቻችንን ይቀላቀሉ።
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

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user = query.from_user

    for title, channel in CHANNELS:

        member = await context.bot.get_chat_member(
            chat_id=channel,
            user_id=user.id
        )

        if member.status in ["left", "kicked"]:

            await query.message.reply_text(
                "⚠️ እባክዎ መጀመሪያ ሁሉንም ቻናሎች ይቀላቀሉ።"
            )

            return

    await query.message.reply_text(
        "🎉 እንኳን ደስ አለዎት!\n\n"
        "DANI HUB MINISTRY 🌐 አገልግሎቶችን "
        "አሁን መጠቀም ይችላሉ።",
        reply_markup=reply_markup
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🕊️ DANI HUB MINISTRY 🌐

DANI HUB MINISTRY 🌐 በ2018 ዓ.ም.
በወንድም ዳኒኤል አበራ የተመሰረተ
የፕሮቴስታንት ክርስቲያን
ዲጂታል አገልግሎት ነው።

🌐 ራዕያችን

በቴክኖሎጂ እየተጠቀምን
የእግዚአብሔርን ቃል ለብዙዎች ማድረስ፣
ሕይወቶችን በክርስቶስ ፍቅር
ማበረታታት እና መንፈሳዊ
እድገትን መደገፍ ነው።

🎯 ተልዕኳችን

📖 የእግዚአብሔርን ቃል ማስፋፋት

🙏 የጸሎት ድጋፍ መስጠት

🎶 መንፈሳዊ መዝሙሮችን ማድረስ

🛐 የሕይወት ምስክርነቶችን ማጋራት

⛓️ ከሱስ ነፃ ለመውጣት
መንፈሳዊ ድጋፍ መስጠት

🤝 የአገልግሎቱን ድጋፍ መቀበል

💰 የሪፈራል እድል መስጠት

📖 "ሂዱና ወደ ዓለም ሁሉ
ወንጌልን ስበኩ።"

— ማርቆስ 16፥15

❤️ DANI HUB MINISTRY 🌐
"""


    await update.message.reply_text(text)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text


    if text == "📖 የዕለቱ ቃል":

        await update.message.reply_text(
            "📖 የዛሬ የመጽሐፍ ቅዱስ ቃል በቅርቡ ይላካል።"
        )


    elif text == "🙏 የጸሎት ጥያቄ":

        await update.message.reply_text(
            "🙏 የጸሎት ጥያቄዎን ይላኩ።\n\n"
            "የጸሎት ርዕስዎ በአገልግሎታችን ይታያል "
            "እና ብዙ አማኞች አብረውዎት ይጸልያሉ።"
        )


    elif text == "🎶 መዝሙሮች":

        await update.message.reply_text(
            "🎶 የመዝሙር አገልግሎት በቅርቡ ይጨመራል።"
        )


    elif text == "🛐 የሕይወት ምስክርነት":

        await update.message.reply_text(
            "🛐 የሕይወት ምስክርነትዎን ያካፍሉ።\n\n"
            "ስምዎን መግለጽ ወይም ማንነትዎን መደበቅ ይችላሉ።"
        )


    elif text == "⛓️ ከሱስ ነፃ ለመውጣት":

        await update.message.reply_text(
            "⛓️ ከሱስ ነፃ ለመውጣት የሚረዳ "
            "መንፈሳዊ ድጋፍ በቅርቡ ይጨመራል።"
        )


    elif text == "ℹ️ ስለ Dani Hub Ministry":

        await about(update, context)


    elif text == "🌍 ቋንቋ":

        await update.message.reply_text(
            "🌍 የቋንቋ መቀየሪያ አገልግሎት በቅርቡ ይጨመራል።"
        )


    elif text == "🤝 አገልግሎቱን ይደግፉ":

        await update.message.reply_text(
            "🤝 DANI HUB MINISTRY 🌐ን ለመደገፍ "
            "መረጃ በቅርቡ ይላካል።"
        )


    elif text == "💰 ገቢ ያግኙ":

        await update.message.reply_text(
            "💰 ሌሎችን ወደ DANI HUB MINISTRY 🌐 "
            "በመጋበዝ የሪፈራል ሽልማት "
            "የሚያገኙበት ስርዓት ነው።"
        )


    elif text == "📞 አስተዳዳሪ":

        await update.message.reply_text(
            "📞 አስተዳዳሪ\n\n"
            "Telegram: @mr_dani10"
        )


    else:

        await update.message.reply_text(
            "🙏 እባክዎ ከሜኑ ውስጥ አንዱን ይምረጡ።"
        )

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