from typing import Union

U = Union[str, int]

def test_union_change(p: U):
    if isinstance(p, str):
        p = 1

d: dict[str, U] = {'name': 'Alice', 'age': 20}
test_union_change(d['name'])