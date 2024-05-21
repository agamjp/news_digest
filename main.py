import requests
from datetime import date, timedelta
from send_email import send_email

today = date.today()
d = timedelta(days=7)
seven_days_ago = today - d

print(seven_days_ago)
api_key = "fcb94f8c82844455aefb8cb11f48af26"
url = "https://newsapi.org/v2/everything?q=data+engineering&from=" \
       + str(seven_days_ago) + "&sortBy=publishedAt&apiKey=" + api_key \
      + "&language=en"

request = requests.get(url)
content = request.json()

digest = [f"{a['author']}\n{a['title']}\n{a['description']}\n{a['url']}\n\n"
          for a in content["articles"]]

with open("digest.txt", "w", encoding="utf-8") as file:
    file.writelines(digest)

with open("digest.txt", "r", encoding="utf-8") as file_:
    raw_message = file_.read()

subject = "Your last week's Data Engineering digest!"

send_email(raw_message, subject)

