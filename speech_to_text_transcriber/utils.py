```python
import os
import subprocess
from google.cloud import speech

def convert_audio_to_wav(file_path):
    output_path = os.path.splitext(file_path)[0] + ".wav"
    command = f"ffmpeg -i {file_path} -vn -acodec pcm_s16le -ac 1 -ar 16000 -f wav {output_path}"
    subprocess.call(command, shell=True)
    return output_path

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

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript
```