import webbrowser

def open_browser(link):
	link = link.strip()
	if 'http://' not in link :
		link = 'http://' + link
	if '.com' not in link :
		link = link + '.com'
	print webbrowser.open(link)




if __name__ == '__main__' :
	open_browser('http://google.com')