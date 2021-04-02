## Imports
import sys
import time
import random
import vlc
import speech_recognition as sr

## Options
resume_type = 0				# 0=keyboard, 1=voice
my_lang = 'ru-RU'			# recognizer language
word_for_resume = 'старт'	# word for recognizer to resume music

## Functions
def wait_for_word(word):
	phrase = ''
	recog = sr.Recognizer()
	mic = sr.Microphone()
	while True:
		with mic as audio_file:
			recog.adjust_for_ambient_noise(audio_file)
			audio = recog.listen(audio_file)
			try:
				phrase = recog.recognize_google(audio, language=my_lang)
				print("Recognizer:", phrase)
				if (phrase.lower().find(word.lower()) > -1):
					break
			except Exception:
				print("Error")

## Main code
try:
	print()
	player = vlc.MediaPlayer(sys.argv[1])
	while True:
		player.play()
		time.sleep(random.randint(3, 8)+2)
		player.pause()
		if resume_type == 1:
			wait_for_word(word_for_resume)
		else:
			input("Press ENTER to resume... ")
		print("OK")

except KeyboardInterrupt:
	player.stop()
	print("\n")
	print("Stopped by keyboard.")
	print("")
	quit()
