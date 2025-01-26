import requests
from send_email import send_email

topic = "tesla"
api_key = "9e11f332980c4e58b21e4188e4cac500"
url = f"https://newsapi.org/v2/everything?q={topic}&"\
    "from=2024-12-25&sortBy=publishedAt&apiKey="\
        "9e11f332980c4e58b21e4188e4cac500&language=en"

request = requests.get(url)

content = request.json()

body = "Subject: Today's News\n\n" 
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = body + article["title"]+"\n"+article["description"]+"\n"+article["url"]+ 2*"\n"

body = body.encode("utf-8")
send_email(body)

   
