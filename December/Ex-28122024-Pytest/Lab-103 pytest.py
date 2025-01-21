import pytest


def method():
    print("Helloword")


@pytest.mark.smoke
def test_Method1():
    print("This is pytest positive")
    assert 1 + 5 == 6


def test_Method3():
    print("This is negative pytest case")
    assert 1 + 2 == 3
