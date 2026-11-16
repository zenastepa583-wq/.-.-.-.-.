import io
import pyautogui
import telebot

BOT_TOKEN = "8191224863:AAHCI6iCZHmEUFJkQYhGA_aaBiaXNbscctI"
ALLOWED_USERNAME = "Gro0und"  # ваш юзернейм без знака @

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  # Проверяем, есть ли у пользователя юзернейм и совпадает ли он с вашим
  if (
      message.from_user.username is None
      or message.from_user.username.lower() != ALLOWED_USERNAME.lower()
  ):
    return

  if message.text and message.text.lower().strip() == "скриншот":
    screenshot = pyautogui.screenshot()
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    bot.send_photo(message.chat.id, img_bytes)


bot.polling(none_stop=True)
