import pytest
def fn(x):
    return x + 1


def test_check():

    assert fn(3) == 4
