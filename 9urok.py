import numpy as np
from pprint import pprint

def answer(quest):
    q = set(quest.split())
    print(q)
    if "?" in q:
        x = np.random.randint(low=100, size = 1)
        if x > 75:
            pprint ("YES")
        else:
            pprint("NO")
    return print(x)

question = input("Введите свой вопрос: ") + " ?"
answer(question)
