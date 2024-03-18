"""
Module to make tests folder in a package.
To run tests, use: "python manage.py test app" in terminal

Code copied from stackOverflow:
https://stackoverflow.com/questions/6248510/how-to-spread-django-unit-tests-over-multiple-files
"""
import pkgutil
import unittest

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(module_name).load_module(module_name)
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, unittest.case.TestCase):
            exec('%s = obj' % obj.__name__)
