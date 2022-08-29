import pytest


def sumfind(n):
    count = 0
    for i in range(1, n + 1):
        count = count + i
    return count;


def test_me():
    assert 15 == sumfind(6)
