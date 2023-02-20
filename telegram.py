import requests
import urllib.request
from extensions import Money
import json
import telebot

t = open('tel_token.py', 'r', encoding='utf8')
TOKEN = t.read()
t.close()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_start(message):
    if message.chat.username == None:
        bot.send_message(message.chat.id, f"Приветствую, Незнакомец! Введи команду /help, если нужна помощь.")
    else:
        bot.send_message(message.chat.id, f"Приветствую, {message.chat.username}! Введи команду /help, если нужна помощь.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Введи через пробел: код валюты, из которой надо перевести, \n "
                                      "код валюты, в которую нужно конвертировать, \n "
                                      "и количество (если число не целое, то через точку). \n "
                                      "К примеру: RUB USD 99.99 \n "
                                      "Команда /value покажет все достуные валюты.")

@bot.message_handler(commands=['value'])
def send_value(message):
    all_value_pr = f"1. {Money.all_value[0][1]} - {Money.all_value[0][0]} \n" \
                   f"2. {Money.all_value[1][1]} - {Money.all_value[1][0]} \n" \
                   f"3. {Money.all_value[2][1]} - {Money.all_value[2][0]} \n" \
                   f"4. {Money.all_value[3][1]} - {Money.all_value[3][0]} \n" \
                   f"5. {Money.all_value[4][1]} - {Money.all_value[4][0]} \n" \
                   f"6. {Money.all_value[5][1]} - {Money.all_value[5][0]} \n" \
                   f"7. {Money.all_value[6][1]} - {Money.all_value[6][0]} \n" \
                   f"8. {Money.all_value[7][1]} - {Money.all_value[7][0]} \n" \
                   f"9. {Money.all_value[8][1]} - {Money.all_value[8][0]} \n" \
                   f"10. {Money.all_value[9][1]} - {Money.all_value[9][0]} \n" \
                   f"11. {Money.all_value[10][1]} - {Money.all_value[10][0]} \n" \
                   f"12. {Money.all_value[11][1]} - {Money.all_value[11][0]} \n" \
                   f"13. {Money.all_value[12][1]} - {Money.all_value[12][0]} \n" \
                   f"14. {Money.all_value[13][1]} - {Money.all_value[13][0]} \n" \
                   f"15. {Money.all_value[14][1]} - {Money.all_value[14][0]}"
    bot.send_message(message.chat.id, all_value_pr)

@bot.message_handler(content_types=['text'])
def get_text_rezult(message):
    try:
        alfa = message.text
        beta = alfa.split(' ')

        for i in Money.all_value:
            if beta[0] in i[1]:
                break

        for i in Money.all_value:
            if beta[1] in i[1]:
                break

    except IndexError:
        bot.send_message(message.chat.id, "Я вас не понимаю. Введите /help, если нужна помощь.")

    else:
        chis = None
        znam = None
        amount = None

        alfa = message.text
        beta = alfa.split(' ')

        for i in Money.all_value:
            if beta[0] in i[1]:
                chis = beta[0]
                break
            else:
                chis = None

        if chis == None:
            bot.send_message(message.chat.id, f"Я не знаю такую валюту: {beta[0]}. Введите /value, если нужна подсказка.")

        for i in Money.all_value:
            if beta[1] in i[1]:
                znam = beta[1]
                break
            else:
                znam = None

        if znam == None:
            bot.send_message(message.chat.id, f"Я не знаю такую валюту: {beta[1]}. Введите /value, если нужна подсказка.")

        try:
            amount = float(beta[2])
        except ValueError:
            bot.send_message(message.chat.id, f"{beta[2]} - не число.")
        except TypeError:
            bot.send_message(message.chat.id, "Числе через . - не через ,")

        if not chis == None and not znam == None and not amount == None:
            try:
                data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
                if chis == 'RUB':
                    base = 1
                else:
                    base = data['Valute'][chis]['Value']
                if znam == 'RUB':
                    quote = 1
                else:
                    quote = data['Valute'][znam]['Value']
                rezult = Money.get_price(base, quote, amount)
                bot.send_message(message.chat.id, f"{amount} {chis} это {rezult} {znam}")
            except ParseError:
                bot.send_message(message.chat.id, "Соответствует ошибке 400")
            except NotFound:
                bot.send_message(message.chat.id, "Соответствует ошибке 404")
            except MethodNotAllowed:
                bot.send_message(message.chat.id, "Соответствует ошибке 405")
        else:
            bot.send_message(message.chat.id, "Измените значения и попробуйте ещё раз!")

bot.polling(none_stop=True)