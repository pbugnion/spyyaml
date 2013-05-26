
"""
syaml
=====

A wrapper around yaml to ease reading scientific files
(and interaction with fortran).

Provides two extensions to the yaml syntax:

    * Scalars like 2e-1 are treated like floating point numbers.
       More specificially, any number that matches:
       -?\d+[e|d]-?\d+ is treated as a float.
       Thus, for instance, the following will be recognized as
       floats: 1e0, -1e-2, 2d1, -3d75
    * The literals "T" and "F" are treated as True or False, 
       respectively.

This module is designed to be imported *instead* of yaml. It 
will bring all the top-level functions of yaml into its
own namespace.
"""

import re
from yaml import *

# 1. Handling xdy

def float_constructor(loader,node):
    value = loader.construct_scalar(node)
    return float(value.replace("d","e",1))

_float_pattern = re.compile(r"-?\d+[e|d]-?\d+")

add_constructor(u"!float",float_constructor)
add_implicit_resolver(u"!float",_float_pattern)


# 2. Handling T/F

def bool_constructor(loader, node):
    value = loader.construct_scalar(node)
    return value == "T"

_bool_pattern = re.compile(r"[T|F]")

add_constructor(u"!bool",bool_constructor)
add_implicit_resolver(u"!bool",_bool_pattern)

