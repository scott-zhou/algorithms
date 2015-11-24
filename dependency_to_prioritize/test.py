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