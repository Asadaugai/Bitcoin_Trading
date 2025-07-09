
# Fetech data for 1 hour
'''import ccxt
import pandas as pd
import numpy as np


def fetch_ohlcv(exchange, symbol, timeframe='1m', limit=60):
    return exchange.fetch_ohlcv(symbol, timeframe, limit=limit)


def compute_rsi(prices, period=14):
    deltas = np.diff(prices)
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    avg_gain = np.mean(gains[-period:]) if gains else 0
    avg_loss = np.mean(losses[-period:]) if losses else 1e-10  # Avoid division by zero
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def compute_atr(highs, lows, closes, period=14):
    tr = [max(highs[i] - lows[i],
              abs(highs[i] - closes[i - 1]),
              abs(closes[i - 1] - lows[i]))
          for i in range(1, len(closes))]
    return np.mean(tr[-period:]) / closes[-1] * 100 if tr else 0


def compute_volatility(prices):
    returns = np.diff(prices) / prices[:-1]
    return pd.Series(returns).std() * 100


def fetch_order_book_metrics(exchange, symbol, current_price):
    order_book = exchange.fetch_order_book(symbol, limit=10)
    bid = order_book['bids'][0][0] if order_book['bids'] else current_price
    ask = order_book['asks'][0][0] if order_book['asks'] else current_price
    spread = ((ask - bid) / bid) * 100
    return bid, ask, spread


def fetch_binance_1h_metrics(symbol='BTC/USDT'):
    try:
        exchange = ccxt.binance()

        ohlcv = fetch_ohlcv(exchange, symbol)
        closes = [c[4] for c in ohlcv]
        highs = [c[2] for c in ohlcv]
        lows = [c[3] for c in ohlcv]
        volumes = [c[5] for c in ohlcv]

        current_price = closes[-1]
        avg_volume = np.mean(volumes)
        volatility = compute_volatility(closes)
        price_change = ((closes[-1] - closes[0]) / closes[0]) * 100
        rsi = compute_rsi(closes)
        atr = compute_atr(highs, lows, closes)
        bid, ask, spread = fetch_order_book_metrics(exchange, symbol, current_price)
        moving_avg = np.mean(closes[-20:])
        momentum = closes[-1] - closes[0]
        hourly_high = max(highs)
        hourly_low = min(lows)

        return {
            "current_price": current_price,
            "average_volume_1h": avg_volume,
            "volatility_1h": volatility,
            "price_change_1h": price_change,
            "rsi_14": rsi,
            "atr_14": atr,
            "bid_price": bid,
            "ask_price": ask,
            "bid_ask_spread": spread,
            "moving_average_20": moving_avg,
            "momentum": momentum,
            "hourly_high": hourly_high,
            "hourly_low": hourly_low
        }

    except Exception as e:
        print(f"Error fetching data: {e}")
        return {
            "current_price": 0,
            "average_volume_1h": 0,
            "volatility_1h": 0,
            "price_change_1h": 0,
            "rsi_14": 50,
            "atr_14": 0,
            "bid_price": 0,
            "ask_price": 0,
            "bid_ask_spread": 0,
            "moving_average_20": 0,
            "momentum": 0,
            "hourly_high": 0,
            "hourly_low": 0
        }


if __name__ == "__main__":
    data = fetch_binance_1h_metrics()
    print("1-Hour Binance Data:", data)'''








# Fetch data for 4 hour
import ccxt
import pandas as pd
import numpy as np


def fetch_ohlcv(exchange, symbol, timeframe='1m', limit=240):
    return exchange.fetch_ohlcv(symbol, timeframe, limit=limit)


def compute_rsi(prices, period=14):
    deltas = np.diff(prices)
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    avg_gain = np.mean(gains[-period:]) if gains else 0
    avg_loss = np.mean(losses[-period:]) if losses else 1e-10
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def compute_atr(highs, lows, closes, period=14):
    tr = [max(highs[i] - lows[i],
              abs(highs[i] - closes[i - 1]),
              abs(closes[i - 1] - lows[i]))
          for i in range(1, len(closes))]
    return np.mean(tr[-period:]) / closes[-1] * 100 if tr else 0


def compute_volatility(prices):
    returns = np.diff(prices) / prices[:-1]
    return pd.Series(returns).std() * 100


def fetch_order_book_metrics(exchange, symbol, current_price):
    order_book = exchange.fetch_order_book(symbol, limit=10)
    bid = order_book['bids'][0][0] if order_book['bids'] else current_price
    ask = order_book['asks'][0][0] if order_book['asks'] else current_price
    spread = ((ask - bid) / bid) * 100
    return bid, ask, spread


