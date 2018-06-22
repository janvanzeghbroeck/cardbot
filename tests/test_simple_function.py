
from cardbot import simple_function

# ! pytest --> to run the test
# the ! tells ipython to run it in bash
# looks to run any .py file with "test" in the beginning of the file

print('print me') # allow it to print ! pytest -s

def test_answer_fail():
    assert simple_function() == 1

def test_answer_pass():
    assert simple_function() == 2

import unittest

class TestStuff(unittest.TestCase):
    def setUp(self):
        self.thing = 2

    def test_stuff(self):
        assert self.thing == 3
