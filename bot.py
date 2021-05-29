from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule
import tweepy
import time

CONSUMER_KEY = 'Qvhe4Nxs05zr60gxvIwwhv0oW'  #environ['CONSUMER_KEY']
CONSUMER_SECRET = 'mUPcEy62LkXPVV5UWRXGgronpHAtoJO29o5qHDHo0Y6Ky39hf7'  # environ['CONSUMER_SECRET']
ACCESS_KEY = '1356366441612599297-O5ocnNWpRQKHtTtjXCai6RFmUN0yhT'  # environ['ACCESS_KEY']
ACCESS_SECRET = 'MnuxATNMArIzyWfmQqP8BNwYPphng9MsbbE3oQzdEqSxz'

# AUTH

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()


def bot_send_text(bot_message):

    bot_token = ''
    bot_chatID = '1444121534'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response


def btc_scraping():
    url_btc = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    url_etherium = requests.get('https://awebanalysis.com/es/coin-details/ethereum/')
    url_lite = requests.get('https://awebanalysis.com/es/coin-details/litecoin/')
    url_bch = requests.get('https://awebanalysis.com/es/coin-details/bitcoin-cash/')
    url_bincoin = requests.get('https://awebanalysis.com/es/coin-details/binance-coin/')
    url_doge = requests.get('https://awebanalysis.com/es/coin-details/dogecoin/')
    url_neo = requests.get('https://awebanalysis.com/es/coin-details/neo/')
    url_iota = requests.get('https://awebanalysis.com/es/coin-details/iota/')

    soup_btc = BeautifulSoup(url_btc.content, 'html.parser')
    soup_ethereum = BeautifulSoup(url_etherium.content, 'html.parser')
    soup_bch = BeautifulSoup(url_bch.content, 'html.parser')
    soup_bincoin = BeautifulSoup(url_bincoin.content, 'html.parser')
    soup_doge = BeautifulSoup(url_doge.content, 'html.parser')
    soup_lite = BeautifulSoup(url_lite.content, 'html.parser')
    soup_neo = BeautifulSoup(url_neo.content, 'html.parser')
    soup_iota = BeautifulSoup(url_iota.content, 'html.parser')

    btc_ = soup_btc.find('td',
                         {'class': 'wbreak_word align-middle coin_price'})
    ethereum_ = soup_ethereum.find(
        'td', {'class': 'wbreak_word align-middle coin_price'})
    bch_ = btc_ = soup_bch.find(
        'td', {'class': 'wbreak_word align-middle coin_price'})
    btc_ = soup_btc.find('td',
                         {'class': 'wbreak_word align-middle coin_price'})
    bincoin_ = soup_bincoin.find(
        'td', {'class': 'wbreak_word align-middle coin_price'})
    doge_ = soup_doge.find('td',
                           {'class': 'wbreak_word align-middle coin_price'})
    lite_ = soup_lite.find('td',
                           {'class': 'wbreak_word align-middle coin_price'})
    neo_ = soup_neo.find('td',
                         {'class': 'wbreak_word align-middle coin_price'})
    iota_ = soup_iota.find('td',
                           {'class': 'wbreak_word align-middle coin_price'})

    txt_btc = btc_.text
    txt_ethereum = ethereum_.text
    txt_bch = bch_.text
    txt_bincoin = bincoin_.text
    txt_doge = doge_.text
    txt_lite = lite_.text
    txt_neo = neo_.text
    txt_iota = iota_.text

    msg = 'Bitcoin (BTC) ----------> ' + txt_btc + '\nEthereum (ETH) ---------> ' + txt_ethereum + '\nLitecoin (LTC) ---------> ' + txt_lite + '\nNEO (NEO) --------------> ' + txt_neo + '\nIOTA (ETH) -------------> ' + txt_iota + '\nDogecoin (DOGE) --------> ' + txt_doge  #+ '\nBitcoin Cash(BCH) ---------> ' + txt_bch +  '\nBinance-Coin (BNB) ---------> ' + txt_bincoin
    print(msg)
    return msg


def report():
    msg = btc_scraping()

    bot_send_text(msg)

    api.update_status(msg)


if __name__ == '__main__':

    report()
    schedule.every(8).hours.do(report)

    while True:
        schedule.run_pending()
"""
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
"""
