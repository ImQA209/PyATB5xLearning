import pytest
import allure


@allure.title("Verify that creating booking positive cases")
@allure.description("This testcase checked for valid positive cases")
@pytest.mark.positive
def test_create_booking_positive1():
    print("This is pytest positive")
    assert 1 + 5 == 6


@allure.title("Verify that creating booking positive cases1")
@allure.description("This testcase checked for valid positive cases1")
@pytest.mark.positive1
def test_create_booking_positive2():
    print("This is positive pytest case")
    assert 1 + 2 == 3


@allure.title("Verify that creating booking negative cases")
@allure.description("This testcase checked for valid negative cases")
@pytest.mark.negative
def test_create_booking_negative2():
    print("This is negative pytest case")
    assert 1 + 2 == 4
