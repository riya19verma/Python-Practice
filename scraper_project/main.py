import requests
from bs4 import BeautifulSoup

url = "https://apps.apple.com/us/app/duckduckgo-browser-search-ai/id663592361"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')  # or 'html.parser'

print("TEXT : \n")
for p in soup.find_all('p'):
    print(p.get_text())

for h in soup.find_all(['h1', 'h2', 'h3']):
    print(h.get_text())

print("LINKS : \n")
for a in soup.find_all('a', href=True):
    print(a['href'])  # Relative or absolute URL

print("IMAGES : \n")
for img in soup.find_all('img', src=True):
    print(img['src'])  # Can download with requests

print("HTML META TAGS : \n")
# Common HTML meta tags
for meta in soup.find_all('meta'):
    if meta.get('name') == 'author':
        print("Author:", meta.get('content'))
    if meta.get('property') == 'article:published_time':
        print("Published:", meta.get('content'))

print("RATINGS : \n")
ratings = soup.find_all(class_="rating")
for r in ratings:
    print(r.get_text())

print("FORMS : \n")
for form in soup.find_all('form'):
    for input_tag in form.find_all('input'):
        print(input_tag.get('name'), "=", input_tag.get('value'))
