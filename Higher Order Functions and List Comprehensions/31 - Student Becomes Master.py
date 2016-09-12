'''
Implement the higher order functions map(), filter() and reduce().
(They are built-in but writing them yourself may be a good exercise.)
'''

# The solutions below are were based on this definition from http://www.python-course.eu/lambda.php

example = ['Apple','Jack','Google']

# my implementation of the map() function
def my_map(function, sequence):
    result = []
    for i in sequence:
        result.append(function(i))
    return result

# my implementation of the filter() function
def my_filter(function, list):
    result = []
    for item in list:
        if item:
            result += item
    return result