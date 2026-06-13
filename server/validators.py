import re

# Coinbase ticker sembolleri yalnizca harf, rakam ve kisa ayraclardan olusur.
# allowlist regex ile dogrulayarak SSRF / URL enjeksiyonunu engelliyoruz.
_COIN_RE = re.compile(r'^[A-Za-z0-9]{1,15}$')

# period yalnizca Coinbase'in destekledigi sabit degerlerden biri olabilir.
_ALLOWED_PERIODS = frozenset({'hour', 'day', 'week', 'month', 'year', 'all'})


def validate_coin(coin):
    """Coin sembolunu allowlist regex ile dogrula; gecersizse ValueError firlat."""
    if not isinstance(coin, str) or not _COIN_RE.match(coin):
        raise ValueError('Invalid coin symbol')
    return coin.upper()


def validate_period(period):
    """Period degerini sabit enum ile dogrula; gecersizse ValueError firlat."""
    if period not in _ALLOWED_PERIODS:
        raise ValueError('Invalid period')
    return period
