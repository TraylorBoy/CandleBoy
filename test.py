"""Tests the CandleBoy Module"""

from candleboy import CandleBoy

client = CandleBoy()


def test_utility():
    global client

    assert 'phemex' in client.exchanges()
    assert '1m' in client.timeframes(exchange='phemex')
    assert len(client.ohlcv(exchange='phemex',
                            symbol='BTC/USD:USD', tf='1m')) > 0
    assert len(client.ohlcv(exchange='phemex', symbol='BTC/USD:USD',
                            tf='1m', since=client.timestamp(exchange='phemex', date='2021-12-29'))) > 0


def test_macd():
    global client

    # Get closing values
    _, _, _, _, close, _ = client.ohlcv('phemex', 'BTC/USD:USD', '1m')
    macd, _, _ = client.macd(close)
    assert len(list(macd)) > 0


def test_ema():
    global client

    # Get closing values
    _, _, _, _, close, _ = client.ohlcv('phemex', 'BTC/USD:USD', '1m')
    ema = client.ema(close)
    assert len(ema) > 0


if __name__ == '__main__':
    test_utility()
    test_macd()
    test_ema()
    print('All tests passed')
