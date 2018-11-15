import numpy as np
from copy import deepcopy

class denselookup(object):
    def __init__(self,values,dims): 
        self.__dimension = 0
        whattype = type(dims)
        if whattype == np.ndarray:
            self.__dimension = 1
        else:
            self.__dimension = len(dims)        
        if self.__dimension == 0:
            raise Exception('Could not define dimension for {}'.format(whattype))
        self.__axes = deepcopy(dims)
        self.__values = deepcopy(values)
        self.__type = type(self.__values)
        
    def __call__(self,*args):        
        indices = []
        if self.__dimension == 1:
            indices.append(np.maximum(np.minimum(np.searchsorted(self.__axes, args[0], side='right')-1,self.__values.shape[0]-1),0))
        else:
            for dim in xrange(self.__dimension):
                print self.__axes[dim], self.__values.shape
                indices.append(np.maximum(np.minimum(np.searchsorted(self.__axes[dim], args[dim], side='right')-1,self.__values.shape[len(self.__axes)-dim-1]-1),0))
        indices.reverse()
        print tuple(indices)
        return self.__values[tuple(indices)]

class evaluator(object):
    def __init__(self,names,primitives):
        self.__functions = {}
        for key, idx in names.iteritems():
            self.__functions[key] = denselookup(*primitives[idx])
        
    def __getitem__(self, key):
        return self.__functions[key]
        