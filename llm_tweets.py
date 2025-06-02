
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

























