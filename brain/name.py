# import nltk

def get_name(text):
  text = text.split(' ')
  try :
  	return text[-2:]  
  except :
  	return ''

 