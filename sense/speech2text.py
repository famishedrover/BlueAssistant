import subprocess
def say(text) :
	subprocess.call(['say',text])

if __name__ == '__main__' :
	say('I am angryziber!')