import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_articles(articles, max_chunk_size=5):
    """
    Summarize long list of articles into a concise version for sentiment analysis.
    Args:
        articles: List of article strings.
        max_chunk_size: Number of articles to include per summary chunk.
    Returns:
        A summarized string combining all summarized chunks.
    """
    summaries = []

    for i in range(0, len(articles), max_chunk_size):
        chunk = articles[i:i + max_chunk_size]
        chunk_text = "\n\n".join([f"Article {j+i+1}:\n{a}" for j, a in enumerate(chunk) if a.strip()])

        prompt = f"""
You are a financial news summarizer. Summarize the following Bitcoin-related news articles while preserving the most insightful and sentiment-relevant content. Focus on regulatory actions, institutional moves, market trends, and general crypto updates. Your summary should be concise and capture key points useful for market sentiment analysis.

### Articles:
{chunk_text}

### Summary:
(Summarize here)
"""

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="Llama3-8b-8192",
            temperature=0.3,
        )

        summaries.append(response.choices[0].message.content.strip())

    return "\n\n".join(summaries)
