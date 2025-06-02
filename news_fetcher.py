
#Fetch the aritcles info from the multiple news outlet using the rss_feed
# Without TRB
import feedparser

def parse_rss_feed(url, limit=5):
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
    return articles

def fetch_coindesk_articles(limit=5):
    return parse_rss_feed("https://www.coindesk.com/arc/outboundfeeds/rss/", limit)

def fetch_cointelegraph_articles(limit=5):
    return parse_rss_feed("https://cointelegraph.com/rss", limit)

def fetch_bitcoinmagazine_articles(limit=5):############################################################
    return parse_rss_feed("https://bitcoinmagazine.com/.rss/full/", limit)


def fetch_decrypt_articles(limit=5):
    return parse_rss_feed("https://decrypt.co/feed", limit)

def fetch_theblock_articles(limit=5):##################################################################
    return parse_rss_feed("https://www.theblock.co/rss", limit)

def fetch_cryptoslate_articles(limit=5):
    return parse_rss_feed("https://cryptoslate.com/feed", limit)

def fetch_beincrypto_articles(limit=5):
    return parse_rss_feed("https://beincrypto.com/feed", limit)

def fetch_utoday_articles(limit=5):
    return parse_rss_feed("https://u.today/rss", limit)


def fetch_cnbc_crypto_articles(limit=5):
    return parse_rss_feed("https://www.cnbc.com/id/10000664/device/rss/rss.html", limit)


# main function to get the articles from multiple news outlet
news_outlets_list = [fetch_coindesk_articles,fetch_cointelegraph_articles,fetch_decrypt_articles,fetch_cryptoslate_articles,fetch_beincrypto_articles,fetch_utoday_articles,fetch_cnbc_crypto_articles]
def main():
    articles_list = []
   

    print("Fetching latest multiple articles...")
    for i in news_outlets_list:
        articles = i()

        for article in articles:
            #print('Link',article["link"])
            #print('Text',article["text"])
            #print('')
            #print('')

            articles_list.append(article['text'])

    return articles_list
        


if __name__ == "__main__":
    main()




























# main function to get the aritcles from single news outlet
'''def main():
    articles_list = []
   

    print("Fetching latest articles from CoinDesk...")
    articles = fetch_cointelegraph_articles()

    print("\n=== Sentiment Analysis ===")
    for article in articles:
        print('Link',article["link"])
        print('Text',article["text"])
        print('')
        print('')

        articles_list.append(article['text'])

    return articles_list'''
        























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






















