class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people):
    person_objects = []

    # 1. Создаём все объекты Person
    for data in people:
        person = Person(data["name"], data["age"])
        person_objects.append(person)

    # 2. Устанавливаем wife/husband
    for data in people:
        person = Person.people[data["name"]]

        spouse_name = data.get("wife") or data.get("husband")
        if spouse_name is None:
            continue

        if "wife" in data:
            person.wife = Person.people[spouse_name]
        else:
            person.husband = Person.people[spouse_name]

    return person_objects
