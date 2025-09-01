# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 16:36:16 2025

@author: cj8q21
"""

import shutil
import os

def func(_input, _input2, _output, _reltion, _replaceOLD, _replaceNEW, _replace2OLD, _replace2NEW, _StringAddOn):
    __output = ""
    if _input != "":
        with open(_input,'r') as file:
            __input = " ".join(line.rstrip() for line in file)
        __output = __output + __input
    if _input2 != "":
        with open(_input2,'r') as file:
            __input2 = " ".join(line.rstrip() for line in file)
        __output = __output + "," + __input2
    if _reltion != "":
        with open(_reltion,'r') as file:
            __relation = " ".join(line.rstrip() for line in file)
        __output = __output + "," + __relation
    if _replaceOLD != _replaceNEW:
        __output = __output.replace(_replaceOLD, _replaceNEW)
    if _replace2OLD != _replace2NEW:
        __output = __output.replace(_replace2OLD, _replace2NEW)
        
    f = open(_output, 'w')
    f.write(__output + _StringAddOn)
    f.close()
    
    
def rm(_name):
    for name in _name:
        shutil.rmtree('output/' + name + '')
        os.mkdir('output/' + name + '')
        os.mkdir('output/' + name + '/check')
        os.mkdir('output/' + name + '/trade')
    
    base_dir = 'output'
    
    for name in _name:
            user_dir = os.path.join(base_dir, name)
            os.makedirs(user_dir, exist_ok=True)
    
            for other_name in _name:
                if other_name != name:
                    sub_dir = os.path.join(user_dir, other_name)
                    os.makedirs(sub_dir, exist_ok=True)

    
if __name__ == "__main__":
    pass