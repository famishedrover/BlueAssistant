from open_apps import open_browser
import webbrowser
import time
from automation.fblogin import fblogin

def find_any_text(ltext ,text):
	assert type(ltext) == type ([1,2])
	for lx in ltext :
		if lx.lower() in text.lower() :
			return True 
	return False


def grade_text(text) :
	pass

def text_process(keyword , text) :
	keywordupper = keyword[0].upper() + keyword[1:]
	text = text.replace(keyword,'')
	text = text.replace(keywordupper,'')
	text = text.replace(keyword.lower(),'')
	text = text.strip()
	return text 

def parse_open(text):
	text = text_process('open',text)
	if find_any_text(['chrome','browser','safari'],text) :
		return 'Speak website name:website_link'
	else :
		open_browser(text)
		return 'Done!'


def parse_google(text) :
	text = text_process('google',text)
	link = 'https://www.google.co.in/search?q='
	text = '+'.join(text.split(' '))
	webbrowser.open(link+text)
	return 'Done!'

def parse_login(text) :
	text = text_process('login',text)

	if find_any_text(['facebook','fb'],text) :
		fblogin()

	return 'Done'


def process_command(text , replycall = None):
	textlower = text.lower()

	if 'open' in textlower :
		ans = parse_open(textlower)
		return ans
	if 'google' in textlower :
		ans = parse_google(text) 
		return ans
	if 'login' in textlower :
		ans = parse_login(text)
		if ans is not None :
			return ans
		else :
			return ''

	if 'wait for' in text :
		pass

	return 'Cannot Process :('









