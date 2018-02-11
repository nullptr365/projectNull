#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 02:20:05 2018

@author: null

@Module :-> PyStack    ->   L.I.F.0

"""

import sys

# ConsT
_LIST = 0
_DICT = 1
_BACK = -1


# create a new data structure; Stack that performs the stack-(ing) operation(s)
# In this version, Operation(s) include but are not limited to:
# (1) create()      -> creates an empty stack
# (2) is_empty(stack)   -> returns True if the given stack has no data in it
# (3) size(stack)       -> returns the number of data values in the given stack
# (4) push(stack, value)     -> adds a given value to the back of the given stack
# (5) pop(stack)    -> remove the value at the front of the given stack and return it
# (6) peek(stack)   -> returns the value at the front of the given stack without remvoing it

# =============================================================================
#             -> Basic Queue Operation(s) <-
# =============================================================================

def _get_type(t):
    """
        -> SImply return the type of t
        
        @param : t      -> type to check
        
        @return :   -> type of t
    """
    return type(t)


# First attempt on chosing the data structure. WIll use a tuple of list and dict
def _create():
    """
        -> Creates and empty _stack data structure and return it <-
        
        @param : None
        
        @return :  empty _stack created  (tuple)
    """
    _struct = ([], {})      # tuple of list and dict
    return _struct


#_q = _create()

# =============================================================================
# #print(type(_q))
# 
# print(len(_q[0])); sys.exit(-1)
# =============================================================================

def _is_empty(_stack):
    """
        -> Given a _stack type; return True if _stack is empty. False otherwise <-
        
        @param : _stack  ->  _stack to check   (Queue type ->(tuple))
        
        @return :  True if empty; False otherwise  (bool)
    """
    _type = _get_type(_stack)
    
    if _type != tuple:
        print('[ TYPE_ERRoR ] TyPe Expected : {0}  -> TyPe Seen : {1}\
              '.format('tuple', _type)); sys.exit(-3)
    return True if len(_stack[_LIST]) == 0 else False


#_empty = _is_empty(_q)

#print(_empty); sys.exit(-2)

def _size(_stack):
    """
        -> Return the number of data values in _stack <-
        
        @param : _stack: Queue data structure to operate on ->  (tuple)
        
        @return  : Number of data values in _stack  (int)
                : 0 is returned if no element is in the _stack
    """
    return len(_stack[_LIST])


#_s = _size(_q)
#
#print(_s)
#
#sys.exit(-6)


def _push(_stack, value):
    """
        -> Adds a given value to the back of a given _stack  <-
        
        @param : queue  ->  _stack to add value in _stack(tuple DT)
        @param : value  -> value to add  (??)
        
        @return :       None
    """
    _type = _get_type(_stack)
    if _type is not tuple:
        print('[ TYPE_ERRoR ] TyPe Expected : {0}  -> TyPe Seen : {1}\
                  '.format('tuple', _type)); sys.exit(-3)
    getattr(_stack[_LIST], 'append')(value)
    # modify the dict rec
    if value in _stack[_DICT]:        #  it's been seen before
        _stack[_DICT][value] += 1
    else:       # first time
        _stack[_DICT][value] = 1
        

#_enqueue(_q, 3)
#_enqueue(_q, 9)
#_enqueue(_q, 9)      
#
#print(_q)
#
#sys.exit(-7)


def _pop(_stack):
    """
        -> Remove the value from the front of _stack and return it <-
        
        @param : _stack
        
        @return :  value in front of _stack  (??)
    
    """
    _val = _stack[_LIST][_BACK]
    _temp = _stack[_LIST][:_BACK]
    
#    print(_temp); sys.exit(-1)
    _stack[_LIST].remove(_val)
    _stack[_LIST][:] = _temp
    del _temp
    # look at the dictionary and keep track
    if _val in _stack[_DICT]:
        # check how many
        if _stack[_DICT][_val] == 1:     # it's count 1. delete it !!!
            del _stack[_DICT][_val]
        else:   # it's more than 1. decrement it
            _stack[_DICT][_val]  -= 1
    # ....!
            

_s = _create()

_push(_s, 10)
_push(_s, 20)
_push(_s, 30)
_push(_s, 40)
_push(_s, 50)
_push(_s, 60)
_push(_s, 70)
_push(_s, 90)
_push(_s, 40)



_pop(_s)


print(_s)



def _peek(_stack):
    """
        -> Returns the value at the front of the given queue without returning it <-
        
        @param : queue -> queue to look  (tuple DT)
        
        @return :  value in front of queue  (??)
    """
    return _stack[_LIST][_BACK]
