# For 1 hour data
'''import os
from news_fetecher_time import main as news_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
import schedule
import time
from datetime import datetime

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(data):
    """
    Predict Bitcoin market sentiment using Groq's LLM based on news and market data
    Args:
        data: Dictionary with articles (list) and market_data (dict)
    Returns:
        Formatted string with sentiment percentages
    """
    articles_list = data["articles"]
    market_data = data["market_data"]
    
    prompt = """
You are a financial analyst specializing in Bitcoin markets. Your task is to analyze recent news articles and 1-hour market data to predict the overall market sentiment for Bitcoin, classified into five categories with percentages summing to 100%.

### Instructions:
1. Analyze news articles, prioritizing:
   - Regulatory actions (e.g., bans, approvals): Very high impact
   - Institutional moves (e.g., ETF approvals, corporate adoption): High impact
   - Market trends (e.g., price movements, adoption): Moderate impact
   - General crypto news (e.g., tech updates): Low impact

2. Use the following **1-hour** market data to contextualize sentiment. These data points help assess short-term momentum and sentiment:
   - Current Price: Current Bitcoin price
   - Average Volume: Higher volume confirms trend strength
   - Volatility: Standard deviation of returns (high volatility may signal uncertainty)
   - Price Change: 1H price change % (positive/negative trend)
   - RSI (14): Overbought >70, Oversold <30
   - ATR (14): Higher values suggest greater volatility and emotional trading
   - Bid-Ask Spread: Calculated as (ask - bid) / ask * 100; narrow spreads imply strong liquidity
   - Moving Average (20): Used to determine whether current price is trending above or below short-term average
   - Momentum: Measures rate of change; positive indicates bullish pressure
   - Hourly High/Low: Assess range; tighter range suggests consolidation, wide range suggests volatility

3. Predict sentiment in five categories:
   - very bullish: Strong positive outlook (e.g., major adoption, price surge)
   - bullish: Moderately positive outlook
   - neutral: Balanced or unclear outlook
   - bearish: Moderately negative outlook
   - very bearish: Strong negative outlook (e.g., regulatory bans, price crash)

4. Ensure percentages sum to 100% and reflect combined news and 1-hour market data insights.

### Market Data (1H Only):
 - Current Bitcoin Price: ${current_price}
 - 1H Average Volume: {average_volume_1h}
 - 1H Volatility: {volatility_1h:.2f}%
 - 1H Price Change: {price_change_1h:.2f}%
 - 1H RSI (14): {rsi_14:.2f}
 - 1H ATR (14): {atr_14:.2f}%
 - 1H Bid Price: ${bid_price}
 - 1H Ask Price: ${ask_price}
 - 1H Bid-Ask Spread: {bid_ask_spread:.2f}%
 - 1H Moving Average (20): ${moving_average_20}
 - 1H Momentum: {momentum}
 - 1H High: ${hourly_high}
 - 1H Low: ${hourly_low}

### Output Format:
Return **ONLY** this exact format with no additional text, comments, or explanations. Use ': ' as the separator and numeric percentages:
very bullish: X%
bullish: Y%
neutral: Z%
bearish: A%
very bearish: B%

### Example Output:
very bullish: 20%
bullish: 30%
neutral: 40%
bearish: 10%
very bearish: 0%

### Articles:
""".format(**market_data)

    for i, article in enumerate(articles_list, 1):
        if article.strip():
            prompt += f"\nArticle {i}:\n{article.strip()}\n"

    #print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    #print(prompt)
    #print("\n===== END OF PROMPT =====\n\n")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        #model="llama3-70b-8192",
        model="Llama3-8b-8192",
     
        temperature=0,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    data = news_fetch()
    sentiment_result = analyze_bitcoin_sentiment(data)
    print("\n===== Data ======")
    print(data)
    print("\n===== BITCOIN MARKET SENTIMENT =====")
    print(sentiment_result)'''

'''import time

while True:
    if __name__ == "__main__":
        data = news_fetch()
        sentiment_result = analyze_bitcoin_sentiment(data)
        print("\n===== BITCOIN MARKET SENTIMENT =====")
        print(sentiment_result)

    # Wait for 1 hour (3600 seconds)
    time.sleep(3600)'''






