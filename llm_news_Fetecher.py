import os
from news_fetcher import main as news_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_metrics(data):
    """
    Predict Bitcoin trading metrics using Groq's LLM based on news and market data
    Args:
        data: Dictionary with articles (list) and market_data (dict)
    Returns:
        Formatted string with trading metrics
    """
    articles_list = data["articles"]
    market_data = data["market_data"]
    
    prompt = """
You are a financial analyst specializing in Bitcoin trading. Your task is to analyze recent news articles and market data to predict five critical trading metrics for Bitcoin.

### Instructions:
1. Use news articles to assess market sentiment and events, prioritizing:
   - Regulatory actions (e.g., bans, approvals): High impact
   - Institutional moves (e.g., ETF approvals, corporate adoption): High impact
   - Market trends (e.g., price movements, adoption): Moderate impact
   - General crypto news (e.g., tech updates): Low impact
2. Integrate market data to inform predictions:
   - Current Price: Current Bitcoin price
   - Volume: 24-hour average trading volume
   - Volatility: Standard deviation of returns (%)
   - Price Change: 24-hour price change (%)
   - Bid-Ask Spread: Spread between top bid and ask (%)
   - RSI: Relative Strength Index (14-period, 0-100)
   - ATR: Average True Range as % of price (14-period)
3. Predict the following metrics:
   - Buy Price: Recommended entry price, near current price or support level
   - Stop-Loss Price: Exit price below Buy Price to limit losses, based on ATR/volatility
   - Take-Profit Price: Exit price above Buy Price to secure profits, based on RSI/price trends
   - Stop-Loss Zone %: Percentage range below Buy Price, derived from ATR/volatility
   - Profit Zone %: Percentage range above Buy Price, derived from ATR/volatility
4. Adjust metrics dynamically:
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
Buy Price: $70000
Stop-Loss Price: $68000
Take-Profit Price: $72000
Stop-Loss Zone %: 2.86%
Profit Zone %: 2.86%

### Articles:
""".format(**market_data)

    for i, article in enumerate(articles_list, 1):
        if article.strip():
            prompt += f"\nArticle {i}:\n{article.strip()}\n"

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
    data = news_fetch()
    metrics_result = analyze_bitcoin_metrics(data)
    print("\n===== BITCOIN TRADING METRICS =====")
    print(metrics_result)



'''import os
from news_fetcher import main as news_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(data):
    """
    Analyze Bitcoin sentiment and predict trading metrics using Groq's LLM
    Args:
        data: Dictionary with articles (list) and market_data (dict)
    Returns:
        Formatted string with sentiment and trading metrics
    """
    articles_list = data["articles"]
    market_data = data["market_data"]
    
    prompt = """
You are a financial analyst specializing in Bitcoin markets. Your task is to analyze recent news articles and market data to assess Bitcoin market sentiment and predict trading metrics.

### Instructions:
1. Analyze the sentiment of the provided news articles, considering:
   - Regulatory actions (very high impact)
   - Institutional moves (high impact)
   - Market data/technical indicators (moderate impact)
   - Broader blockchain news (low impact)
2. Use market data (current price, volume, volatility) to inform predictions.
3. Classify overall sentiment into five categories (summing to 100%):
   - very bullish
   - bullish
   - neutral
   - bearish
   - very bearish
4. Predict trading metrics based on sentiment and market data:
   - Buy Price: Recommended price to enter a trade
   - Stop-Loss Price: Price to exit to limit losses
   - Take-Profit Price: Price to exit to secure profits
   - Stop-Loss Zone %: Percentage range below Buy Price, based on volatility
   - Profit Zone %: Percentage range above Buy Price, based on volatility
5. Adjust metrics dynamically based on market conditions (e.g., high volatility widens zones, high volume strengthens sentiment).

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
very bullish: 20%
bullish: 30%
neutral: 40%
bearish: 10%
very bearish: 0%
Buy Price: $70000
Stop-Loss Price: $68000
Take-Profit Price: $72000
Stop-Loss Zone %: 2.86%
Profit Zone %: 2.86%

### Articles:
""".format(**market_data)

    for i, article in enumerate(articles_list, 1):
        if article.strip():
            prompt += f"\nArticle {i}:\n{article.strip()}\n"

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
    data = news_fetch()
    sentiment_result = analyze_bitcoin_sentiment(data)
    print("\n===== BITCOIN MARKET SENTIMENT AND TRADING METRICS =====")
    print(sentiment_result)'''








# Without TRB
'''import os
from news_fetcher import main as news_fetch
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

# Initialize Groq client with API key directly
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_bitcoin_sentiment(articles_list):
    """
    Analyze Bitcoin sentiment using Groq's LLM based on news articles

    Args:
        articles_list: List of news articles or content about Bitcoin

    Returns:
        Formatted sentiment analysis string
    """

    prompt = """
You are a financial analyst specializing in Bitcoin and cryptocurrency markets. Your task is to analyze a set of recent news items — some may include full articles, summaries, or just titles — and assess the overall market sentiment regarding Bitcoin.

### Instructions:
1. For each item, do your best to interpret the sentiment (positive, negative, or neutral) toward Bitcoin, even if only a headline or summary is available.
2. If only a title or partial content is provided, make a reasonable judgment based on phrasing, keywords, and implications.
3. Ignore unrelated metadata or boilerplate text that is not relevant to market analysis.
4. Weight each item’s sentiment based on the **importance of its topic**:
   - Regulatory actions (e.g., bans, approvals, lawsuits, legislation) — very high impact
   - Institutional moves (e.g., ETFs, bank adoption, government positions) — high impact
   - Market data and technical indicators (e.g., price trends, volatility) — moderate impact
   - Broader blockchain/crypto news (e.g., general events, partnerships, innovations) — low impact
5. Combine the weighted sentiments into an overall market sentiment for Bitcoin.

### Classification Scale:
Your final sentiment analysis must classify the overall tone using **these five categories**, with values summing to 100%:
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

### List of Articles in Following:
"""


    # Add articles with clear formatting
    for i, article in enumerate(articles_list, 1):
        if article.strip():
            prompt += f"\nArticle {i}:\n{article.strip()}\n"

    # Print the full prompt for validation
    print("\n\n===== FINAL PROMPT SENT TO LLM =====\n")
    #print(prompt)
    print("\n===== END OF PROMPT =====\n\n")

    # Call Groq API
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    # Return the sentiment analysis
    return response.choices[0].message.content.strip()

# === Entry point ===
if __name__ == "__main__":
    # Fetch Bitcoin-related news articles
    news_list = news_fetch()

    # Run sentiment analysis
    sentiment_result = analyze_bitcoin_sentiment(news_list)

    # Print final sentiment output
    print("\n===== BITCOIN MARKET SENTIMENT =====")
    print(sentiment_result)
'''












