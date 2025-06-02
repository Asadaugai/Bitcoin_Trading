
# Without TRB
import os
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
    print(sentiment_result)












'''import os
from twitter import main as tweet_fetch
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
    # Prepare prompt with tweets data
    prompt = f"""
    You are a Bitcoin market expert. Analyze these tweets from influential people and 
    determine the overall market sentiment for Bitcoin.

    Here are the tweets:
    {tweets_dict}
    
    Consider the importance of each person in the context of Bitcoin:
    - Elon Musk, Cathie Wood, and President Bukele have very high influence on Bitcoin markets
    - JPMorgan and Donald Trump have moderate influence
    - Adjust importance for others based on their crypto market relevance
    
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
    tweets_dict = tweet_fetch()
    # Get and print sentiment analysis
    sentiment_result = analyze_bitcoin_sentiment(tweets_dict)
    print(sentiment_result)'''

















