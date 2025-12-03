class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people):
    person_list = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]

        wife_name = data.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = data.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