# For 4 hour data
import os
from news_fetecher_time import main as news_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
import schedule
import time
from datetime import datetime

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(data):
    """
    Predict Bitcoin market sentiment using Groq's LLM based on news and market data
    Args:
        data: Dictionary with articles (list) and market_data (dict)
    Returns:
        Formatted string with sentiment percentages
    """
    articles_list = data["articles"]
    market_data = data["market_data"]
    
    prompt = """
You are a financial analyst specializing in Bitcoin markets. Your task is to analyze recent news articles and 4-hour market data to predict the overall market sentiment for Bitcoin, classified into five categories with percentages summing to 100%.

### Instructions:
1. Analyze news articles, prioritizing:
   - Regulatory actions (e.g., bans, approvals): Very high impact
   - Institutional moves (e.g., ETF approvals, corporate adoption): High impact
   - Market trends (e.g., price movements, adoption): Moderate impact
   - General crypto news (e.g., tech updates): Low impact

2. Use the following **4-hour** market data to contextualize sentiment. These data points reflect broader short-term market behavior and help identify momentum and volatility trends:
   - Current Price: Current Bitcoin price
   - Average Volume (4H): Higher volume confirms strength of movement
   - Volatility (4H): Higher volatility suggests uncertainty or breakout potential
   - Price Change (4H): Direction and strength of short-term price move
   - RSI (14): Overbought >70, Oversold <30
   - ATR (14): Measures recent volatility; high values indicate increased risk sentiment
   - Bid-Ask Spread: Calculated as (ask - bid) / ask * 100; narrower spread = more liquidity
   - Moving Average (20): Indicates direction of trend; price above MA = bullish bias
   - Momentum: Positive = bullish pressure; Negative = bearish pressure
   - 4H High/Low: Range boundaries help assess volatility and price pressure zones

3. Predict sentiment in five categories:
   - very bullish: Strong positive outlook (e.g., major adoption, price surge)
   - bullish: Moderately positive outlook
   - neutral: Balanced or unclear outlook
   - bearish: Moderately negative outlook
   - very bearish: Strong negative outlook (e.g., regulatory bans, price crash)

4. Ensure percentages sum to 100% and reflect combined insights from the news and 4-hour market data.

### Market Data (1H Only):
 - Current Bitcoin Price: ${current_price}
 - 4H Average Volume: {average_volume_4h}
 - 4H Volatility: {volatility_4h:.2f}%
 - 4H Price Change: {price_change_4h:.2f}%
 - 4H RSI (14): {rsi_14:.2f}
 - 4H ATR (14): {atr_14:.2f}%
 - 4H Bid Price: ${bid_price}
 - 4H Ask Price: ${ask_price}
 - 4H Bid-Ask Spread: {bid_ask_spread:.2f}%
 - 4H Moving Average (20): ${moving_average_20}
 - 4H Momentum: {momentum}
 - 4H High: ${high_4h}
 - 4H Low: ${low_4h}


### Output Format:
Return **ONLY** this exact format with no additional text, comments, or explanations. Use ': ' as the separator and numeric percentages:
very bullish: X%
bullish: Y%
neutral: Z%
bearish: A%
very bearish: B%

### Example Output:
very bullish: 20%
bullish: 30%
neutral: 40%
bearish: 10%
very bearish: 0%

### Articles:
""".format(**market_data)

    for i, article in enumerate(articles_list, 1):
        if article.strip():
            prompt += f"\nArticle {i}:\n{article.strip()}\n"

    #print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    #print(prompt)
    #print("\n===== END OF PROMPT =====\n\n")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        #model="llama3-70b-8192",
        model="Llama3-8b-8192",
     
        temperature=0,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    data = news_fetch()
    sentiment_result = analyze_bitcoin_sentiment(data)
    print("\n===== Data ======")
    print(data)
    print("\n===== BITCOIN MARKET SENTIMENT =====")
    print(sentiment_result)

'''import time

while True:
    if __name__ == "__main__":
        data = news_fetch()
        sentiment_result = analyze_bitcoin_sentiment(data)
        print("\n===== BITCOIN MARKET SENTIMENT =====")
        print(sentiment_result)

    # Wait for 1 hour (3600 seconds)
    time.sleep(3600)'''
