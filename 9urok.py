import numpy as np
from pprint import pprint


def answer(q):
    print(q)
    if "?" in q:
        x = np.random.randint(low=100, size = 1)
        if x > 50:
            pprint ("YES")
        else:
            pprint("NO")


question = ''
while question != 'стоп':
	question = input("Введите свой вопрос: ")
	answer(question)
