from news_fetcher import main as news_fetch
from twitter_fetecher import main as tweet_fetch
from llm_news_Fetecher import analyze_bitcoin_metrics as analyze_news
from llm_tweets import analyze_bitcoin_metrics as analyze_tweets

def parse_metrics(output):
    """Parse LLM output into a dictionary"""
    metrics = {}
    print("Raw LLM Output:\n", output)  # Debug
    for line in output.split('\n'):
        if ': ' not in line:
            print(f"Skipping malformed line: {line}")
            continue
        try:
            key, value = line.split(': ')
            if '%' in value:
                metrics[key] = float(value.replace('%', ''))
            else:
                metrics[key] = float(value.replace('$', ''))
        except ValueError as e:
            print(f"Error parsing line '{line}': {e}")
    return metrics

def main():
    # Fetch news and market data
    news_data = news_fetch()
    
    # Fetch tweets
    tweets_data = tweet_fetch()
    
    # Analyze metrics
    news_metrics = parse_metrics(analyze_news(news_data))
    tweet_metrics = parse_metrics(analyze_tweets(tweets_data))
    
    # Combine metrics (average)
    combined_metrics = {
        "Buy Price": (news_metrics.get("Buy Price", 0) + tweet_metrics.get("Buy Price", 0)) / 2,
        "Stop-Loss Price": (news_metrics.get("Stop-Loss Price", 0) + tweet_metrics.get("Stop-Loss Price", 0)) / 2,
        "Take-Profit Price": (news_metrics.get("Take-Profit Price", 0) + tweet_metrics.get("Take-Profit Price", 0)) / 2,
        "Stop-Loss Zone %": (news_metrics.get("Stop-Loss Zone %", 0) + tweet_metrics.get("Stop-Loss Zone %", 0)) / 2,
        "Profit Zone %": (news_metrics.get("Profit Zone %", 0) + tweet_metrics.get("Profit Zone %", 0)) / 2
    }
    
    print("\n===== FINAL BITCOIN TRADING METRICS =====")
    for key, value in combined_metrics.items():
        print(f"{key}: {value:.2f}{'%' if 'Zone' in key else ''}")

if __name__ == "__main__":
    main()




# main.py
'''from news_fetcher import main as news_fetch
from twitter_fetecher import main as tweet_fetch
from llm_news_Fetecher import analyze_bitcoin_sentiment as analyze_news
from llm_tweets import analyze_bitcoin_sentiment as analyze_tweets
from validate_metrics import validate_metrics

def parse_metrics(output):
    """Parse LLM output into a dictionary"""
    metrics = {}
    for line in output.split('\n'):
        key, value = line.split(': ')
        if '%' in value:
            metrics[key] = float(value.replace('%', ''))
        else:
            metrics[key] = float(value.replace('$', ''))
    return metrics

def main():
    # Fetch news and market data
    news_data = news_fetch()
    
    # Fetch tweets
    tweets_dict = tweet_fetch()
    
    # Analyze sentiment and metrics
    news_metrics = parse_metrics(analyze_news(news_data))
    tweet_metrics = parse_metrics(analyze_tweets(tweets_dict))
    
    # Combine metrics (e.g., average or weighted based on reliability)
    combined_metrics = {
        "Buy Price": (news_metrics["Buy Price"] + tweet_metrics["Buy Price"]) / 2,
        "Stop-Loss Price": (news_metrics["Stop-Loss Price"] + tweet_metrics["Stop-Loss Price"]) / 2,
        "Take-Profit Price": (news_metrics["Take-Profit Price"] + tweet_metrics["Take-Profit Price"]) / 2,
        "Stop-Loss Zone %": (news_metrics["Stop-Loss Zone %"] + tweet_metrics["Stop-Loss Zone %"]) / 2,
        "Profit Zone %": (news_metrics["Profit Zone %"] + tweet_metrics["Profit Zone %"]) / 2
    }
    
    # Validate metrics
    validation_result = validate_metrics(combined_metrics)
    
    print("\n===== FINAL BITCOIN TRADING METRICS =====")
    for key, value in combined_metrics.items():
        print(f"{key}: {value:.2f}{'%' if 'Zone' in key else ''}")
    print("\n===== VALIDATION RESULTS =====")
    for key, value in validation_result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()'''