#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.GarbageCollection')
def gem():
    #
    #   Functions
    #
    Python_GarbaseCollection = __import__('gc')


    export(
        'collect_garbage',      Python_GarbaseCollection.collect,
    )
