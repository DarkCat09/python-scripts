import speech_recognition as sr
recog = sr.Recognizer()
with sr.Microphone() as source:
    print("Говорите...")
    audio = recog.listen(source)
    print("Распознавание...")
    try:
        print("Вы сказали:", recog.recognize_google(audio, language='ru-RU'))
    except Exception as ex:
        print("Произошла ошибка:", str(ex))
