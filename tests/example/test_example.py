import pytest


def func(x):
    return x


def test_func():
    assert func(1) != 2
    assert func(1) == 1

