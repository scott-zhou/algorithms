import logging

class Prioritize(object):
    '''
    Class which convert dependency relationship to priority level
    '''
    def __init__(self):
        self._priorityLevel = {}

    def getPrioritizeLevel(self, item):
        if item in self._priorityLevel:
            return self._priorityLevel[item]
        return -1

    def reset(self):
        self._priorityLevel.clear()

    @staticmethod
    def _rmItemRelationship(relationship, item):
        rmRelation = set([])
        for (f, t) in relationship:
            if t == item or f == item:
                rmRelation.add((f, t))
        relationship -= rmRelation

    def convertFrom(self, dependRelations):
        """
        Return true when convert is succeed.
        The priority level is stored in _priorityLevel.
        Input args:
        dependRelations - Set of dependency relationship.
            example: set([(A, B), (A, C)]) means A depends on B and C.
        """
        self.reset()
        curLev = 0
        depent = dependRelations.copy()
        todo = set([])
        for (f, t) in depent:
            todo.add(f)
            todo.add(t)
        while todo:
            exclude = set([])
            for (f, t) in depent:
                exclude.add(f)
            curLevItem = todo - exclude
            if not curLevItem:
                logging.warning("Dependency relationship error. Circular dependency exist.")
                return False
            for item in curLevItem:
                Prioritize._rmItemRelationship(depent, item)
                self._priorityLevel[item] = curLev
            todo -= curLevItem
            curLev = curLev + 1
        return True
