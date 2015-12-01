import unittest
from prioritize import Prioritize


class TestPrioritize(unittest.TestCase):
    def test_9_deps(self):
        deps = set(
            [('c', 'a'),
             ('d', 'a'),
             ('g', 'a'),
             ('c', 'b'),
             ('b', 'd'),
             ('e', 'd'),
             ('e', 'f'),
             ('f', 'g'),
             ('g', 'b'),
             ])
        pri = Prioritize()
        pri.convertFrom(deps)
        expectResult = {
            'a': 0,
            'd': 1,
            'b': 2,
            'c': 3,
            'g': 3,
            'f': 4,
            'e': 5
            }
        self.assertEqual(pri._priorityLevel, expectResult)

    def test_7_deps(self):
        deps = set(
            [('a', 'b'),
             ('b', 'c'),
             ('b', 'd'),
             ('c', 'e'),
             ('d', 'e'),
             ('e', 'f'),
             ('g', 'd')
             ])
        pri = Prioritize()
        pri.convertFrom(deps)
        expectResult = {
            'f': 0,
            'e': 1,
            'c': 2,
            'd': 2,
            'g': 3,
            'b': 3,
            'a': 4
            }
        self.assertEqual(pri._priorityLevel, expectResult)

    def test_1_deps(self):
        deps = set([('a', 'b')])
        pri = Prioritize()
        pri.convertFrom(deps)
        expectResult = {
            'b': 0,
            'a': 1
            }
        self.assertEqual(pri._priorityLevel, expectResult)

    def test_3_deps_fail(self):
        deps = set(
            [('a', 'b'),
             ('b', 'c'),
             ('c', 'a')
             ])
        pri = Prioritize()
        self.assertFalse(pri.convertFrom(deps))

if __name__ == '__main__':
    unittest.main()
