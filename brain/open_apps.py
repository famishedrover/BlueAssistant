import webbrowser
import os 


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

def open_application(text):
	h = '/Applications/'

	code = os.system("open %s%s"%(h,text))
	if code !=0 :
		code = os.system("open %s%s"%(h,text+'.app'))

	if code!=0 :
		return 'Not Found.'
	if code == 0:
		return 'Done!'


def open_folder(text,home=None) :
	if home is None :
		home = os.getenv("HOME")
		home += '/'
	flag = False 
	path = '.'

	# dirlists = ['Desktop','Documents','Downloads']
	dirlists = ['']
	for hh in dirlists :
		for dirname , dirnames , filename in os.walk(home+hh) :
			for subd in dirnames :
				if text.lower() in subd.lower() :
					path = os.path.join(dirname,subd)
					flag = True
					break
			if flag is True :
				break
		if flag is True :
			break


	if flag is False :
		return 'Not Found.'
	else :
		os.system('open %s'%path)
		return 'Done!'



if __name__ == '__main__' :
	open_browser('http://google.com')