import inspect
import pkgutil
import unittest
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '[%(asctime)s] [%(name)s]\t[%(levelname)s] %(message)s'
)

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

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

