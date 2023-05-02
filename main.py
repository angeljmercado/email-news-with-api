import os
import requests
from send_email import send_email

api_key = os.getenv("api_key1")
url = f"https://newsapi.org/v2/everything?domains"\
f"=wsj.com&apiKey={api_key}"

# Make the request
request = requests.get(url)

# Using json to get dictionaries with the data
content = request.json()

# Access all the tiles and description in articles
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

# Send the news tiles and description to the email
body = body.encode("utf-8")
send_email(body)
