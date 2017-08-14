import speech_recognition as sr
from speech2text import say

r = sr.Recognizer()
sample_rate = 48000
chunk_size = 2048

def listen_blue(talk=False) :
	r = sr.Recognizer()
	# mic_list = sr.Microphone.list_microphone_names()
	with sr.Microphone( device_index = 0 ,sample_rate = sample_rate ,chunk_size = chunk_size)  as source :
		r.adjust_for_ambient_noise(source)
		print 'Speak Now !...'
		if talk is True :
			say('Speak Now')

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