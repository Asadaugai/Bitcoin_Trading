
# Extracting the tweets of multiple persons using Webscraping
# Without TRB
from selenium import webdriver
from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from binance_data import fetch_binance_data
import time

def init_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    return driver

def get_elon_musk_tweets(username, driver, count=5):
    url = f"https://x.com/{username}"
    #url = "https://x.com/realDonaldTrump"
    #url = "https://x.com/jpmorgan"
    driver.get(url)
    time.sleep(5)  # Wait for tweets to load

    tweet_xpath = '//article[@role="article"]//div[@data-testid="tweetText"]'
    tweet_elements = driver.find_elements(By.XPATH, tweet_xpath)

    tweets = [tweet.text for tweet in tweet_elements[:count]]
    return tweets



def main():
    driver = init_driver()
    users =['realDonaldTrump','saylor','jack','cz_binance','VitalikButerin','aantonop','jpmorgan','nayibbukele','CathieDWood']

    tweet_dic = {}
    try:
        for i in users:
            tweets = get_elon_musk_tweets(i, driver, count=5)
            tweet_dic[i] = tweets


        
        # Fetch market data
        market_data = fetch_binance_data()
        return {"tweets": tweet_dic, "market_data": market_data}
        
           
        #print(tweet_dic)
        #print(type(tweet_dic))

        #return tweet_dic
        
    finally:
        driver.quit()



if __name__ == "__main__":
    main()
    













#Fetch the tweets of single person using webscraping
'''from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def init_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    return driver

def get_elon_musk_tweets(driver, count=5):
    #url = "https://x.com/elonmusk"
    #url = "https://x.com/realDonaldTrump"
    url = "https://x.com/jpmorgan"
    driver.get(url)
    time.sleep(5)  # Wait for tweets to load

    tweet_xpath = '//article[@role="article"]//div[@data-testid="tweetText"]'
    tweet_elements = driver.find_elements(By.XPATH, tweet_xpath)

    tweets = [tweet.text for tweet in tweet_elements[:count]]
    return tweets

def main():
    driver = init_driver()
    try:
        tweets = get_elon_musk_tweets(driver, count=5)
        print("\nLatest Tweets by Elon Musk:")
        for i, tweet in enumerate(tweets, 1):
            print(f"{i}. {tweet}\n")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()'''





#Fetching data of tweets using API key
#BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALRN1AEAAAAA8v97mac%2FO3anaQ%2FuzzmWCCXUUf8%3DukMJO681p60PtiE6j358HETIM4kKegbjZvFK9H16EI7aObdyCX"
'''import requests

# Your Bearer Token here
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALRN1AEAAAAA8v97mac%2FO3anaQ%2FuzzmWCCXUUf8%3DukMJO681p60PtiE6j358HETIM4kKegbjZvFK9H16EI7aObdyCX"  # Replace with your actual bearer token

# Headers for auth
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# Get user ID from username
def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["id"]
    else:
        print(f"Failed to fetch user ID for {username}: {response.text}")
        return None

# Get tweets by user ID
def get_user_tweets(user_id, limit=5):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results={limit}&tweet.fields=created_at,text"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Failed to fetch tweets for user ID {user_id}: {response.text}")
        return []

# Fetch Elon Musk's tweets
def get_elon_tweets(limit=5):
    #username = "realDonaldTrump"
    username = "xai"
    print(f"\n🔍 Tweets by @{username}:")
    user_id = get_user_id(username)
    all_tweets = []
    if user_id:
        tweets = get_user_tweets(user_id, limit)
        for tweet in tweets:
            print(f"{tweet['created_at']}: {tweet['text']}\n")
            all_tweets.append(tweet['text'])
    print(all_tweets)
    return all_tweets


def main():
    elon_tweets = get_elon_tweets()
    return elon_tweets


# Run
if __name__ == "__main__":
    main()'''






