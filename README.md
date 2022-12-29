# CandleBoy
Crypto exchange indicator application

## Todo
- Add more indicators
- Add more exchanges
- Add charting

## Notes
- Only exchange is Phemex, they require specific symbols for SPOT and FUTURE
- SPOT Symbols start with *s* and are handled in USDT ex. sBTCUSDT
- FUTURE Symbols are all formatted as so *BTC/USD:USD*

## Installation
- Requires TA-Lib which may be difficult to install
- Here is their install docs https://mrjbq7.github.io/ta-lib/install.html

```
pip install candleboy
```

## Usage
### Instantiation
```
client = CandleBoy()
```
### Retrieve list of currently supported exchanges
```
client.exchanges()
```

### Get a list of all available timeframes for an exchange
```
client.timeframes(exchange='phemex')
```

### Retrieve Open, High, Low, Close, Volume data from exchange
- Some exchanges may return different values
- Retrieves 1000 candles for phemex
```
# -- Phemex -- #
timestamps, open, high, low, close, volume = client.ohlcv(exchange='phemex', symbol='BTC/USD:USD', tf='1m')

# Use a start at date
timestamp = client.timestamp('2021-12-29') # YEAR-MONTH-DATE
timestamps, open, high, low, close, volume = client.ohlcv(exchange='phemex', symbol='BTC/USD:USD', tf='1m', since=timestamp)
```

### Get Moving Average Convergence/Divergence Indicator Values
```
_, _, _, _, close, _ = client.ohlcv('phemex', 'BTC/USD:USD', '1m')
macd, signal, histogram = client.macd(close)

# May optionally change parameters (default is 12, 26, 9)
fastperiod=9
slowperiod=12
signalperiod=3

macd, signal, histogram = client.macd(close, fastperiod, slowperiod, signalperiod)
```

### Get Exponential Moving Average Indicator Values
```
_, _, _, _, close, _ = client.ohlcv('phemex', 'BTC/USD:USD', '1m')
ema = client.ema(close)

# May optionally change parameters (default is 200)
timeperiod = 20

ema = client.ema(close, timeperiod)
```

## Test

- Runs the tests on the CandleBoy module

```
make test
```

or

```
python3 test
