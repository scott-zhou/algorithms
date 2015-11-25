#!/usr/bin/env python2

from prioritize import Prioritize

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
p = Prioritize()
p.convertFrom(deps)
print(p._priorityLevel)
"""
Expected result:
a: 0
d: 1
b: 2
c/g: 3
f: 4
e: 5
"""

deps = set(
    [('a', 'b'),
     ('b', 'c'),
     ('b', 'd'),
     ('c', 'e'),
     ('d', 'e'),
     ('e', 'f'),
     ('g', 'd')
     ])
p.convertFrom(deps)
print(p._priorityLevel)
"""
Expected result:
f: 0
e: 1
c/d: 2
b/g: 3
a: 4
"""

deps = set([('a', 'b')])
p.convertFrom(deps)
print(p._priorityLevel)
"""
Expected result:
b: 0
a: 1
"""

deps = set(
    [('a', 'b'),
     ('b', 'c'),
     ('c', 'a')
     ])
p.convertFrom(deps)
print(p._priorityLevel)
"""
Expected result:
ERROR
"""

