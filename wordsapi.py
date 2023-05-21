import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WORDS_API_KEY")


def get_dictionary_result(word: str):
  url = "https://wordsapiv1.p.rapidapi.com/words/" + word

  headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers)
  result = response.json()

  return result