import os
import requests
from datetime import date, timedelta
from send_email import send_email
from dotenv import load_dotenv

load_dotenv()
today = date.today()
d = timedelta(days=7)
seven_days_ago = today - d

topic = input("Enter the topic that interests you:")

print(seven_days_ago)
api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}" \
      f"&from={seven_days_ago}&sortBy=publishedAt&apiKey={api_key}&language=en"

request = requests.get(url)
content = request.json()

digest = [f"{a['author']}\n{a['title']}\n{a['description']}\n{a['url']}\n\n"
          for a in content["articles"]]

with open("digest.txt", "w", encoding="utf-8") as file:
    file.writelines(digest)

with open("digest.txt", "r", encoding="utf-8") as file_:
    raw_message = file_.read()

subject = f"Your last week's {topic.title()} digest!"

send_email(raw_message, subject)

