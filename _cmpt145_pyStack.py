#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 02:20:05 2018

@author: null

@Module :-> PyStack    ->   L.I.F.0

"""

#import sys
import matplotlib.pyplot as plt

## ConsT
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


# ADT type-check
def _check_type(_stack_type):
    """
    
    """
    
    # =============================================================================
    #           -> Nested (Assumed) Private Function <-
    # =============================================================================
    def _get_type(_stack_type):        
        """
            -> SImply return the stack type of t
            
            @param : t  -> type to check
            
            @return :   -> type of t
        """
        
        if type(_stack_type) is tuple:
            try:
                _ddt = _stack_type[0]
                assert _ddt == '_pyStack', 'TypeError: Expected _pyStack but got {0}'.format(str(type(_stack_type)))
                return '_pyStack'
            except IndexError:
                assert False, 'TypeError: Expected _pyStack but got {0}'.format(str(type(_stack_type))) 
        else:
            assert False, 'TypeError: Expected _pyStack but got {0}'.format(str(type(_stack_type)))
    
    return True if _get_type(_stack_type) == '_pyStack' else False
        



# =============================================================================
#             -> Basic Stack Operation(s) <-
# =============================================================================

    
# First attempt on chosing the data structure. WIll use a tuple of list and dict
def _create():
    """
        -> Creates and empty _stack data structure and return it <-
        
        @param : None
        
        @return :  empty _stack created  (tuple)
    """
    _struct = ([], {})      # tuple of list and dict
    return '_pyStack', _struct



def _is_empty(_stack):
    """
        -> Given a _stack type; return True if _stack is empty. False otherwise <-
        
        @param : _stack  ->  _stack to check   (Queue type ->(tuple))
        
        @return :  True if empty; False otherwise  (bool)
    """
    if _check_type(_stack):
        
        _dt, _struct = _stack    # `unpck
        return True if len(_struct[_LIST]) == 0 else False
    else:
        assert False, 'TypeError: Expected _pyStack but got {0}'.format(type(_stack))
    


def _size(_stack):
    """
        -> Return the number of data values in _stack <-
        
        @param : _stack: Queue data structure to operate on ->  (tuple)
        
        @return  : Number of data values in _stack  (int)
                : 0 is returned if no element is in the _stack
    """
    if _check_type(_stack):
        
        _dt, _struct = _stack    # `unpck
        return len(_struct[_LIST])
    else:
        assert False, 'TypeError: Expected _pyStack but got {0}'.format(type(_stack))




def _push(_stack, value):
    """
        -> Adds a given value to the back of a given _stack  <-
        
        @param : queue  ->  _stack to add value in _stack(tuple DT)
        @param : value  -> value to add  (??)
        
        @return :    None
    """
    
    if _check_type(_stack):
        _dt, _struct = _stack        
        getattr(_struct[_LIST], 'append')(value)  # stack is modified (in-place)
        # modify the dict rec
        if value in _struct[_DICT]:        #  it's been seen before
            _struct[_DICT][value] += 1
        else:       # first time
            _struct[_DICT][value] = 1
    else:
        assert False, 'TypeError: Expected _pyStack but got {0}'.format(type(_stack))
        


def _pop(_stack):
    """
        -> Remove the value from the front of _stack and return it <-
        
        @param : _stack  -> stack to remove value from
        
        @return :  value at back of _stack  (??)
    
    """
    if _check_type(_stack):
        _dt, _struct = _stack           
        try:
            _val = _struct[_LIST][_BACK]     # get the value at the back of the stack. ( Last in )
            _temp = _struct[_LIST][:_BACK]   # to preserve the order it was inserted
            _struct[_LIST].remove(_val)
            _struct[_LIST][:] = _temp
            del _temp
            
            if _val in _struct[_DICT]:
            # check how many
                if _struct[_DICT][_val] == 1:     # it's count 1. delete it !!!
                    del _struct[_DICT][_val]
                else:   # it's more than 1. decrement it
                    _struct[_DICT][_val]  -= 1
            
            return _val     # ( first out )
    
        except IndexError as e:
            return 0
        # ....!
    else:
        assert False, 'TypeError: Expected _pyStack but got {0}'.format(type(_stack))
            


def _peek(_stack):
    """
        -> Returns the value at the front of the given _stack without returning it <-
        
        @param : _stack -> _stack to look into (tuple DT)
        
        @return :  value in front of _stack  (??)
    """
    
    if _check_type(_stack):
        _dt, _struct = _stack
        return _struct[_LIST][_BACK]   #ie; _struct = tuple; ([], {}); 0= []; 1={}
    else:
        assert False, 'TypeError: Expected _pyStack but got {0}'.format(type(_stack))



# =============================================================================
#       -> Implement basic _Stack Dictionary Operation(s) <-
# =============================================================================
    
def _histogram(_stack, _char='*', _show_tab=False):  # returns x,y cords by default
    """
        -> Displays the histogram of a given _stack. Useful for plotting <-
        -> _stack remains unchanged / unmodified <-
        
        @param : _stack  -> _stack to analyze  (tuple DT)
        @param : _char  -> choice of character to represent histogram. Default='*'
        
        @return : None
    """
    _star = '\t\t ' + ' *' * (len(' [ ~ PyStack : Histogram ~ ] ') // 2)
    _title = '\t\t ' + ' [ ~ PyStack : Histogram ~ ] '
    
    # after all these operations and we have say; 1k+ data, how are we able to represent
    # this using the histogram visually without messing up the output?
    # for the purpose of this project, we will use tripple Qs (QQQ+) to represent 
    # 10+ datas. You are able to see the exact amount at the int tab value(s)
         
    if _check_type(_stack):
        _dt, _struct = _stack
        _analysis = _struct[_DICT]
        if _show_tab:
            print(); print(_star); print(_title); print(_star); print()                       
            _hist_len = 15
            # no modification to data structure. So we use only the dict type here                        
            print('{0:>16} {1:>20} {2:>25}\
                  '.format('_ValUe', '#_oCCuranCe', 'INT_VaL'))
            print('{0:>16} {1:>20} {2:>25}\
                  '.format(('*' * len('_VaLue')), ('*' * len('#_oCCuranCe')), '*' * len('INT_VaL')))
            print()
                  
            for _freq in sorted(_analysis):
                if _freq is ' ':    # pass on space
                    continue
                print('[ OUT ] {0:>5} : {1:^30}\t\t[ {2:^4} ] \
                      '.format(_freq, ((_char * _analysis[_freq]) if _analysis[_freq] < _hist_len else 'QQQ+'), _analysis[_freq]))                
            #...
        else:
            # sequencial mapping
            _sortd_x = []
            _sortd_y = []
            # for now, mamually sort the dict. (Hopefully data is not too big)
            # heres one way to sequencially  map an unordered dict key-value pair
            # without losing track of structure
            for i in sorted(_analysis):
                getattr(_sortd_x, 'append')(i)
                getattr(_sortd_y, 'append')(_analysis[i])
                
            return _sortd_x, _sortd_y
    else:
        assert False, 'TypeError: Expected _pyStack but got {0}'.format(type(_stack))


# =============================================================================
#                    ->  TeSt OperaTions <-
# =============================================================================
    
# =============================================================================
# _s = _create()
# 
# _push(_s, 10)
# _push(_s, 40)
# _push(_s, 40)
# _push(_s, 90)
# _push(_s, 20)
# _push(_s, 30)
# _push(_s, 40)
# _push(_s, 10)
# _push(_s, 50)
# _push(_s, 40)
# _push(_s, 40)
# _push(_s, 60)
# _push(_s, 70)
# _push(_s, 90)
# _push(_s, 30)
# _push(_s, 10)
# _push(_s, 60)
# #_push(_s, 40)
# 
# _push(_s, 40)
# _push(_s, 40)
# _push(_s, 40)
# _push(_s, 40)
# _push(_s, 40)
# _push(_s, 40)
# =============================================================================


#print()
#print('[ OUT ] Original EntRy : [ {0} ]'.format(_s))
#print()
#print('[ OUT ] PoPed : [ {0} ] '.format(_pop(_s)))
#print()
#print('[ OUT ] PeeKed : [ {0} ]'.format(_peek(_s)))
#print()
#print('[ OUT ] EntRy after PeeKed : [ {0} ]'.format(_s))
#print()


x, y = _histogram(_s)




plt.figure()

plt.xlabel(' -> Value(s) <-')
plt.ylabel(' -> N Occurance(s) <-')


plt.title('[ ~ pyStack Histogram ~ ]')
plt.grid()

plt.plot(x, y, 'bo')

plt.show()





#print(x, y)





















