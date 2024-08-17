import speech_recognition as sr
import time
from pathlib import Path
import openai
import pyaudio

client = openai.OpenAI(api_key='your api key')      # https://platform.openai.com/api-keys

def record_audio() -> str:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Say something...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    print("Audio recorded, processing...")

    WAVE_OUTPUT_FILENAME = Path(__file__).parent / "mic_input.wav"
    with open(WAVE_OUTPUT_FILENAME, "wb") as f:
        f.write(audio.get_wav_data())
    
    return WAVE_OUTPUT_FILENAME

def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text",
            language="en"
        )
    return transcription

def get_gpt4_response(transcription: str) -> str:

    user_message = transcription + " Please respond concisely, as if talking in a real conversation."
    
    response = client.chat.completions.create(
        model="choice api models",                  # https://platform.openai.com/docs/models/models-overview
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

def stream_to_speakers(text: str) -> None:
    global start_time
    player_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
    start_time = time.time()

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="choice voice options",               # https://platform.openai.com/docs/guides/text-to-speech/voice-options
        response_format="pcm",
        input=text,
    ) as response:
        for chunk in response.iter_bytes(chunk_size=1024):
            player_stream.write(chunk)

def main():
    while True:
        try:
            audio_file_path = record_audio()
            transcription = transcribe_audio(audio_file_path)
            print("Transcription: ", transcription, end='')
            
            gpt4_response = get_gpt4_response(transcription)
            print("GPT Response: ", gpt4_response)
            print()
            
            stream_to_speakers(gpt4_response)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
