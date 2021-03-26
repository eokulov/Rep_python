from pprint import pprint
class Person:
    def __init__(self, name, rost, ves, mesto_uch):
        self.name, self.rost, self.ves, self.mesto_uch = name, rost, ves, mesto_uch
        self.key = (name, mesto_uch)
    def __repr__(self):
        return "Person('%s',%s,%s,'%s')" % (self.name, self.rost, self.ves, self.mesto_uch)
evgen = Person("evgen", 194, 80, "pnipu")
ivan = Person("Ivan", 176, 90, "psu")
naruto = Person("Naruto", 164, 69, "shtn")
people = {
    evgen.key: evgen,
    ivan.key: ivan,
    naruto.key: naruto
}
pprint(people)
pprint(people[evgen.key])
