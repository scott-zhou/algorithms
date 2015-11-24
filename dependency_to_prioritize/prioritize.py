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

    def convertFrom(self, dependRelations):
        """
        Return true when convert is succeed.
        The priority level is stored in _priorityLevel.
        Input args:
        dependRelations - Set of dependency relationship.
            example: set([(A, B), (A, C)]) means A depends on B and C.
        """
        self._priorityLevel.clear()
        curLev = 0
        depent = dependRelations.copy()
        todo = set([])
        for (f, t) in depent:
            todo.add(f)
            todo.add(t)
        while todo:
            if not depent:
                print("ERROR: No depend relationship when have item in todo list.")
                print todo
                print depent
                return False
            rmRelation = set([])
            rmItem = set([])
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
            if len(depent) == 1:
                (f, t) = depent.pop()
                self._priorityLevel[t] = curLev
                self._priorityLevel[f] = curLev+1
                rmItem.clear()
                rmItem.add(f)
                rmItem.add(t)
                todo -= rmItem
                for left in todo:
                    self._priorityLevel[left] = curLev
                todo.clear()
            print("current stution, todo list:", todo)
            print("current stution, depent list:", depent)
        return True
