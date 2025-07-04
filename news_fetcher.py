#Fetch the aritcles info from the multiple news outlet using the rss_feed
# Without TRB
import feedparser
from binance_data import fetch_binance_data
import re

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def parse_rss_feed(url, limit=5):
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:limit]:
        title = entry.title
        summary = strip_html_tags(entry.get('summary', ''))
        text = f"{title}. {summary}"
        articles.append({
            "title": title,
            "summary": summary,
            "text": text,
            "link": entry.link
        })
    return articles

'''def parse_rss_feed(url, limit=5):
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
    return articles'''



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



# New functions for additional sources
def fetch_cryptopotato_articles(limit=5):
    return parse_rss_feed("https://cryptopotato.com/feed/", limit)

def fetch_bitcoinist_articles(limit=5):
    return parse_rss_feed("https://bitcoinist.com/feed/", limit)

def fetch_newsbtc_articles(limit=5):
    return parse_rss_feed("https://www.newsbtc.com/feed/", limit)

def fetch_coinjournal_articles(limit=5):
    return parse_rss_feed("https://coinjournal.net/feed/", limit)

def fetch_cryptonews_articles(limit=5):
    return parse_rss_feed("https://www.cryptonews.com/feed/", limit)

def fetch_ambcrypto_articles(limit=5):
    return parse_rss_feed("https://www.ambcrypto.com/feed/", limit)

def fetch_coingape_articles(limit=5):
    return parse_rss_feed("https://coingape.com/feed/", limit)

def fetch_cryptobriefing_articles(limit=5):
    return parse_rss_feed("https://cryptobriefing.com/feed/", limit)

def fetch_blockonomi_articles(limit=5):
    return parse_rss_feed("https://blockonomi.com/feed/", limit)

def fetch_bitcoinik_articles(limit=5):
    return parse_rss_feed("https://www.bitcoinik.com/feed/", limit)

def fetch_bitcoincom_articles(limit=5):
    return parse_rss_feed("https://news.bitcoin.com/feed/", limit)

def fetch_bitdegree_articles(limit=5):
    return parse_rss_feed("https://www.bitdegree.org/crypto/news/rss", limit)

def fetch_forbes_digital_assets_articles(limit=5):
    return parse_rss_feed("https://www.forbes.com/digital-assets/feed/", limit)




# main function to get the articles from multiple news outlet
#news_outlets_list = [fetch_coindesk_articles,fetch_cointelegraph_articles,fetch_decrypt_articles,fetch_cryptoslate_articles,fetch_beincrypto_articles,fetch_utoday_articles,fetch_cnbc_crypto_articles]
news_outlets_list = [
    #fetch_coindesk_articles,
    fetch_cointelegraph_articles, # Meta Data with content
    #fetch_bitcoinmagazine_articles,
    fetch_decrypt_articles,
    #fetch_theblock_articles,
    fetch_cryptoslate_articles, # Meta Data with content
    fetch_beincrypto_articles,  # Meta Data with content
    fetch_utoday_articles,      # Short Content
    fetch_cnbc_crypto_articles, # Short content
    #fetch_cryptopotato_articles,
    fetch_bitcoinist_articles,
    fetch_newsbtc_articles,
    fetch_coinjournal_articles, # Meta Data with Content
    fetch_cryptonews_articles, # Meta Data with Content
    fetch_ambcrypto_articles, # Meta Data with Content
    #fetch_coingape_articles,
    fetch_cryptobriefing_articles, # Meta Data with Content
    fetch_blockonomi_articles, # Meta Data with Content
    fetch_bitcoinik_articles, # Meta Data with Content
    fetch_bitcoincom_articles, # Meta Data with Content
    fetch_bitdegree_articles, # Meta Data with content
    #fetch_forbes_digital_assets_articles
]

def main():
    articles_list = []
   

    print("Fetching latest multiple articles...")
    for i in news_outlets_list:
        articles = i()

        for article in articles:
            #print('Link',article["link"])
            print('Text',article["text"])
            #print('')
            #print('')

            articles_list.append(article['text'])


    # Fetch market data from Binance
    market_data = fetch_binance_data()
    return {"articles": articles_list, "market_data": market_data}

    #return articles_list
        


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
    url = "https://cryptoslate.com/feed"
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










