import webbrowser

def find_any_text(ltext ,text):
	assert type(ltext) == type ([1,2])
	for lx in ltext :
		if lx in text :
			return True 
	return False


def open_browser(link):
	link = link.strip()
	if 'http://' not in link or 'https://' :
		link = 'http://' + link
	if '.com' not in link  or '.co.in' not in link:
		link = link + '.com'

	print webbrowser.open(link)




if __name__ == '__main__' :
	open_browser('http://google.com')