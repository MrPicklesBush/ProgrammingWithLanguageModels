from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    input_text = input("Enter a text string: ")
    sentiment = analyze_sentiment(input_text)
    print(f"The sentiment of the text is: {sentiment}")

if __name__ == "__main__":
    main()