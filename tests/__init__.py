import inspect
import pkgutil
import unittest

def load_tests(loader, suite, pattern):
    """
    Import all local testing submodules here, so that ``gromp``
    is accessible for even the deeper tests.
    https://stackoverflow.com/questions/29713541/recursive-unittest-discover
    """
    for imp, modname, _ in pkgutil.walk_packages(__path__):
        mod = imp.find_module(modname).load_module(modname)
        for test in loader.loadTestsFromModule(mod):
            suite.addTests(test)

    return suite