def fetch_binance_4h_metrics(symbol='BTC/USDT'):
    try:
        exchange = ccxt.binance()

        ohlcv = fetch_ohlcv(exchange, symbol)
        closes = [c[4] for c in ohlcv]
        highs = [c[2] for c in ohlcv]
        lows = [c[3] for c in ohlcv]
        volumes = [c[5] for c in ohlcv]

        current_price = closes[-1]
        avg_volume = np.mean(volumes)
        volatility = compute_volatility(closes)
        price_change = ((closes[-1] - closes[0]) / closes[0]) * 100
        rsi = compute_rsi(closes)
        atr = compute_atr(highs, lows, closes)
        bid, ask, spread = fetch_order_book_metrics(exchange, symbol, current_price)
        moving_avg = np.mean(closes[-20:])
        momentum = closes[-1] - closes[0]
        high_4h = max(highs)
        low_4h = min(lows)

        return {
            "current_price": current_price,
            "average_volume_4h": avg_volume,
            "volatility_4h": volatility,
            "price_change_4h": price_change,
            "rsi_14": rsi,
            "atr_14": atr,
            "bid_price": bid,
            "ask_price": ask,
            "bid_ask_spread": spread,
            "moving_average_20": moving_avg,
            "momentum": momentum,
            "high_4h": high_4h,
            "low_4h": low_4h
        }

    except Exception as e:
        print(f"Error fetching data: {e}")
        return {
            "current_price": 0,
            "average_volume_4h": 0,
            "volatility_4h": 0,
            "price_change_4h": 0,
            "rsi_14": 50,
            "atr_14": 0,
            "bid_price": 0,
            "ask_price": 0,
            "bid_ask_spread": 0,
            "moving_average_20": 0,
            "momentum": 0,
            "high_4h": 0,
            "low_4h": 0
        }


if __name__ == "__main__":
    data = fetch_binance_4h_metrics()
    print("4-Hour Binance Data:", data)








#Fetching information for last 24 hours

'''import ccxt
import pandas as pd
import numpy as np

def fetch_binance_data(symbol='BTC/USDT', timeframe='1h', limit=24):
    """
    Fetch real-time Bitcoin market data from Binance API
    Args:
        symbol: Trading pair (default: BTC/USDT)
        timeframe: Candlestick timeframe (default: 1 hour)
        limit: Number of data points (default: 24 for last 24 hours)
    Returns:
        Dictionary with market metrics
    """
    try:
        exchange = ccxt.binance()
        
        # Fetch OHLCV data
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        prices = [candle[4] for candle in ohlcv]  # Closing prices
        volumes = [candle[5] for candle in ohlcv]  # Volumes
        highs = [candle[2] for candle in ohlcv]   # Highs
        lows = [candle[3] for candle in ohlcv]    # Lows
        
        # Current price and volume
        current_price = prices[-1]
        avg_volume = sum(volumes) / len(volumes)
        
        # Volatility (standard deviation of returns)
        returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
        volatility = pd.Series(returns).std() * 100
        
        # Price trend (24-hour price change %)
        price_change = ((prices[-1] - prices[0]) / prices[0]) * 100
        
        # Order book depth
        order_book = exchange.fetch_order_book(symbol, limit=10)
        bid_price = order_book['bids'][0][0] if order_book['bids'] else current_price
        ask_price = order_book['asks'][0][0] if order_book['asks'] else current_price
        bid_ask_spread = ((ask_price - bid_price) / bid_price) * 100
        
        # Relative Strength Index (RSI, 14-period)
        deltas = np.diff(prices)
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        avg_gain = np.mean(gains[-14:]) if gains else 0
        avg_loss = np.mean(losses[-14:]) if losses else 1e-10  # Avoid division by zero
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        # Average True Range (ATR) for volatility
        tr = [max(highs[i] - lows[i], abs(highs[i] - prices[i-1]), abs(prices[i-1] - lows[i])) for i in range(1, len(prices))]
        atr = np.mean(tr[-14:]) / current_price * 100 if tr else volatility  # ATR as % of price
        
        return {
            "current_price": current_price,
            "volume": avg_volume,
            "volatility": volatility,
            "price_change": price_change,
            "bid_ask_spread": bid_ask_spread,
            "rsi": rsi,
            "atr": atr
        }
    except Exception as e:
        print(f"Error fetching Binance data: {e}")
        return {
            "current_price": 0,
            "volume": 0,
            "volatility": 0,
            "price_change": 0,
            "bid_ask_spread": 0,
            "rsi": 50,
            "atr": 0
        }

if __name__ == "__main__":
    data = fetch_binance_data()
    print("Binance Data:", data)'''








