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


# =========================
# CHANNELS
# =========================

CHANNELS = [
    ("🕊️ ቃሉን አነባለሁ", "@kalun_anebalew"),
    ("🎵 ቅኔ ለእግዚአብሔር", "@getami_daniel"),
    ("🌅 መንፈስ ቅዱስ", "@morning_messages1")
]


# =========================
# MAIN MENU
# =========================

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


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    name = user.first_name

    async def about_ministry(update: Update, context: ContextTypes.DEFAULT_TYPE):

    about_text = """
🕊️ DANI HUB MINISTRY 🌐

ዲጂታል የፕሮቴስታንት ክርስቲያን አገልግሎት

DANI HUB MINISTRY 🌐 በ2018 ዓ.ም.
በወንድም ዳኒኤል አበራ የተመሰረተ
የፕሮቴስታንት ክርስቲያን
ዲጂታል አገልግሎት ነው።

🌐 ራዕያችን:

በቴክኖሎጂ እየተጠቀምን የእግዚአብሔርን
ቃል ለብዙዎች ማድረስ፣
ሕይወቶችን በክርስቶስ ፍቅር
ማበረታታት እና የመንፈሳዊ
ድጋፍ ማቅረብ ነው።


🎯 ተልዕኳችን:

📖 የእግዚአብሔርን ቃል ማስፋፋት

🙏 የጸሎት ድጋፍ መስጠት

🎶 መንፈሳዊ መዝሙሮችን
ማቅረብ

🛐 የሕይወት ምስክርነት
ማካፈል

⛓️ ከሱስ ነፃ ለመውጣት
መንፈሳዊ ድጋፍ መስጠት


🙏 በDANI HUB MINISTRY 🌐
ማግኘት የሚችሉት:

📖 የዕለቱ ቃል

🙏 የጸሎት ጥያቄ

🎶 መዝሙሮች

🛐 የሕይወት ምስክርነት

⛓️ ከሱስ ነፃ ለመውጣት

🤝 አገልግሎቱን መደገፍ


📖 "ሂዱና ወደ ዓለም ሁሉ
ወንጌልን ስበኩ።"

— ማርቆስ 16፥15

❤️ DANI HUB MINISTRY 🌐
እግዚአብሔርን ማገልገል
• ተስፋን ማድረስ
• እምነትን መገንባት
"""

    await update.message.reply_text(about_text)


    buttons = []

    for title, channel in CHANNELS:
        buttons.append(
            [
                InlineKeyboardButton(
                    title,
                    url=f"https://t.me/{channel.replace('@','')}"
                )
            ]
        )

    buttons.append(
        [
            InlineKeyboardButton(
                "✅ ተቀላቅያለሁ",
                callback_data="verify"
            )
        ]
    )


    await update.message.reply_text(
        message,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# =========================
# VERIFY CHANNELS
# =========================

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    user = query.from_user

    await query.answer()

    for _, channel in CHANNELS:

        member = await context.bot.get_chat_member(
            chat_id=channel,
            user_id=user.id
        )

        if member.status == "left":

            await query.message.reply_text(
                "⚠️ እባክዎ ሁሉንም ቻናሎች ይቀላቀሉ።"
            )

            return


    await query.message.reply_text(
        "🙏 እናመሰግናለን!\n\n"
        "አሁን የDANI HUB MINISTRY 🌐 "
        "አገልግሎቶችን መጠቀም ይችላሉ።",
        reply_markup=reply_markup
    )


# =========================
# BUTTONS
# =========================

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text


    if text == "📖 የዕለቱ ቃል":
        await update.message.reply_text(
            "📖 የዕለቱ ቃል በቅርቡ ይጨመራል።"
        )


    elif text == "🙏 የጸሎት ጥያቄ":
        await update.message.reply_text(
            "🙏 የጸሎት አገልግሎት በቅርቡ ይጨመራል።"
        )


    else:
        await update.message.reply_text(
            "🙏 ይህ አገልግሎት በማዘጋጀት ላይ ነው።"
        )


# =========================
# RUN
# =========================

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(verify, pattern="verify")
)

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        buttons
    )
)


print("DANI HUB MINISTRY BOT STARTED")

app.run_polling()