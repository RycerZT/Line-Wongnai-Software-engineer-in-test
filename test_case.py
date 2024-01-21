import unittest
from Q1 import fn

class TestBracketFunction(unittest.TestCase):

    def test_balanced_brackets(self):
        self.assertTrue(fn('{[()]}'))
        self.assertTrue(fn('{([])}'))
        self.assertTrue(fn('[{()}]'))
        self.assertTrue(fn('[()]'))

    def test_unbalanced_brackets(self):
        self.assertFalse(fn('{[()]'))
        self.assertFalse(fn('{[(])}'))
        self.assertFalse(fn('({}])'))
        self.assertFalse(fn(')('))

    def test_no_brackets(self):
        self.assertTrue(fn('abcd'))
        self.assertTrue(fn(''))
        self.assertTrue(fn('12345'))

    def test_mixed_characters(self):
        self.assertTrue(fn('a{b[c]d}e(f)g'))
        self.assertTrue(fn('abc123[def]456{ghi}'))
        
    

if __name__ == '__main__':
    unittest.main()
