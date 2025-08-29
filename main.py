# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:48:58 2025

@author: Sebi
"""
names = ['sebipwned', 'edwardxelric', 'perlibug', 'bwwl']

from inc import sebipwned, edwardxelric, perlibug, bwwl
from inc import func

# Create a mapping from string to module
modules = {
    'sebipwned': sebipwned,
    'edwardxelric': edwardxelric,
    'perlibug': perlibug,
    'bwwl': bwwl
}

if __name__ == '__main__':
    for name in names:
        func.rm(name)

    for name in names:
        modules[name].main()


    
    
    
    
    