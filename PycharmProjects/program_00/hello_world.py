class Person(object):

    def __init__(self, name, age, height, nationality):
        self.name = name
        self.age = age
        self.height = height
        self.nationality = nationality

    def display_person(self):
        print "Name: " + self.name
        print "Age: " + str(self.age)
        print "Height: " + str(self.height)
        print "Nationality: " + self.nationality
        print "-" * (len("Nationality") + len(self.nationality) + 2)

nico = Person("Nico", 19, 6.0, "America")
javi = Person("Javi", 20, 6.2, "Spain")
nico.display_person()
javi.display_person()
