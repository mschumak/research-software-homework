# Michael Schumaker
# Unit tests for the square and circle area calculation package
# Building Research Software Lesson 3 homework 

import numpy as np
import pytest
from pytest import approx

from lesson3package import square_the_circle as stc

def test_calc_area_square_valid():
    inputs = [2, 4.0, 11.0, np.pi, "12", "2.0"]
    exp_output = [4, 16.0, 121.0, 9.87, 144, 4.0]
    for i, e in zip(inputs, exp_output):
        actual_output = stc.calc_area_square(i)
        assert actual_output == approx(e, rel=1e-4)

def test_calc_area_square_negative():
    with pytest.raises(ValueError):
        stc.calc_area_square(-2)
    with pytest.raises(ValueError):
        stc.calc_area_square(-20.0)

def test_calc_area_square_bad_type():
    with pytest.raises(TypeError):
        stc.calc_area_square([1])
    with pytest.raises(TypeError):
        stc.calc_area_square({5, 3})
    with pytest.raises(ValueError):
        stc.calc_area_square("wrong")
        
def test_calc_area_circle_valid():
    inputs = [2, 4.0, 11.0, np.pi, "12", "2.0"]
    exp_output = [12.566, 50.265, 380.133, 31.006, 452.39, 12.566]
    for i, e in zip(inputs, exp_output):
        actual_output = stc.calc_area_circle(i)
        assert actual_output == approx(e, rel=1e-4)

def test_calc_area_circle_negative():
    with pytest.raises(ValueError):
        stc.calc_area_circle(-2)
    with pytest.raises(ValueError):
        stc.calc_area_circle(-20.0)

def test_calc_area_circle_bad_type():
    with pytest.raises(TypeError):
        stc.calc_area_circle([1])
    with pytest.raises(TypeError):
        stc.calc_area_circle({5, 3})
    with pytest.raises(ValueError):
        stc.calc_area_circle("wrong")


