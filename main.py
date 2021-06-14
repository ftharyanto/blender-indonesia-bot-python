import os, re
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

updater = Updater(os.environ["BOT_TOKEN"])

channel_id = "@GaleriBlenderIndonesia"
group_id = "@Blender3DIndonesia"

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

# forward from
# reply_to = Update.message.reply_to_message
# reply_chat_id = reply_to.from.id

# if re.search('caption', reply_to):
#     reply_caption = reply_to.caption
# else:
#     reply_caption = ""


updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
