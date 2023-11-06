```python
import os
from google.cloud import speech
from utils import convert_audio_to_wav

def transcribe_audio(file_path):
    client = speech.SpeechClient()

    with open(file_path, "rb") as audio_file:
        input_audio = audio_file.read()

    audio = speech.RecognitionAudio(content=input_audio)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

def main():
    audio_file_path = os.getenv('AUDIO_FILE_PATH')
    wav_file_path = convert_audio_to_wav(audio_file_path)
    transcribe_audio(wav_file_path)

if __name__ == "__main__":
    main()
```