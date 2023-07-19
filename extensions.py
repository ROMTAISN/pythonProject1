import json
import requests
from currency import keys


class APIExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIExeption(f'Невозможно конвертировать {base} в {quote}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIExeption(f'Не удалось обравотать валюту {quote}.')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIExeption(f'Не удалось обравотать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Введено неверное количество валюты для перевода. {amount} - не число')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base
