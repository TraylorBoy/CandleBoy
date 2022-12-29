"""Crypto exchange indicator application"""
__version__ = '1.0.0'

import ccxt
import talib
import numpy


class CandleBoy:
    def __init__(self):
        self.phemex_client = ccxt.phemex()

# ------------------------------ Utility Methods ----------------------------- #

    def exchanges(self):
        """Returns a list of available exchanges"""
        return ['phemex']

    def timeframes(self, exchange):
        """Retrieve all timeframes available for exchange

        exchange (String) - Exchange code to retrieve timeframes from (ex. phemex)
        """
        if exchange == 'phemex':
            return self.phemex_client.timeframes

    def timestamp(self, date):
        """Creates UTC timestamp from date

        date (String) - Date to convert to timestamp, YEAR-MONTH-DAY (ex. 2018-12-01)
        """
        formatted_date = date + 'T00:00:00Z'
        return self.phemex_client.parse8601(formatted_date)

    def ohlcv(self, exchange, symbol, tf, since=None):
        """Retrieve the open - high - low - close - volume data from exchange

        exchange (String) - Exchange code to retrieve OHLCV data from
        symbol (String) - Pairing to retrieve OHLCV data for
        tf (String) - Timeframe for OHLCV data
        since (UTC Timestamp) - Optional start date for retrieving OHLCV data
        (requires UTC timestamp)
        """
        timestamps = []
        open = []
        high = []
        low = []
        close = []
        volume = []

        if exchange == 'phemex':
            self.phemex_client.load_markets(True)
            candles = self.phemex_client.fetch_ohlcv(
                symbol, tf, since, limit=1000)
            # First value is timestamp
            # Then the following values are:
            # Open, High, Low, Close, Volume
            for candle in candles:
                timestamps.append(candle[0])
                open.append(candle[1])
                high.append(candle[2])
                low.append(candle[3])
                close.append(candle[4])
                volume.append(candle[5])

            return timestamps, open, high, low, close, volume

# ------------------------------ Client Methods ------------------------------ #

    def macd(self, close, fastperiod=12, slowperiod=26, signalperiod=9):
        """Returns the Moving Average Convergence/Divergence indicator values

        See TA-Lib docs for details on parameters.
        https://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html
        """
        # Format
        close = numpy.array(close, dtype=float)

        # Get indicator values
        macd, macdsignal, macdhist = talib.MACD(
            close, fastperiod, slowperiod, signalperiod)

        return macd, macdsignal, macdhist

    def ema(self, close, timeperiod=200):
        """Returns the Exponential Moving Average indicator values

        See TA-Lib docs for details on parameters
        """
        # Format
        close = numpy.array(close, dtype=float)

        # Get indicator values
        real = talib.EMA(close, timeperiod)

        return real
