from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
website = requests.get("https://www.merriam-webster.com/word-of-the-day")
soup = BeautifulSoup(website.content, "html.parser")
word_header = soup.find("div", class_="word-and-pronunciation")
word_of_day = word_header.find("h1")
meaning_loc = soup.find("div", "wod-definition-container")
meaning_loc = meaning_loc.find_all("p")
i = 0
meaning = ""
example = ""
for line in meaning_loc:
    if i==2:
        break
    i += 1
    if i==1:
        meaning = line.text
    else:
        example = line.text[2:]
time.sleep(300)
notification.notify(title="Word Of The Day", message=f"Word - {word_of_day.text}\nMeaning - {meaning}\nExample - {example}\nLink - {website.url}", timeout=2000)