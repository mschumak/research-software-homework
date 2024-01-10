# Michael Schumaker
# Unit tests for the square and circle area calculation package
# Building Research Software Lesson 3 homework 

import numpy as np
from pytest import approx
import lesson3package

def load_from_file(filename):
    radii = np.loadtxt(filename)
    return radii

def calc_area_circle(radii):
    areas = np.pi * radii**2
    return areas

def test_load_and_calculate():
    #### Generate test case ####
    # save list of radii
    np.array([5.2, 1.1, 9.3, 11.4, 19.2]).savetxt('radii.txt')

    #### Run function ####
    # load list of radii
    radii_list = load_from_file('radii.txt')

    # calculate area
    area_list = calc_area_circle(radii_list)

    #### Test result ####
    assert area_list == approx([84.95, 3.8, 271.7, 408.3, 1158.1])



import pytest
import mycode


def test_calc_area_square():
    inputs = [2, 4, 10]
    exp_output = [4, 16, 100]

    for i, e in zip(inputs, exp_output):
        actual_output = mycode.calc_area_square(i)
        assert actual_output == e


def test_calc_area_square_negative():
    with pytest.raises(ValueError):
        mycode.calc_area_square(-10)


