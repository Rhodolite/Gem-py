#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.IO')
def gem():
    export(
        #
        #   Insanely enough, the python 2 'input' function actually evaluated the input!
        #   We use the python 3 meaning of 'input' -- don't evaluate the input
        #
        'input',        (PythonBuiltIn.raw_input   if is_python_2 else   PythonBuiltIn.input),
    )
