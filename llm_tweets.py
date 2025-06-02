import os
from twitter_fetecher import main as tweet_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_metrics(data):
    """
    Predict Bitcoin trading metrics using Groq's LLM based on tweets and market data
    Args:
        data: Dictionary with tweets (dict) and market_data (dict)
    Returns:
        Formatted string with trading metrics
    """
    tweets_dict = data["tweets"]
    market_data = data["market_data"]

    prompt = """
You are a Bitcoin trading expert. Your task is to analyze tweets from influential figures and market data to predict five critical trading metrics for Bitcoin.

### Instructions:
1. Assess tweets for market sentiment, considering the influence of each person:
   - Very High: Elon Musk, Cathie Wood
   - Moderate: JPMorgan, Donald Trump
   - Others: Adjust based on crypto relevance (e.g., CZ Binance, Vitalik Buterin)
2. Evaluate tweet tone (optimism, pessimism, regulatory hints, adoption signals).
3. Integrate market data to inform predictions:
   - Current Price: Current Bitcoin price
   - Volume: 24-hour average trading volume
   - Volatility: Standard deviation of returns (%)
   - Price Change: 24-hour price change (%)
   - Bid-Ask Spread: Spread between top bid and ask (%)
   - RSI: Relative Strength Index (14-period, 0-100)
   - ATR: Average True Range as % of price (14-period)
4. Predict the following metrics:
   - Buy Price: Recommended entry price, near current price or support level
   - Stop-Loss Price: Exit price below Buy Price to limit losses, based on ATR/volatility
   - Take-Profit Price: Exit price above Buy Price to secure profits, based on RSI/price trends
   - Stop-Loss Zone %: Percentage range below Buy Price, derived from ATR/volatility
   - Profit Zone %: Percentage range above Buy Price, derived from ATR/volatility
5. Adjust metrics dynamically:
   - High volatility/ATR: Widen Stop-Loss/Profit Zones
   - High RSI (>70): Conservative Take-Profit; Low RSI (<30): Aggressive Buy Price
   - High volume/price change: Stronger trend confirmation
   - Narrow bid-ask spread: Higher liquidity, tighter zones

### Market Data:
- Current Bitcoin Price: ${current_price}
- 24-Hour Average Volume: {volume}
- 24-Hour Volatility: {volatility:.2f}%
- 24-Hour Price Change: {price_change:.2f}%
- Bid-Ask Spread: {bid_ask_spread:.2f}%
- RSI (14-period): {rsi:.2f}
- ATR (% of price): {atr:.2f}%

### Output Format:
Return **ONLY** this exact format with no additional text, comments, or explanations. Use ': ' as the separator and numeric values (dollars for prices, percentages for zones):
Buy Price: $P
Stop-Loss Price: $S
Take-Profit Price: $T
Stop-Loss Zone %: SZ%
Profit Zone %: PZ%

### Example Output:
Buy Price: $69500
Stop-Loss Price: $67500
Take-Profit Price: $71500
Stop-Loss Zone %: 2.88%
Profit Zone %: 2.88%

### Tweets:
""".format(**market_data)

    for person, tweets in tweets_dict.items():
        clean_tweets = [tweet.strip() for tweet in tweets if tweet.strip()]
        formatted_tweets = "\n".join([f"- {tweet}" for tweet in clean_tweets])
        prompt += f"\n{person}:\n{formatted_tweets}\n"

    print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    print(prompt)
    print("\n===== END OF PROMPT =====\n\n")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192",
        temperature=0,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    data = tweet_fetch()
    metrics_result = analyze_bitcoin_metrics(data)
    print("\n===== BITCOIN TRADING METRICS =====")
    print(metrics_result)


