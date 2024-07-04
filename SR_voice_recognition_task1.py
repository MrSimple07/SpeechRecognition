import speech_recognition as sr

# Инициализация распознавателя речи
r = sr.Recognizer()

# Функция распознавания речи
def recognize_speech():
    with sr.Microphone() as source:
        print("Говорите...")
        audio = r.record(source, duration=10)

    try:
        # Распознавание текста из аудио
        text = r.recognize_google(audio, language="ru-RU")
        print("Распознано: " + text)

        # Обработка распознанной фразы
        if text.lower() == "привет я разработчик":
            response = "Сегодня выходной"
        elif text.lower() == "я сегодня не приду домой":
            response = "Ну и катись отсюда"
        elif text.lower() == "stop" or "стоп":
            response = "Stopping..."
            return None 
        else:
            response = "Не понимаю ваш речь"

        # Ответ
        print("Ответ:", response)
        return response
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

while True:
    response = recognize_speech()
    if response is None:
        break 

print("Program stopped!")

