#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.Global')
def gem():
    class Gem_Global(Object):
        __slots__ = (())


        if is_python_2:
            __slots__ += ((
                'context',              #   None | Exception
            ))


        __slots__ += ((
            'crystal_parser',           #   Boolean
            'java_parser',              #   Boolean
            'python_parser',            #   Boolean
            'sql_parser',               #   Boolean
            'testing',                  #   Boolean
            'tremolite_parser',         #   Boolean
        ))


        def __init__(t):
            if is_python_2:
                t.context = none

            t.crystal_parser   = false
            t.java_parser      = false
            t.python_parser    = false
            t.sql_parser       = false
            t.testing          = false
            t.tremolite_parser = false


    gem_global = Gem_Global()


    del Gem_Global.__init__


    export(
        'gem_global',    gem_global,
    )
