# Extracting the tweets of multiple persons and perform analysis
from selenium import webdriver
from transformers import TextClassificationPipeline, AutoModelForSequenceClassification, AutoTokenizer
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



def analyze_sentiment(tweets):
    model_name = "ElKulako/cryptobert"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, max_length=64, truncation=True, padding='max_length')

    sentiments = pipe(tweets)
    return sentiments




def main():
    driver = init_driver()
    users =['realDonaldTrump','jpmorgan','__SayI0r','nayibbukele','CathieDWood']
    username = 'realDonaldTrump'
    tweet_dic = {}
    try:
        for i in users:
            tweets = get_elon_musk_tweets(i, driver, count=5)
            tweet_dic[i] = tweets
       
            sentiments = analyze_sentiment(tweets)

            
        
           
            
            for i, (tweet, sentiment) in enumerate(zip(tweets, sentiments), 1):
                print(f"{i}. {tweet}\nSentiment: {sentiment['label']} (score: {sentiment['score']:.2f})\n")
        #print(tweet_dic)
    finally:
        driver.quit()



if __name__ == "__main__":
    main()








