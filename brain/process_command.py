from open_apps import open_browser

def find_any_text(ltext ,text):
	assert type(ltext) == type ([1,2])
	for lx in ltext :
		if lx in text :
			return True 
	return False


def grade_text(text) :
	pass


def parse_open(text):
	text = text.replace('open','')
	text = text.strip()
	
	if find_any_text(['chrome','browser','safari'],text) :
		return 'Speak website name:website_link'
	else :
		open_browser(text)
		return 'Done!'


def process_command(text , replycall = None):
	text = text.lower()

	if 'open' in text :
		ans = parse_open(text)
		return ans
		
	return 'Cannot Process :('