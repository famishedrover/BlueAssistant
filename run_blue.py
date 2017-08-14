from sense.speech2text import say
from sense.speechrecog import listen_blue

from brain.name import get_name
from brain.process_command import process_command

# say("Hello! What's your name?")
# name = listen_blue()
# print name
# name = get_name(name)
# say('Hi '+name)
max_iter = 20
cont = True
say("Let's Begin!")
while(cont is True or max_iter > 0) :
	say('Say Something...')
	max_iter -=1 
	command = listen_blue()
	print 'command:\t',command
	
	if 'exit' in command.lower() or 'stop listening' in command.lower():
		cont = False 
		break

	answer = process_command(command)
	print 'answer:\t',answer
	say(answer)