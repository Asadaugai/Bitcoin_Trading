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
























'''import os
from news_fetcher import main as news_fetch
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
    # Prepare prompt with tweets data
    prompt = f"""
    You are a Bitcoin market expert. Analyze these news articles and 
    determine the overall market sentiment for Bitcoin.

    Here are the articles:
    {articles_list}
    
    Consider the importance of different factors in the articles:
    - Regulatory news tends to have high impact
    - Institutional adoption news is very significant
    - Market movements and technical analysis have moderate impact
    - General crypto ecosystem news has some influence
    
    Classify the overall sentiment into these categories and provide percentages:
    very bullish, bullish, neutral, bearish, very bearish
    
    The percentages should add up to 100%. Format your response ONLY as:
    very bullish : X bullish : Y neutral : Z bearish : A very bearish: B
    """
    
    # Call Groq API
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )
    
    # Return the sentiment analysis
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    # Sample dictionary of tweets
    #tweets_dict = {'realDonaldTrump': ['', '', '', 'THE SUPREME COURT IS BEING PLAYED BY THE RADICAL LEFT LOSERS, WHO HAVE NO SUPPORT, THE PUBLIC HATES THEM, AND THEIR ONLY HOPE IS THE INTIMIDATION OF THE COURT, ITSELF. WE CAN’T LET THAT HAPPEN TO OUR COUNTRY!', 'Republicans MUST UNITE behind, “THE ONE, BIG BEAUTIFUL BILL!” Not only does it cut Taxes for ALL Americans, but it will kick millions of Illegal Aliens off of Medicaid to PROTECT it for those who are the ones in real need. The Country will suffer greatly without this Legislation,'], 'jpmorgan': ['Today, we hosted #JPMInvestorDay, where senior leaders shared updates on the firm’s long-term strategy to help advance employees, clients, and communities. https://jpmorganchase.com/ir/investor-day', 'At #JPMInvestorDay, Troy Rohrbaugh used private credit as an example of our client-centric and solutions driven approach.', 'Umar Farooq, co-head of Global Payments, shared how we’re making targeted investments to capture growth opportunities, across the Payments business.', 'This week, Boston became the hub for over 3,000 industry leaders and innovators during the 53rd annual #JPMTMC. \n\nInvestors, companies and thought leaders gathered to explore the key factors shaping the sector, exchanging insights on investment opportunities and the latest tech'], 'nayibbukele': ['Annual inflation rate:\n\n Venezuela: 172%\n Argentina: 47.3%\n Türkiye: 37.86%\n Nigeria: 23.71%\n Ukraine: 15.1%\n Lebanon: 14.2%\n Egypt: 13.9% \n Kazakhstan: 10.7%\n Russia: 10.2%\n Bangladesh: 9.17%\n Brazil: 5.53%\n Poland: 4.3%\n Hungary: 4.2%\n Serbia: 4.0%', '', 'Feel that?\n\nThat’s the system splitting at the seams.', 'A country on the rise…', 'It’s been a cold winter and cloudy spring, so last week I grabbed a flight from New York to El Salvador.\n\nThis was my third trip since 2023.\n\nI continue to be struck by how the country is changing between my visits, especially in terms of infrastructure. Projects that drag on for'], 'CathieDWood': ['Last month, BBC reported that GOSH, a research hospital in the UK, base edited the genome of a 12-year-old girl, Alyssa, suffering from leukemia. She had failed dozens of therapies and had no more options. Seven months later, she is cancer- free. Not many investors know about it.', 'Thank you, \n@elonmusk\n.', ' Yesss!!! ', 'I believe the Delaware court decision, forcing #Tesla to void the March 2018 vote on Elon Musk’s performance-based pay package, is un-American, an assault on investor rights, and an insult to the Board of Directors of one of the most stunningly successful companies in US history.', 'Based on her \n@TSLA\n ruling, DE Judge McCormick is an activist judge at its worst. No judge has the right to determine CEO compensation. Shareholders voted twice, overwhelmingly each time, to ratify \n@elonmusk\n’s 2018 performance-based pay package. She will lose this fight in Supreme']}
    news_list = news_fetch()
    # Get and print sentiment analysis
    sentiment_result = analyze_bitcoin_sentiment(news_list)
    print(sentiment_result)'''




