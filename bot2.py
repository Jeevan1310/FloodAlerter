from dotenv import load_dotenv
import os
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Location
load_dotenv()


print('Code running')

API_KEY=os.getenv("API_KEY")
updater = Updater(API_KEY,
                  use_context=True)

print("Passed")


  
  
def hi(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
    

def start(update: Update, context: CallbackContext):
    
    kbd_layout = [['Register', 'Status'], ['Help', 'Sponsor-us'],
                       ["Contact-us"]]

    kbd = ReplyKeyboardMarkup(kbd_layout)

    
    update.message.reply_text(text="Select Options", reply_markup=kbd)
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /help -to get help""")
  
  
def status(update: Update, context: CallbackContext):
    #Check for user if the user is registered for Fsaver
    update.message.reply_text(
        "Sorry we cannot get registeration details \
        please come back after some time)")
  
  
def sponsor(update: Update, context: CallbackContext):
    update.message.reply_text("By us a coffe so we can make lot of more activities ")
  
  
def contact(update: Update, context: CallbackContext):
    update.message.reply_text(
        "contact the builder for more details")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")


def remove(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """

    reply_markup = ReplyKeyboardRemove()

    # sending the reply so as to remove the keyboard
    update.message.reply_text(text="I'm back.", reply_markup=reply_markup)
    pass

def echo(update: Update, context: CallbackContext):
    """
    message to handle any "Option [0-9]" Regrex.
    """
    # sending the reply message with the selected option
    update.message.reply_text("You just clicked on '%s'" % update.message.text)
    update.message.reply_text("The option you have selected is for registering flood alert")
    kbd_layout = [['YES', 'NO']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text="Do you want continue ??", reply_markup=kbd)
    pass




def completed(update: Update, context: CallbackContext):
    update.message.reply_text(
        "You simply clicked '%s' As a result you have been succesfully registered for the Flood Alerting Service by Fsaver" % update.message.text
    )
    user = update.message.from_user
    print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
    kbd_layout = [['Thankyou']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text="You have done a good thing", reply_markup=kbd)
    pass
def incomplete(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Oh Sad you just clicked '%s' Please come back when you ready for the alert service" % update.message.text
    )
    pass
def tnx(update: Update,context: CallbackContext):
    update.message.reply_text(
        "Thank you for your wonderful support"
    )
    pass
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(CommandHandler("hi", hi))
updater.dispatcher.add_handler(CommandHandler("remove", remove))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"Register"), echo))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"Status"), status))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"Sponsor-us"), sponsor))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"Help"), help))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"Contact-us"), contact))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"YES"), completed))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"NO"), incomplete))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"Thankyou"), tnx))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

  
updater.start_polling()
updater.idle()