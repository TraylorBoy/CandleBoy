# CandleBoy
Crypto exchange indicator application

## Notes
- Only exchange is Phemex so far, they require specific symbols for SPOT and FUTURE
- SPOT Symbols start with *s* and are handled in USDT ex. sBTCUSDT
- FUTURE Symbols are all formatted as so *BTC/USD:USD*
- Can create symbols with ```symbol``` method

## Installation
- Requires TA-Lib which may be difficult to install
- Here is their install docs https://mrjbq7.github.io/ta-lib/install.html

```
pip install candleboy
```

## Usage
### Instantiation
```
from candleboy.core import CandleBoy

# Only exchange at the moment is phemex
# Verbose shows logging
client = CandleBoy(exchange='phemex', verbose=True)

# Turn logging on/off
client.verbose()
client.silent()

# Access current exchange property
print(client.exchange)
```

### Get a list of all available timeframes for an exchange
```
client.timeframes()
```

### Retrieve Open, High, Low, Close, Volume data from exchange
- Some exchanges may return different values
- Retrieves 1000 candles for phemex
```
# Create symbol first
symbol = client.symbol(base='BTC', quote='USD', code='future') # BTC/USD:USD

timestamps, open, high, low, close, volume = client.ohlcv(symbol=symbol, tf='1m')

# Use a start at date
date = '2021-12-29' # YEAR-MONTH-DATE
timestamps, open, high, low, close, volume = client.ohlcv(symbol=symbol, tf='1m', since=date)
```

### Get Moving Average Convergence/Divergence Indicator Values
```
symbol = client.symbol(base='BTC', quote='USD', code='future')
_, _, _, _, close, _ = client.ohlcv(symbol, '1m')
macd, signal, histogram = client.macd(close)

# May optionally change parameters (default is 12, 26, 9)
fastperiod = 9
slowperiod = 12
signalperiod = 3

macd, signal, histogram = client.macd(close, fastperiod, slowperiod, signalperiod)
```

### Get Exponential Moving Average Indicator Values
```
symbol = client.symbol(base='BTC', quote='USD', code='future')
_, _, _, _, close, _ = client.ohlcv(symbol, '1m')
ema = client.ema(close)

# May optionally change parameters (default is 200)
timeperiod = 20

ema = client.ema(close, timeperiod)
```

### Get Stochastic Indicator Values
```
symbol = client.symbol(base='BTC', quote='USD', code='future')
_, _, high, low, close, _ = client.ohlcv(symbol, '1m')
slowk, slowd = client.stoch(high, low, close)

# May optionally change parameters (default is 5, 3, 0, 3, 0)
fastk_period = 5
slowk_period = 3
slowk_matype = 0
slowd_period = 3
slowd_matype = 0

slowk, slowd = client.stoch(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)
```

### Get ADX Indicator Values
```
symbol = client.symbol(base='BTC', quote='USD', code='future')
_, _, high, low, close, _ = client.ohlcv(symbol, '1m')
adx = client.adx(high, low, close)

# May optionally change parameters (default is 14)
timeperiod = 14

adx = client.stoch(high, low, close, timeperiod)
```

### Get MESA Indicator Values
```
symbol = client.symbol(base='BTC', quote='USD', code='future')
_, _, _, _, close, _ = client.ohlcv(symbol, '1m')
mama, fama = client.mesa(close)

# May optionally change parameters (default is 0.5, 0.05)
fastlimit = 0.5
slowlimit = 0.05

mama, fama = client.mesa(close, fastlimit, slowlimit)
```

## Test

- Runs the tests on the CandleBoy module

```
make test
```
