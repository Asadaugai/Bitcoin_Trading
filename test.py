#Fetch the aritcles info from the single news outlet using the rss_feed
'''import feedparser

def fetch_latest_coindesk_articles(limit=5):
    url = "https://cointelegraph.com/rss"
    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:limit]:
        title = entry.title
        summary = entry.get('summary', '')
        text = f"{title}. {summary}"
        articles.append({
            "title": title,
            "summary": summary,
            "text": text,
            "link": entry.link
        })
    for article in articles:
        print(article['text'], end="\n\n")

    return articles

fetch_latest_coindesk_articles()'''



import snscrape.modules.twitter as sntwitter

def fetch_latest_tweets(username, count=5):
    tweets = []
    query = f"from:{username}"
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= count:
            break
        tweets.append(tweet.content)
    
    print(f"\nLatest tweets by @{username}:\n")
    for i, tweet in enumerate(tweets, 1):
        print(f"{i}. {tweet}\n")

# Example usage
if __name__ == '__main__':
    user = input("Enter Twitter username (without @): ").strip()
    fetch_latest_tweets(user)
