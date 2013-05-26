
=======
spyyaml
=======

This is a wrapper around the pyyaml library designed to extend the YAML syntax to facilitate reading or producing yaml files in a scientific context.

This provides two extensions to the yaml syntax:

- Scalars like 2e-1 are treated like floating point numbers.
   More specificially, any number that matches:
   -?\d+[e|d]-?\d+ is treated as a float.
   Thus, for instance, the following will be recognized as
   floats: 1e0, -1e-2, 2d1, -3d75
- The literals "T" and "F" are treated as True or False, 
   respectively.


Example usage
-------------

:: 

    import syaml

    input = \
    """
        start-time : 0.0
        end-time : 1e5
        optimize : T
    """

    syaml.load(input) 

    # returns a dictionary 
    { "start-time" : 0.0, "end-time" : 10000, "optimize" : True }

