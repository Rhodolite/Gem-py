#
#   Copyright (c) 2018 Joy Diamond.  All rights reserved.
#
@gem('Gem.Sleep')
def gem():
    PythonTime = __import__('time')


    export(
        'sleep',    PythonTime.sleep,
    )