# Fetching data for last 1 hour and last 4 hours

'''import ccxt
import pandas as pd
import numpy as np
import json

def compute_metrics(ohlcv, symbol, exchange, period_label):
    prices = [candle[4] for candle in ohlcv]  
    volumes = [candle[5] for candle in ohlcv]  
    highs = [candle[2] for candle in ohlcv]
    lows = [candle[3] for candle in ohlcv]

    current_price = prices[-1]
    avg_volume = sum(volumes) / len(volumes)

    # Volatility (standard deviation of returns)
    returns = [(prices[i] - prices[i - 1]) / prices[i - 1] for i in range(1, len(prices))]
    volatility = pd.Series(returns).std() * 100

    # Price change %
    price_change = ((prices[-1] - prices[0]) / prices[0]) * 100

    # Order book
    order_book = exchange.fetch_order_book(symbol, limit=10)
    bid_price = order_book['bids'][0][0] if order_book['bids'] else current_price
    ask_price = order_book['asks'][0][0] if order_book['asks'] else current_price
    bid_ask_spread = ((ask_price - bid_price) / bid_price) * 100

    # RSI (14-period)
    deltas = np.diff(prices)
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    avg_gain = np.mean(gains[-14:]) if len(gains) >= 14 else np.mean(gains)
    avg_loss = np.mean(losses[-14:]) if len(losses) >= 14 else np.mean(losses) or 1e-10
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    # ATR (% of price)
    tr = [
        max(highs[i] - lows[i], abs(highs[i] - prices[i - 1]), abs(prices[i - 1] - lows[i]))
        for i in range(1, len(prices))
    ]
    atr = np.mean(tr[-14:]) / current_price * 100 if len(tr) >= 14 else np.mean(tr) / current_price * 100

    return {
        f"current_price_{period_label}": current_price,
        f"volume_{period_label}": avg_volume,
        f"volatility_{period_label}": volatility,
        f"price_change_{period_label}": price_change,
        f"bid_ask_spread": bid_ask_spread,  # shared as same
        f"rsi_{period_label}": rsi,
        f"atr_{period_label}": atr
    }

def fetch_binance_metrics(symbol='BTC/USDT'):
    try:
        exchange = ccxt.binance()
        timeframe = '15m'

        # 1 Hour => last 4 candles of 15m
        ohlcv_1h = exchange.fetch_ohlcv(symbol, timeframe, limit=4)
        metrics_1h = compute_metrics(ohlcv_1h, symbol, exchange, '1h')

        # 4 Hours => last 16 candles of 15m
        ohlcv_4h = exchange.fetch_ohlcv(symbol, timeframe, limit=16)
        metrics_4h = compute_metrics(ohlcv_4h, symbol, exchange, '4h')

        with open("binance_metrics.json", "a") as f:
            json.dump({**metrics_1h, **metrics_4h}, f, indent=4)
        
        return {**metrics_1h, **metrics_4h}

        return {**metrics_1h, **metrics_4h}

    except Exception as e:
        print(f"Error fetching Binance data: {e}")
        return {}

if __name__ == "__main__":
    data = fetch_binance_metrics()

    # Output with placeholders as requested
    print(f"Last 1 Hour:")
    print(f" - Current Bitcoin Price: ${data.get('current_price_1h')}")
    print(f" - 1H Average Volume: {data.get('volume_1h')}")
    print(f" - 1H Volatility: {data.get('volatility_1h'):.2f}%")
    print(f" - 1H Price Change: {data.get('price_change_1h'):.2f}%")
    print(f" - 1H Bid-Ask Spread: {data.get('bid_ask_spread'):.2f}%")
    print(f" - 1H RSI: {data.get('rsi_1h'):.2f}")
    print(f" - 1H ATR (% of price): {data.get('atr_1h'):.2f}%")

    print(f"\nLast 4 Hours:")
    print(f" - Current Bitcoin Price: ${data.get('current_price_4h')}")
    print(f" - 4H Average Volume: {data.get('volume_4h')}")
    print(f" - 4H Volatility: {data.get('volatility_4h'):.2f}%")
    print(f" - 4H Price Change: {data.get('price_change_4h'):.2f}%")
    print(f" - 4H Bid-Ask Spread: {data.get('bid_ask_spread'):.2f}%")
    print(f" - 4H RSI: {data.get('rsi_4h'):.2f}")
    print(f" - 4H ATR (% of price): {data.get('atr_4h'):.2f}%")'''




