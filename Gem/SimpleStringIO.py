#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.SimpleStringIO')
def gem():
    require_gem('Gem.Import')


    if is_python_2:
        StringIO = import_module('cStringIO').StringIO
    else:
        StringIO = import_module('_io').StringIO


    @export
    def create_SimpleStringOutput():
        return StringIO()
