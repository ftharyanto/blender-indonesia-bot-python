import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

channel_id = os.environ['CHANNEL_ID']
group_id = os.environ['GROUP_ID']

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def post(update: Update, context: CallbackContext) -> None:
    # forward from
    msg = update.effective_message
    reply_to = msg.reply_to_message


    if reply_to.caption:
        reply_caption = reply_to.caption
    else:
        reply_caption = ''

    if reply_to.from_user.username:
        reply_username = '@' + reply_to.from_user.username
    else:
        reply_username = f'{reply_to.from_user.first_name} {reply_to.from_user.last_name}'

    # check member status
    chat_id = msg.chat.id
    user_id = msg.from_user.id  
    message_id = msg.message_id
    ADMINS = ["creator", "administrator"]
    member_status = context.bot.get_chat_member(chat_id, user_id).status

    if member_status in ADMINS == 0:
        pass
    else:
        # check the filetype
        if reply_to.animation != None:
          file_id = reply_to.animation.file_id
          context.bot.sendAnimation(channel_id, file_id, caption = f'{reply_caption}\nby {reply_username}')
        elif reply_to.video != None:
          file_id = reply_to.video.file_id
          context.bot.sendVideo(channel_id, file_id, caption = f'{reply_caption}\nby {reply_username}')
        elif reply_to.photo != None:
          file_id = reply_to.photo[-1].file_id
          context.bot.sendPhoto(channel_id, file_id, caption = f'{reply_caption}\nby {reply_username}')
        elif type(reply_to.document) is str:
          file_id = reply_to.document.file_id
          context.bot.sendDocument(channel_id, file_id, caption = f'{reply_caption}\nby {reply_username}')
    context.bot.deleteMessage(group_id, message_id)
    
    
updater = Updater(os.environ['BOT_TOKEN'])
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('post', post))

updater.start_polling()
updater.idle()
