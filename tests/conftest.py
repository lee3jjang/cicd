import pytest
from cicd.arithmetic import Calculator

@pytest.fixture
def calc():
    calculator = Calculator()
    return calculator