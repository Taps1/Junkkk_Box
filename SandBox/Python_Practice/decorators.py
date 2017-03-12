"""def foo(bar):
    return bar + 1

print foo(2) == 3
-------------------------------------------------------------
Nested Function:
--------------------------------------------------------------

def parent(number):
    print "Printing from parent function"

    def first():
        print "first child"
    def second():
        print "second child"
    def third():
        print "third child"

    try:
       assert number == 10
       return first()
    except AssertionError:
       return second()

parent(18)

------------------------------------------------------------
Decorator Call to function
------------------------------------------------------------

def my_decorator(some_func):
    def wrapper():
        print "Something is happening before some_function() is called"
        some_func()
        print "Something is happening after some_function() is called"
    
    return wrapper

def just_some_function():
    print "Wwheee!!"


just_some_function = my_decorator(just_some_function)()
#just_some_function()


-------------------------------------------------------
Decorator Call to function with "PIE" syntax
-------------------------------------------------------
def my_decorator(some_func):
    def wrapper():
        print "Something is happening before some_function() is called"
        some_func()
        print "Something is happening after some_function() is called"
    
    return wrapper

@my_decorator
def just_some_function():
    print "Wwheee!!"


just_some_function()


-------------------------------------------------------
Some real word examples
-------------------------------------------------------
"""
from time import sleep

def sleep_decorator(function):
    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper

@sleep_decorator
def print_number(num):
    print num

print_number(10)
