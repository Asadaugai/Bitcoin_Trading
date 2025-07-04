#Fetch the aritcles info from the single news outlet using the rss_feed
import feedparser

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

fetch_latest_coindesk_articles()