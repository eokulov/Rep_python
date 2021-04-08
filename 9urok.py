from random import choice
from pprint import pprint

memory = []
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
