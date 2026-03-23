class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    Person.people = {}
    for p_dict in people_dicts:
        Person(p_dict["name"], p_dict["age"])

    for p_dict in people_dicts:
        name = p_dict["name"]
        person_instance = Person.people[name]
        partner_key = "wife" if "wife" in p_dict else "husband"
        partner_name = p_dict.get(partner_key)
        if partner_name is not None:
            partner_instance = Person.people[partner_name]
            setattr(person_instance, partner_key, partner_instance)
    return list(Person.people.values())
