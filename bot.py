from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
🕊️ እንኳን ወደ Dani Hub በደህና መጡ!

ይህ መድረክ የተዘጋጀው የእግዚአብሔርን ቃል፣ መንፈሳዊ መልእክቶችን እና ጸሎትን ለማጋራት ነው።

📖 የመጽሐፍ ቅዱስ ቃል
🙏 ጸሎት
🌅 የዕለቱ መልእክት

እግዚአብሔር ይባርካችሁ!
"""
    await update.message.reply_text(message)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()