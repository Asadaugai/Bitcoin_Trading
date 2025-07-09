#Fetch the aritcles info from the multiple news outlet using the rss_feed
# Without TRB
import feedparser
from binance_data import fetch_binance_4h_metrics
from datetime import datetime, timedelta
import re
import logging

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)



def parse_rss_feed(url, time_window_hours=1):
    try:
        feed = feedparser.parse(url)
        if feed.bozo:
            logging.error(f"Error parsing RSS feed {url}: {feed.bozo_exception}")
            return []
        articles = []
        current_time = datetime.utcnow()
        time_threshold = current_time - timedelta(hours=time_window_hours)
        for entry in feed.entries:
            pub_date = entry.get('published_parsed', None)
            if pub_date:
                pub_datetime = datetime(*pub_date[:6])
                if pub_datetime >= time_threshold:
                    title = entry.get('title', 'No Title')
                    summary = strip_html_tags(entry.get('summary', 'No Summary'))
                    link = entry.get('link', 'No Link')
                    text = f"{title}. {summary}"
                    articles.append({
                        "title": title,
                        "summary": summary,
                        "text": text,
                        "link": link
                    })
        return articles
    except Exception as e:
        logging.error(f"Failed to fetch RSS feed {url}: {str(e)}")
        return []



def fetch_coindesk_articles(time_window_hours=1):
    return parse_rss_feed("https://www.coindesk.com/arc/outboundfeeds/rss/", time_window_hours)

def fetch_cointelegraph_articles(time_window_hours=1):
    return parse_rss_feed("https://cointelegraph.com/rss", time_window_hours)

def fetch_bitcoinmagazine_articles(time_window_hours=1):############################################################
    return parse_rss_feed("https://bitcoinmagazine.com/.rss/full/", time_window_hours)


def fetch_decrypt_articles(time_window_hours=1):
    return parse_rss_feed("https://decrypt.co/feed", time_window_hours)

def fetch_theblock_articles(time_window_hours=1):##################################################################
    return parse_rss_feed("https://www.theblock.co/rss", time_window_hours)

def fetch_cryptoslate_articles(time_window_hours=1):
    return parse_rss_feed("https://cryptoslate.com/feed", time_window_hours)

def fetch_beincrypto_articles(time_window_hours=1):
    return parse_rss_feed("https://beincrypto.com/feed", time_window_hours)

def fetch_utoday_articles(time_window_hours=1):
    return parse_rss_feed("https://u.today/rss", time_window_hours)

def fetch_cnbc_crypto_articles(time_window_hours=1):
    return parse_rss_feed("https://www.cnbc.com/id/10000664/device/rss/rss.html", time_window_hours)



# New functions for additional sources
def fetch_cryptopotato_articles(time_window_hours=1):
    return parse_rss_feed("https://cryptopotato.com/feed/", time_window_hours)

def fetch_bitcoinist_articles(time_window_hours=1):
    return parse_rss_feed("https://bitcoinist.com/feed/", time_window_hours)

def fetch_newsbtc_articles(time_window_hours=1):
    return parse_rss_feed("https://www.newsbtc.com/feed/", time_window_hours)

def fetch_coinjournal_articles(time_window_hours=1):
    return parse_rss_feed("https://coinjournal.net/feed/", time_window_hours)

def fetch_cryptonews_articles(time_window_hours=1):
    return parse_rss_feed("https://www.cryptonews.com/feed/", time_window_hours)

def fetch_ambcrypto_articles(time_window_hours=1):
    return parse_rss_feed("https://www.ambcrypto.com/feed/", time_window_hours)

def fetch_coingape_articles(time_window_hours=1):
    return parse_rss_feed("https://coingape.com/feed/", time_window_hours)

def fetch_cryptobriefing_articles(time_window_hours=1):
    return parse_rss_feed("https://cryptobriefing.com/feed/", time_window_hours)

def fetch_blockonomi_articles(time_window_hours=1):
    return parse_rss_feed("https://blockonomi.com/feed/", time_window_hours)

def fetch_bitcoinik_articles(time_window_hours=1):
    return parse_rss_feed("https://www.bitcoinik.com/feed/", time_window_hours)

def fetch_bitcoincom_articles(time_window_hours=1):
    return parse_rss_feed("https://news.bitcoin.com/feed/", time_window_hours)

def fetch_bitdegree_articles(time_window_hours=1):
    return parse_rss_feed("https://www.bitdegree.org/crypto/news/rss", time_window_hours)

def fetch_forbes_digital_assets_articles(time_window_hours=1):
    return parse_rss_feed("https://www.forbes.com/digital-assets/feed/", time_window_hours)




# main function to get the articles from multiple news outlet
#news_outlets_list = [fetch_coindesk_articles,fetch_cointelegraph_articles,fetch_decrypt_articles,fetch_cryptoslate_articles,fetch_beincrypto_articles,fetch_utoday_articles,fetch_cnbc_crypto_articles]
news_outlets_list = [
    

    fetch_cointelegraph_articles, # Meta Data with content
    fetch_decrypt_articles,
    fetch_cryptoslate_articles, # Meta Data with content
    fetch_beincrypto_articles,  # Meta Data with content
    fetch_utoday_articles,      # Short Content
    fetch_cnbc_crypto_articles, # Short content

    fetch_bitcoinist_articles,
    fetch_newsbtc_articles,
    fetch_coinjournal_articles, # Meta Data with Content
    fetch_cryptonews_articles, # Meta Data with Content
    fetch_ambcrypto_articles, # Meta Data with Content

    fetch_cryptobriefing_articles, # Meta Data with Content
    fetch_blockonomi_articles, # Meta Data with Content
    fetch_bitcoinik_articles, # Meta Data with Content
    fetch_bitcoincom_articles, # Meta Data with Content
    fetch_bitdegree_articles, # Meta Data with content

    #fetch_forbes_digital_assets_articles # Not Working
    #fetch_coingape_articles, # Not Working
    #fetch_cryptopotato_articles, # Not Working
    #fetch_theblock_articles, # Not Working
    #fetch_bitcoinmagazine_articles, # Not Working
    #fetch_coindesk_articles, # Not Working
]

def main():
    articles_list = []
   

    print("Fetching latest multiple articles...")
    for i in news_outlets_list:
        articles = i()

        for article in articles:
            print('Link',article["link"])
            print('Text',article["text"])
            print('')
            print('')

            articles_list.append(article['text'])


    # Fetch market data from Binance
    market_data = fetch_binance_4h_metrics()
    return {"articles": articles_list, "market_data": market_data}

    #return articles_list
        


if __name__ == "__main__":
    main()