import os
from twitter_fetecher import main as tweet_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(data):
    """
    Predict Bitcoin market sentiment using Groq's LLM based on tweets and market data
    Args:
        data: Dictionary with tweets (dict) and market_data (dict)
    Returns:
        Formatted string with sentiment percentages
    """
    tweets_dict = data["tweets"]
    market_data = data["market_data"]

    prompt = """
You are a Bitcoin market analyst. Your task is to analyze tweets from influential figures and market data to predict the overall market sentiment for Bitcoin, classified into five categories with percentages summing to 100%.

### Instructions:
1. Analyze tweets, considering each person's influence:
   - Very High: Elon Musk, Cathie Wood
   - Moderate: JPMorgan, Donald Trump
   - Others: Adjust based on crypto relevance (e.g., CZ Binance, Vitalik Buterin)
2. Evaluate tweet tone (optimism, pessimism, regulatory hints, adoption signals).
3. Use market data to contextualize sentiment:
   - Current Price: Current Bitcoin price
   - Volume: 24-hour average trading volume (high volume strengthens sentiment)
   - Volatility: Standard deviation of returns (high volatility may signal uncertainty)
   - Price Change: 24-hour price change % (positive/negative trends influence sentiment)
   - Bid-Ask Spread: Spread % (narrow spread indicates liquidity, stable sentiment)
   - RSI: Relative Strength Index (overbought >70, oversold <30 affects sentiment)
   - ATR: Average True Range % (high ATR suggests volatile sentiment)
4. Predict sentiment in five categories:
   - very bullish: Strong positive outlook (e.g., major adoption, price surge)
   - bullish: Moderately positive outlook
   - neutral: Balanced or unclear outlook
   - bearish: Moderately negative outlook
   - very bearish: Strong negative outlook (e.g., regulatory concerns, price drop)
5. Ensure percentages sum to 100% and reflect combined tweet and market data insights.

### Market Data:
- Current Bitcoin Price: ${current_price}
- 24-Hour Average Volume: {volume}
- 24-Hour Volatility: {volatility:.2f}%
- 24-Hour Price Change: {price_change:.2f}%
- Bid-Ask Spread: {bid_ask_spread:.2f}%
- RSI (14-period): {rsi:.2f}
- ATR (% of price): {atr:.2f}%

### Output Format:
Return **ONLY** this exact format with no additional text, comments, or explanations. Use ': ' as the separator and numeric percentages:
very bullish: X%
bullish: Y%
neutral: Z%
bearish: A%
very bearish: B%

### Example Output:
very bullish: 25%
bullish: 35%
neutral: 30%
bearish: 10%
very bearish: 0%

### Tweets:
""".format(**market_data)

    for person, tweets in tweets_dict.items():
        clean_tweets = [tweet.strip() for tweet in tweets if tweet.strip()]
        formatted_tweets = "\n".join([f"- {tweet}" for tweet in clean_tweets])
        prompt += f"\n{person}:\n{formatted_tweets}\n"

    #print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    #print(prompt)
    #print("\n===== END OF PROMPT =====\n\n")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192",
        temperature=0,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    data = tweet_fetch()
    sentiment_result = analyze_bitcoin_sentiment(data)
    #print("\n===== BITCOIN MARKET SENTIMENT =====")
    #print(sentiment_result)



