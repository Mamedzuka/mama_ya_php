import requests
import asyncio

api_key = "aa6fed8b-52c6-47bb-b206-601103e8b126"

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters_usd = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

parameters_rub = {
    'start': '1',
    'limit': '5',
    'convert': 'RUB'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

coins = {}

bold_start = '033[1m'
bold_end = '033[10'

async def coin_prices_updater(updating_time):
    global coins
    while True:
        json_usd = requests.get(url, params=parameters_usd, headers=headers).json()
        json_rub = requests.get(url, params=parameters_rub, headers=headers).json()
        coins_usd = json_usd['data']
        coins_rub = json_rub['data']

        for coin in coins_usd:
            coins[coin['symbol']] = [coin['quote']['USD']['price']]
        for coin in coins_rub:
            coins[coin['symbol']] += [coin['quote']['RUB']['price']]
        print('Prices updated')
        await asyncio.sleep(updating_time)


def bitcoin_price_loader():
    return f"*BTC*:\n{'_USD_ -':<8}{coins['BTC'][0]:.2f}\n{'_RUB_ -':<8}{coins['BTC'][1]:.2f}"


def ethereum_price_loader():
    return f"*ETH*:\n{'_USD_ -':<8}{coins['ETH'][0]:.2f}\n{'_RUB_ -':<8}{coins['ETH'][1]:.2f}"
def ethereum_price_loader():
    return f"*ETH*:\n{'_USD_ -':<8}{coins['ETH'][0]:.2f}\n{'_RUB_ -':<8}{coins['ETH'][1]:.2f}"



def usd_coin_price_loader():
    return f"*USDC*:\n{'_USD_ -':<8}{coins['USDC'][0]:.8f}\n{'_RUB_ -':<8}{coins['USDC'][1]:.8f}"

def usd_coin_price_loader():
    return f"*USDC*:\n{'_USD_ -':<8}{coins['USDC'][0]:.8f}\n{'_RUB_ -':<8}{coins['USDC'][1]:.8f}"

def top_five_price_loader():
    top_five_str = ""
    for coin_key, coin_item in coins.items():
        top_five_str += f"*{coin_key}*:\n{'_USD_ -':<8}{coin_item[0]:.8f}\n{'_RUB_ -':<8}{coin_item[1]:.8f}\n"
    return top_five_str


