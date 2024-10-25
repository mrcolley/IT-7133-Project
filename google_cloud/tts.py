from google.cloud import texttospeech

from google.oauth2 import service_account
import os

def text_to_speech(text):
    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # Save the audio to file
    with open('assets/output.mp3', 'wb') as out:
        out.write(response.audio_content)

    # Play the audio file (assuming the system can play mp3 files)
    os.system("start assets/output.mp3")