'''import os
from twitter_fetecher import main as tweet_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(data):
    """
    Analyze Bitcoin sentiment and predict trading metrics using Groq's LLM
    Args:
        data: Dictionary with tweets (dict) and market_data (dict)
    Returns:
        Formatted string with sentiment and trading metrics
    """
    tweets_dict = data["tweets"]
    market_data = data["market_data"]

    prompt = """
You are a Bitcoin market expert and sentiment analyst. Your task is to analyze tweets from influential figures and market data to assess Bitcoin sentiment and predict trading metrics.

### Instructions:
1. For each person, consider their influence:
   - Very High: Elon Musk, Cathie Wood
   - Moderate: JPMorgan, Donald Trump
   - Adjust for others based on crypto relevance
2. Analyze tweet sentiment (tone, implications, optimism/pessimism).
3. Use market data to inform predictions.
4. Classify overall sentiment (summing to 100%):
   - very bullish
   - bullish
   - neutral
   - bearish
   - very bearish
5. Predict trading metrics:
   - Buy Price: Recommended entry price
   - Stop-Loss Price: Exit price to limit losses
   - Take-Profit Price: Exit price to secure profits
   - Stop-Loss Zone %: Percentage range below Buy Price, based on volatility
   - Profit Zone %: Percentage range above Buy Price, based on volatility
6. Adjust metrics based on market conditions (e.g., high volatility widens zones).

### Market Data:
- Current Bitcoin Price: ${current_price}
- 24-Hour Average Volume: {volume}
- 24-Hour Volatility (std of returns): {volatility:.2f}%

### Output Format:
Return **ONLY** the following format with no additional text, comments, explanations, or deviations. Use exactly ': ' as the separator and ensure all values are numeric (percentages for sentiment and zones, dollar amounts for prices):
very bullish: X%
bullish: Y%
neutral: Z%
bearish: A%
very bearish: B%
Buy Price: $P
Stop-Loss Price: $S
Take-Profit Price: $T
Stop-Loss Zone %: SZ%
Profit Zone %: PZ%

### Example Output:
very bullish: 25%
bullish: 35%
neutral: 30%
bearish: 10%
very bearish: 0%
Buy Price: $69500
Stop-Loss Price: $67500
Take-Profit Price: $71500
Stop-Loss Zone %: 2.88%
Profit Zone %: 2.88%

### Tweets:
""".format(**market_data)

    for person, tweets in tweets_dict.items():
        clean_tweets = [tweet.strip() for tweet in tweets if tweet.strip()]
        formatted_tweets = "\n".join([f"- {tweet}" for tweet in clean_tweets])
        prompt += f"\n{person}:\n{formatted_tweets}\n"

    print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    print(prompt)
    print("\n===== END OF PROMPT =====\n\n")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192",
        temperature=0,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    data = tweet_fetch()
    sentiment_result = analyze_bitcoin_sentiment(data)
    print("\n===== BITCOIN MARKET SENTIMENT AND TRADING METRICS =====")
    print(sentiment_result)'''






# Without TRB
'''import os
from twitter_fetecher import main as tweet_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

# Initialize Groq client with API key directly
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(tweets_dict):
    """
    Analyze Bitcoin sentiment using Groq's LLM

    Args:
        tweets_dict: Dictionary with person names as keys and their tweets as values

    Returns:
        Formatted sentiment analysis string
    """

    # Base prompt
    prompt = """
You are a Bitcoin market expert and sentiment analyst. Your task is to analyze the sentiment of tweets related to Bitcoin from a set of influential figures.

### Instructions:
1. For each person listed, consider their influence on the Bitcoin market:
    - **Very High Influence**: Elon Musk, Cathie
    - **Moderate Influence**: JPMorgan, Donald Trump
    - **Adjust influence** appropriately for any others based on known crypto relevance.

2. Based on their tweets, determine their **individual sentiment** toward Bitcoin. Consider their tone, implications, optimism or pessimism about markets, economics, technology, regulation, etc.

3. Weight each person's sentiment by their influence level to calculate the **overall Bitcoin market sentiment**.

4. Classify the final overall sentiment using these categories (must total 100%):
    - very bullish
    - bullish
    - neutral
    - bearish
    - very bearish

### Output Format:
Respond **ONLY** in this exact format (with no commentary or explanation):
very bullish: X% 
bullish: Y% 
neutral: Z% 
bearish: A% 
very bearish: B%

### Tweets by Persons are in following:
"""

    # Append tweets in a readable format
    for person, tweets in tweets_dict.items():
        clean_tweets = [tweet.strip() for tweet in tweets if tweet.strip()]
        formatted_tweets = "\n".join([f"- {tweet}" for tweet in clean_tweets])
        prompt += f"\n{person}:\n{formatted_tweets}\n"

    
    # Print the full prompt for validation
    print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    #print(prompt)
    print("\n===== END OF PROMPT =====\n\n")

    # Call Groq API
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        #model="llama-3.3-70b-versatile",
        model="llama3-70b-8192",
        temperature=0,
    )

    # Return sentiment analysis
    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    # Fetch tweets dictionary from Twitter module
    tweets_dict = tweet_fetch()

    # Get and print sentiment analysis
    sentiment_result = analyze_bitcoin_sentiment(tweets_dict)
    print(sentiment_result)'''

























