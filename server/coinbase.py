from urllib.parse import quote

import requests

from validators import validate_coin, validate_period

REQUEST_TIMEOUT = 10


def get_coins_summary():
    response = requests.get(
        'https://coinbase.com/api/v2/assets/summary',
        params={
            'include_prices': 'true',
            'resolution': 'week',
            'filter': 'listed',
            'base': 'USD',
        },
        timeout=REQUEST_TIMEOUT,
    )
    return response.json()


def get_coins_search():
    response = requests.get(
        'https://coinbase.com/api/v2/assets/search',
        params={
            'base': 'USD',
            'filter': 'listed',
            'include_prices': 'true',
            'resolution': 'week',
        },
        timeout=REQUEST_TIMEOUT,
    )
    return response.json()


def get_coins_histories(coin, period):
    # Kullanici girdisini allowlist ile dogrula ve URL-encode et (SSRF korumasi).
    coin = validate_coin(coin)
    period = validate_period(period)

    response = requests.get(
        f'https://api.coinbase.com/v2/prices/{quote(coin, safe="")}-USD/historic',
        params={'sort': 'rank', 'period': period},
        timeout=REQUEST_TIMEOUT,
    )
    return response.json()
