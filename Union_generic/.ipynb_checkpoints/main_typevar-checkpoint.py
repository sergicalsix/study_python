from typing import TypeVar

T = TypeVar("T", str, int)

def test_typevar_change(p: T):
    if isinstance(p, str):
        p = 1

v: str = "1"
test_typevar_change(v)