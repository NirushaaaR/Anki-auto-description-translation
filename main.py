import requests
import wordsapi
import tts
import longdudict

if __name__ == "__main__":
    anki_up = requests.get('http://localhost:8765')
    if anki_up.status_code != 200:
        print("Anki not running")
        exit()

    longdudict_url = "https://dict.longdo.com/mobile.php?search="

    deckName = "Default"
    modelName = "Vocab"
    word = input("Word: ")
    print(f"Searching for {word}")

    # get word from wordsapi
    dictionary = wordsapi.get_dictionary_result(word)

    if dictionary.get("results") is None:
        print("Word not found")
        exit()

    description = ""
    for definition in dictionary.get("results"):
        description += f"({definition['partOfSpeech']}) {definition['definition']}<br>"
        if definition.get('examples') is not None:
            for example in definition.get('examples'):
                description += f"Example: {example}<br>"
        description += "<br>"

    print('description', description.replace('<br>', '\n'))

    # meaning from longdudict
    meaning = longdudict.get_longdudict_meaning(word)
    print(meaning.replace('<br>', '\n'))

    # get speech
    speech = str(tts.text_to_wav(word))
    print(speech)


    # add note request
    result = requests.post('http://localhost:8765', json={
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deckName,
                "modelName": modelName,
                "fields": {
                    "Front": word.capitalize(),
                    "meaning": meaning,
                    "description": description,
                },
                "options": {
                    "allowDuplicate": False,
                    "duplicateScope": deckName,
                    "duplicateScopeOptions": {
                        "deckName": deckName,
                        "checkChildren": False,
                        "checkAllModels": False
                    }
                },
                "audio": [{
                "path": speech,
                "filename": word + ".wav",
                "fields": [
                    "speech"
                ]
            }],
            }
        }
    })

    print(result.status_code, result.json())