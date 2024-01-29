from telegram import Bot

TOKEN="6744430799:AAECPtL1iXE6RFFAyYXTKg9bAZL4xTICL-4"

bot = Bot(TOKEN)

last_update=bot.getUpdates()[-1]
user = last_update.message.from_user.id
message=last_update.message.text

bot.send_message(chat_id=user,text=message)