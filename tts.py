import google.cloud.texttospeech as tts
import os
import pathlib

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =str(pathlib.Path('key.json').absolute())

def text_to_wav(text: str):
    voice_name = "en-US-News-M"
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
    
    return pathlib.Path(filename).absolute()

