#Forcasting using crypto bert model and content of articles

from news_fetcher import fetch_coindesk_articles, fetch_cointelegraph_articles, fetch_bitcoinmagazine_articles, fetch_decrypt_articles, fetch_theblock_articles, fetch_cryptoslate_articles, fetch_beincrypto_articles, fetch_utoday_articles,  fetch_cnbc_crypto_articles
from sentiment_analyzer import load_crypto_bert, analyze_sentiment
from datetime import datetime

def main():
    print("Loading CryptoBERT model...")
    sentiment_pipeline = load_crypto_bert()

    print("Fetching latest articles from CoinDesk...")
    articles = fetch_coindesk_articles()

    print("\n=== Sentiment Analysis ===")
    for article in articles:
        sentiment, confidence = analyze_sentiment(sentiment_pipeline, article["text"])
        print(f"[{datetime.utcnow().isoformat()}Z] | {sentiment} ({confidence:.2f})")
        print(f"Title: {article['title']}")
        print(f"Link : {article['link']}")


       
       

        print("-" * 60)

if __name__ == "__main__":
    main()
