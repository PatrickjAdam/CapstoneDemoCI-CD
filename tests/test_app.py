import sys
import math
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, sub, mult, div,
    square, sqrt, log,
    sin, cos, percentage
)



def test_add():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-5, -3) == -8

def test_add_zero():
    assert add(0, 10) == 10


def test_subtract():
    assert sub(10, 4) == 6

def test_subtract_negative():
    assert sub(-5, -3) == -2


def test_multiply():
    assert mult(4, 5) == 20

def test_multiply_by_zero():
    assert mult(10, 0) == 0

def test_multiply_negative():
    assert mult(-3, 4) == -12


def test_divide():
    assert div(10, 2) == 5

def test_divide_float():
    assert div(1, 4) == 0.25

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

def test_square():
    assert square(5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-4) == 16


def test_square_root():
    assert sqrt(16) == 4

def test_square_root_zero():
    assert sqrt(0) == 0

def test_square_root_negative():
    with pytest.raises(ValueError):
        sqrt(-9)


def test_log():
    assert log(10) == 1

def test_log_one():
    assert log(1) == 0

def test_log_zero():
    with pytest.raises(ValueError):
        log(0)

def test_log_negative():
    with pytest.raises(ValueError):
        log(-5)


def test_sin_zero():
    assert math.isclose(sin(0), 0.0, abs_tol=1e-9)

def test_sin_90():
    assert math.isclose(sin(90), 1.0, abs_tol=1e-9)

def test_sin_180():
    assert math.isclose(sin(180), 0.0, abs_tol=1e-9)


def test_cos_zero():
    assert math.isclose(cos(0), 1.0, abs_tol=1e-9)

def test_cos_90():
    assert math.isclose(cos(90), 0.0, abs_tol=1e-9)

def test_cos_180():
    assert math.isclose(cos(180), -1.0, abs_tol=1e-9)


def test_percentage():
    assert percentage(50, 10) == 5

def test_percentage_zero():
    assert percentage(0, 50) == 0

def test_percentage_full():
    assert percentage(200, 50) == 100
