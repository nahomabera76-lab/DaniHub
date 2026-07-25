from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN

keyboard = [
    ["📖 የዛሬ ጥቅስ", "🙏 የጸሎት ጥያቄ"],
    ["📢 ቻናሎቻችን", "🌍 ቋንቋ"],
    ["💰 ገቢ ያግኙ", "👥 የግብዣ ሊንክ"],
    ["ℹ️ ስለ Dani Hub", "📞 አስተዳዳሪ"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕊️ እንኳን ወደ Dani Hub በደህና መጡ!\n\nከታች ካሉት አዝራሮች አንዱን ይምረጡ።",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📖 የዛሬ ጥቅስ":
        await update.message.reply_text("📖 ይህ በኋላ የዕለቱን የመጽሐፍ ቅዱስ ጥቅስ ያሳያል።")

    elif text == "🙏 የጸሎት ጥያቄ":
        await update.message.reply_text("🙏 የጸሎት ጥያቄዎን ይላኩ።")

    elif text == "📢 ቻናሎቻችን":
        await update.message.reply_text("📢 በኋላ የቻናሎቻችን ሊንኮች ይታያሉ።")

    elif text == "🌍 ቋንቋ":
        await update.message.reply_text("🌍 በኋላ ቋንቋ መቀየሪያ ይጨመራል።")

    elif text == "💰 ገቢ ያግኙ":
        await update.message.reply_text("💰 የሪፈራል ስርዓት በቅርቡ ይጨመራል።")

    elif text == "👥 የግብዣ ሊንክ":
        await update.message.reply_text("👥 የሪፈራል ሊንክዎ በቅርቡ ይታያል።")

    elif text == "ℹ️ ስለ Dani Hub":
        await update.message.reply_text("ℹ️ Dani Hub የክርስቲያን መንፈሳዊ ቦት ነው።")

    elif text == "📞 አስተዳዳሪ":
        await update.message.reply_text("📞 @mr_dani10")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

app.run_polling()