# Anki auto word description and TH translation
use to practice english vocab and translate to TH lang.
Using Anki flashcards

## structure
- using words api to get word descriptions and example
- using longdu dict to translate the word into TH
- using google text to speech api to get word pronunciation
- using anki-connect module to automatically add flashcard

## setup
- pip install -r requirements.txt
- create .env with the WORDS_API_KEY from [wordsapi](https://www.wordsapi.com/)
- get google cloud api key, place inside the same folder (name it key.json) 
  - follow https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#0 to generate the api-key
- install [anki-connect](https://ankiweb.net/shared/info/2055492159) module in anki
  - anki need to open in the background in order for anki-connect to work.

