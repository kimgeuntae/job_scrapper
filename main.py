import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

print(indeed_soup)


