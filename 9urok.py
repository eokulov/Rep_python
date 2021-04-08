from random import choice
from pprint import pprint

<<<<<<< HEAD
memory = []
=======

def answer(q):
    if "?" in q:
        x = choice(['yes', 'no'])
        if x == 'yes':
            pprint ("YES")
        else:
            pprint("NO")
    else:
	print('Это не вопрос')


>>>>>>> bfb1ff84161a2a92b2a8a94f14b16b31e174065c
question = ''
while question != 'стоп':
    question = input("Введите свой вопрос: ")
    if '?' in question:
        if question in memory:
            print('Вопрос уже был')
        else:
            x = choice(['YES', 'NO'])
            memory += [question]
            print(memory)
            if x == 'YES':
                pprint("YES")
            else:
                pprint("NO")
    else:
            print('Это не вопрос')
