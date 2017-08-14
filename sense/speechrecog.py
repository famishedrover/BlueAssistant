import speech_recognition as sr
from speech2text import say
import pygame 



pygame.init()
pygame.mixer.music.load("./sounds/beep.mp3")

r = sr.Recognizer()
sample_rate = 48000
chunk_size = 2048

def listen_blue(talk=False,beep=True) :
	r = sr.Recognizer()
	# mic_list = sr.Microphone.list_microphone_names()
	with sr.Microphone( device_index = 0 ,sample_rate = sample_rate ,chunk_size = chunk_size)  as source :
		r.adjust_for_ambient_noise(source)
		print 'Speak Now !...'
		if talk is True :
			say('Speak Now')
		if beep is True :
			pygame.mixer.music.play()
		audio = r.listen(source)
		try :
			text = r.recognize_google(audio)
			return text 
		except sr.UnknownValueError :
			print ('Sorry , Couldnt understand')
			return ''
		except sr.RequestError as e :
			print 'Could not request results from Google Speech Recog Device {0}'.format(e)
			return ''


if __name__ == '__main__' :
	w = listen_blue()
	print w	
	say('You said '+w)