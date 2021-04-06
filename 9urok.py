from random import choice
from pprint import pprint


def answer(q):
    if "?" in q:
        x = choice(['yes', 'no'])
        if x == 'yes':
            pprint ("YES")
        else:
            pprint("NO")
    else:
	print('Это не вопрос')


question = ''
while question != 'стоп':
	question = input("Введите свой вопрос: ")
	answer(question)
