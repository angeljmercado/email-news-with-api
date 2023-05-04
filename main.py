import os
import requests
from send_email import send_email
topic = "tesla"
api_key = os.getenv("api_key1")
url = f"https://newsapi.org/v2/everything?"\
f"q={topic}&from=2023-04-04&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make the request
request = requests.get(url)

# Using json to get dictionaries with the data
content = request.json()

# Access all the tiles and description in articles, using slicing to decrease the amount of news sent to my email
body = ""
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + str(article["description"]) + "\n" + str(article["url"]) + 2*"\n"

# Send the news tiles and description to the email 
body = body.encode("utf-8")
send_email(body)
