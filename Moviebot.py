import os
import re
import telebot

bot = telebot.TeleBot("6216733418:AAE_DsESr0OBuyF1uKFg0RZkQ_fOn9YkwnM")

def filter_files(files):
  """Filters a list of files for MP4 and MKV files."""
  filtered_files = []
  for file in files:
    if re.match(r".*\.(mp4|mkv)$", file):
      filtered_files.append(file)
  return filtered_files

@bot.message_handler(commands=["movie"])
def movie_handler(message):
  """Handles movie requests."""
  files = os.listdir()
  filtered_files = filter_files(files)
  if filtered_files:
    bot.send_message(message.chat.id, "Here are the movies I found:")
    for file in filtered_files:
      bot.send_message(message.chat.id, f"* {file}")
  else:
    bot.send_message(message.chat.id, "I couldn't find any movies.")

bot.polling()

