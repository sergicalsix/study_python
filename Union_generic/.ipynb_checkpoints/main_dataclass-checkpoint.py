from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

def test_dataclass_change(person: Person):
    if isinstance(person.name, str):
        person.name = 1

alice = Person(name='Alice', age=20)
test_dataclass_change(alice)