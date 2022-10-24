#try to tranlate
#by: M1rrox


import random
import googletrans
from googletrans import Translator

#################################

last_int = 0
translator = Translator()
answ = ""

#################################

def read_file(name):
	with open(name, encoding = 'utf-8') as f:
		return f.read().split("\n")

def get_random_int(n1, n2):
	num = random.randint(n1, n2)
	while num == last_int:
		num = random.randint(n1, n2)
	return num

#################################

text_en = read_file("w.txt")

while answ != "$exit":
	n = get_random_int(0, len(text_en))
	en = text_en[n]
	ru = translator.translate(en, src = 'en', dest = 'ru').text
	print("\n+" + (len(en) * "-") + "+")
	print(en)
	answ = input(": ")
	if answ[0] == "$":
		if answ == "$tr":
			print("- " + ru)
	else:
		if answ == ru:
			print("- CORRECT")
		else:
			print("- ERR")
			print("- " + ru)
