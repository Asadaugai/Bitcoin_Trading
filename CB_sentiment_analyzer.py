'''from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

label_map = {"LABEL_0": "Bearish", "LABEL_1": "Neutral", "LABEL_2": "Bullish"}

def load_crypto_bert():
    model_name = "ElKulako/cryptobert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer, truncation=True, max_length=128, padding=True)

def analyze_sentiment(pipeline, text):
    result = pipeline(text)[0]
    sentiment = label_map[result['label']]
    confidence = result['score']
    return sentiment, confidence'''

#Simple Cryptobert model for market analysis
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

def load_crypto_bert():
    model_name = "ElKulako/cryptobert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer, truncation=True, max_length=128, padding=True)

def analyze_sentiment(pipeline, text):
    result = pipeline(text)[0]
    sentiment = result['label']          # Already gives 'Bullish', 'Neutral', or 'Bearish'
    confidence = result['score']
    return sentiment, confidence


