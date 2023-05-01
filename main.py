import requests

api_key = "9e90d18b98f84d31be7132886d45c4a4"
url = "https://newsapi.org/v2/everything?domains"\
"=wsj.com&apiKey=9e90d18b98f84d31be7132886d45c4a4"

request = requests.get(url)
content = request.json()
print(content["title"])
print(content["description"])





