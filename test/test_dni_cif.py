from src.dni_cif import DNI
import pytest


@pytest.mark.test_dni
def test_dni():

    casosTest = [
        "78484464T", "72376173A", "01817200Q", "95882054E", "63587725Q",
        "26861694V", "21616083Q", "26868974Y", "40135330P", "89044648X",
        "80117501Z", "34168723S", "76857238R", "66714505S", "66499420A", "41660450K"]

    for dni in casosTest:
        test = DNI(dni)
        assert test.check_cif() == True


@pytest.mark.test_get_dni
def test_get_dni():

    test = DNI('76857238R')
    assert '76857238R' == test.get_dni()


@pytest.mark.test_get_healthy_number
def test_get_healthy_number():

    test = DNI('76857238R')
    assert False == test.get_healthy_number()


@pytest.mark.test_get_healthy_letter
def test_get_healthy_letter():

    test = DNI('76857238R')
    assert False == test.get_healthy_letter()


@pytest.mark.test_calculate_letter
def test_calculate_letter():

    test = DNI('76857238R')
    assert True == isinstance(test.calculate_letter(), int)


@pytest.mark.test_obtain_letter
def test_obtain_letter():

    test = DNI('41660450K')
    test.set_healthy_number(True)
    assert 'K' == test.obtain_letter()
