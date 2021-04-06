from pprint import pprint
from itertools import product


class Person:
    def __init__(self, name, rost, ves, mesto_uch):
        self.name, self.rost, self.ves, self.mesto_uch = name, rost, ves, mesto_uch
        self.key = (name, mesto_uch)

    def __repr__(self):
        return "Person('%s',%s,%s,'%s')" % (self.name, self.rost, self.ves, self.mesto_uch)

    def __eq__(self, obj):
        if type(obj) == str:
            return self.fuzzy_compare(obj)
        else:
            return 0

    def get_name(self):
        return self.name

    def by_name(self, Q):
        Q = Q - NAME_WORDS
        W = set(self.name.split())
        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def by_rost(self, Q):
        q_rost = max([int_val(q) for q in Q])
        if 'выше' in Q:
            return q_rost < self.rost
        if 'ниже' in Q:
            return q_rost > self.rost
        return q_rost + 5 >= self.rost >= q_rost - 5

    def by_ves(self, Q):
        q_ves = max([int_val(q) for q in Q])
        if 'больше' in Q:
            return q_ves < self.ves
        if 'меньше' in Q:
            return q_ves > self.ves
        return q_ves + 5 >= self.ves >= q_ves - 5

    def by_mesto_uch(self, Q):
        Q = Q - MESTO_WORDS
        W = set(self.mesto_uch.split())
        rez = []
        for a, b in product(Q, W):
            rez += [(compare(a, b), a, b)]
        return max(rez)[0]

    def fuzzy_compare(self, query):
        q = set(query.split())
        score = 0
        for m, a in zip(
                [NAME_WORDS, ROST_WORDS, VES_WORDS, MESTO_WORDS],
                [self.by_name, self.by_rost, self.by_ves, self.by_mesto_uch]):
            if m & q:
                score = a(q)
        return score > 0


def compare(s1, s2):
    s1, s2 = [s.lower() for s in [s1, s2]]
    ngrams = [s1[i:i + 3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
        return count / max(len(s1), len(s2))


def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0


NAME_WORDS = {'зовут', 'имя'}
ROST_WORDS = {'ростом', 'выше', 'ниже'}
VES_WORDS = {'вес больше', 'вес', 'вес меньше'}
MESTO_WORDS = {'учится', 'учился'}

evgen = Person("Евгений", 194, 80, "пнипу")
ivan = Person("Иван", 176, 90, "пгу")
naruto = Person("Наруто", 164, 69, "штн")
people = {
    evgen.key: evgen,
    ivan.key: ivan,
    naruto.key: naruto
}

queries = [
    'зовут Евгений',
    'вес 90',
    'имя Иван',
    'рост выше 180',
    'рост ниже 170',
    'вес меньше 87',
    'учится в пнип',
    'зовут Наруто',
    'ростом 164',
    'учился штн',
]


def main():
    for query, person in product(queries, people.values()):
        if person == query:
            pprint((query, person))


if __name__ == '__main__':
    main()