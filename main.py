import requests

api_key = "9e11f332980c4e58b21e4188e4cac500"
url = "https://newsapi.org/v2/everything?q=tesla&"\
    "from=2024-12-25&sortBy=publishedAt&apiKey="\
        "9e11f332980c4e58b21e4188e4cac500"

request = requests.get(url)

content = request.json()

for articles in content["articles"]:
    print(articles["title"])
    print(articles["description"])
