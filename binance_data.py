



import ccxt
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
    print("Binance Data:", data)










    '''import ccxt
import pandas as pd
from datetime import datetime, timedelta

def fetch_binance_data(symbol='BTC/USDT', timeframe='1h', limit=24):
    """
    Fetch real-time Bitcoin price, volume, and volatility from Binance API
    Args:
        symbol: Trading pair (default: BTC/USDT)
        timeframe: Candlestick timeframe (default: 1 hour)
        limit: Number of data points (default: 24 for last 24 hours)
    Returns:
        Dictionary with current_price, volume, and volatility
    """
    try:
        # Initialize Binance exchange
        exchange = ccxt.binance()
        
        # Fetch OHLCV (Open, High, Low, Close, Volume) data
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        
        # Extract prices and volumes
        prices = [candle[4] for candle in ohlcv]  # Closing prices
        volumes = [candle[5] for candle in ohlcv]  # Volumes
        
        # Calculate metrics
        current_price = prices[-1]  # Latest price
        avg_volume = sum(volumes) / len(volumes)  # Average 24-hour volume
        
        # Calculate volatility (standard deviation of returns)
        returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
        volatility = pd.Series(returns).std() * 100  # Volatility in percentage
        
        return {
            "current_price": current_price,
            "volume": avg_volume,
            "volatility": volatility
        }
    except Exception as e:
        print(f"Error fetching Binance data: {e}")
        return {"current_price": 0, "volume": 0, "volatility": 0}

if __name__ == "__main__":
    data = fetch_binance_data()
    print("Binance Data:", data)'''

