"""
Module to make tests folder in a package.
To run tests, use: "python manage.py test app" in terminal

Code copied from stackOverflow (with some modifications to pass pylint):
https://stackoverflow.com/questions/6248510/how-to-spread-django-unit-tests-over-multiple-files
"""
import pkgutil
import unittest


def create_test_case_class(my_object):
    """Alternative to using exec (This is safer)"""
    class_name = my_object.__name__
    return type(class_name, (my_object,), {})


for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(module_name).load_module(module_name)
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, unittest.case.TestCase):
            globals()[obj.__name__] = create_test_case_class(obj)
