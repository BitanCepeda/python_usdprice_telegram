# Libraries
import requests
import schedule

# Conertion ready
url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()
coptousd = data["rates"]["COP"] / data["rates"]["USD"]
info = '1 usd is ' + str(round(coptousd, 3)) + ' cop. date: ' + data["date"]


# function definition
def bot_send_text(bot_message):
    bot_token = '<bot_token>'
    bot_chatID = '<bot_chatID>'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response


# main function - run evrey day at 08:00
if __name__ == '__main__':
    schedule.every().day.at("08:00").do(bot_send_text, info)
    while True:
        schedule.run_pending()
