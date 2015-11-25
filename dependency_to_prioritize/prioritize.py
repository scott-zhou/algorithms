class Prioritize(object):
    '''
    Class which convert dependency relationship to priority level
    '''
    def __init__(self):
        self._priorityLevel = {}

    def _haveDependency(self, item, dependRelations):
        for (f, t) in dependRelations:
            if item == f:
                return True
        return False

    def getPrioritizeLevel(self, item):
        if item in self._priorityLevel:
            return self._priorityLevel[item]
        return -1

    def reset(self):
        self._priorityLevel.clear()

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
            rmRelation = set([])
            rmItem = set([])
            if len(depent) == 1:
                (f, t) = depent.pop()
                self._priorityLevel[t] = curLev
                self._priorityLevel[f] = curLev+1
                rmItem.add(f)
                rmItem.add(t)
                todo -= rmItem
                for left in todo:
                    self._priorityLevel[left] = curLev
                todo.clear()
                break
            if not depent:
                print("ERROR: No depend relationship when have item in todo list.")
                return False
            for item in todo:
                if self._haveDependency(item, depent):
                    continue
                self._priorityLevel[item] = curLev
                for (f, t) in depent:
                    if t == item:
                        rmRelation.add((f, t))
                rmItem.add(item)
            if not rmRelation:
                print("ERROR: dependency relationship error. Circular dependency exist.")
                return False
            depent -= rmRelation
            todo -= rmItem
            curLev = curLev + 1
        return True
