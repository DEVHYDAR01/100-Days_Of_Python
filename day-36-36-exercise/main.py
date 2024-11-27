import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_prams = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_prams)
stock_response.raise_for_status()
data = stock_response.json()
previous_day_closing_price = float(data["Time Series (Daily)"]["2024-11-26"]["4. close"])
day_before_closing_price = float(data["Time Series (Daily)"]["2024-11-25"]["4. close"])
# previous_day_closing_price = 378.59
positive_difference = round(abs(previous_day_closing_price - day_before_closing_price))
up_down = None
if positive_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
previous_day_5percent_value = round((positive_difference / previous_day_closing_price) * 100)
if previous_day_5percent_value > 1:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": API_KEY_NEWS
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]

    send_msg = [
        Client(ACCOUNT_SID, AUTH_TOKEN).messages.create(
            body=f"{STOCK} {up_down}5%\nHeadlines: {article["title"]}\nBrief: {article["description"]}",
            from_='+12242231211',
            to='+2349016092616'
        )
        for article in articles
    ]
    # for message_sid in send_msg:
    #     print(message_sid)






## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""