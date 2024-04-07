from typing import Union

def test_union_change(p):
    if isinstance(p, str):
        p = 1
    elif isinstance(p, int):
        p = "1"

U = Union[str, int] # str | int でも可
v: U = "1"
test_union_change(v)

d: dict[str, U] = {'name': 'Alice', 'age': 20}
test_union_change(d['name'])
test_union_change(d['age'])