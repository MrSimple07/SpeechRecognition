import speech_recognition as sr
from gtts import gTTS
import os
import pyaudio
import wave

# Функция для записи аудио
def record_audio(filename, duration=5, rate=16000, channels=1):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, frames_per_buffer=1024)
    frames = []

    print("Recording...")
    for _ in range(0, int(rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Функция для распознавания речи с помощью CMU Sphinx
def transcribe_sphinx(audio_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)
    with audio_file as source:
        audio = recognizer.record(source)
    return recognizer.recognize_sphinx(audio)

# Функция для генерации ответа
def generate_response(text):
    if "привет я разработчик" in text.lower():
        response_text = "сегодня выходной"
    elif "я сегодня не приду домой" in text.lower():
        response_text = "Ну и катись отсюда"
    else:
        response_text = "Команда не распознана"
    
    tts = gTTS(response_text, lang='ru')
    tts.save("response.mp3")
    # os.system("mpg321 response.mp3")

def main():
    audio_path = 'input.wav'
    record_audio(audio_path)
    transcribed_text = transcribe_sphinx(audio_path)
    print(f"Распознанный текст: {transcribed_text}")
    generate_response(transcribed_text)

if __name__ == "__main__":
    main()
