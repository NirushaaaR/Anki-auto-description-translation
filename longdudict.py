import requests
from bs4 import BeautifulSoup

longdudict_url = "https://dict.longdo.com/mobile.php?search="

def get_longdudict_meaning(word: str):
    result = requests.get(longdudict_url + word)
    result.encoding = result.apparent_encoding
    soup = BeautifulSoup(result.text, 'html.parser')
    tables = soup.find_all('table')[:3]
    meaning = ""
    for table in tables:
        for tr in table.find_all('tr'):
          td = tr.find_all('td')
          if td[0].text.lower() == word.lower():
            for td in td[1:]:
                meaning += td.text
                if "See also:" in meaning:
                    meaning = meaning.split("See also:")[0]
                meaning += "<br>"
    return meaning