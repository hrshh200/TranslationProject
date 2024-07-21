

import speech_recognition
import pyttsx3
from deep_translator import GoogleTranslator

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def translate(text):
    translator = GoogleTranslator(source='auto', target='fr')
    return translator.translate(text)

def filecontentread():
    with open('Translation.txt', 'r') as file:
        file_content = file.read()
        print(file_content)
        translated_text = translate(file_content)
        print(translated_text)
        speak(translated_text)


if __name__ =='__main__':
    filecontentread()