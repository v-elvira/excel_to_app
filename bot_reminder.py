import telebot
# @sales_reminder_bot

token = "5469710505:AAFgCaMVkLXjg_MhPW2-u9gqCTwlK_BWDMI"
my_chat_id = '1431762917'

bot = telebot.TeleBot(token)
bot.id_list = [my_chat_id]


@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.send_message(chat_id=message.chat.id,
                     text='Здесь будут напоминания о просроченных поставках \n')
    with open('id_list.txt', 'a') as file_storage:
        file_storage.write(str(message.chat.id)+'\n')

@bot.message_handler(commands=['stop'])
def handle_message(message):
    with open('id_list.txt', 'r') as file_storage:
        new_text = file_storage.read().replace(' ', '').replace(str(message.chat.id)+'\n', '')
    with open('id_list.txt', 'w') as file_storage:
        file_storage.write(new_text)
        bot.send_message(chat_id=message.chat.id,
                     text='Вы отписались от напоминаний \n')


def notify(records):
    val_text = '\n'. join(('№ {}, договор {} ({})'.format(*x) for x in records))

    try:
        with open('id_list.txt', 'r') as file_storage:
            id_set = set(map(str.strip, file_storage.readlines())) | set(bot.id_list)
            id_set -= {'', }
    except:
        id_set = set(bot.id_list)

    for chat in set(id_set):
        bot.send_message(chat_id=chat, text='Срок поставки истёк по заказам: \n' + val_text)


if __name__ == '__main__':
    bot.polling()
