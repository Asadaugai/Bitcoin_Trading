# Without TRB
import os
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













