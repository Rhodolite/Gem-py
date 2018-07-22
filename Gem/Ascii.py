#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.Ascii')
def gem():
    require_gem('Gem.Map')


    from Gem import execute


    show      = false
    ascii_map = {}


    class Ascii(Object):
        __slots__ = ((
            'c',                        #   String
            'ordinal',                  #   String
            'portray',                  #   String
            'pattern',                  #   String
            'is_apostrophe',            #   Boolean
            'is_backslash',             #   Boolean
            'is_portray_boring',        #   Boolean
            'is_printable',             #   Boolean
            'is_quotation_mark',        #   Boolean
        ))


        def __init__(
                t, c, ordinal, portray, pattern,

                is_apostrophe     = false,
                is_backslash      = false,
                is_printable      = false,
                is_quotation_mark = false,
        ):
            t.c       = c
            t.ordinal = ordinal
            t.portray = portray
            t.pattern = pattern

            t.is_apostrophe = is_apostrophe
            t.is_backslash  = is_backslash

            t.is_portray_boring = not (
                                         is_backslash
                                      or is_quotation_mark
                                      or not is_printable
                                      or is_apostrophe
                                  )

            t.is_printable      = is_printable
            t.is_quotation_mark = is_quotation_mark


        if __debug__:
            def __repr__(t):
                other = ''

                if t.is_apostrophe:        other += ' is_apostrophe'
                if t.is_backslash:         other += ' is_backslash'
                if t.is_portray_boring:    other += ' is_portray_boring'
                if t.is_printable:         other += ' is_printable'
                if t.is_quotation_mark:    other += ' is_quotation_mark'

                return arrange('<Ascii %r %d %r%s>', t.c, t.ordinal, t.portray, other)



    store_ascii = ascii_map.__setitem__

    def store_ascii_and_ordinal(ascii):
        store_ascii(ascii.c, ascii)
        store_ascii(ascii.ordinal, ascii)


    @execute
    def execute():
        is_special_pattern = FrozenSet(r'$()*+.?[\]^{}').__contains__

        for i in iterate_range(0, 128):
            c = character(i)

            if not (32 <= i <= 126):
                c_portray = intern_string(portray(c)[1:-1])

                store_ascii_and_ordinal(Ascii(c, i, c_portray, c_portray))
                continue

            if c == '"':
                store_ascii_and_ordinal(Ascii(c, i, c, c, is_quotation_mark = true, is_printable = true))
                continue

            if c == '\\':
                portay_backslash = intern_string(r'\\')

                store_ascii_and_ordinal(Ascii(c, i, portay_backslash, portay_backslash, is_backslash = true, is_printable = true))
                continue

            if c == "'":
                store_ascii_and_ordinal(Ascii(c, i, c, c, is_printable = true, is_apostrophe = true))
                continue

            store_ascii_and_ordinal(
                Ascii(
                    c,
                    i,
                    c,
                    (intern_string('\\' + c)    if is_special_pattern(c) else    c),
                    is_printable = true,
                ),
            )


        if show:
            for [i, k] in iterate_items_sorted_by_key(ascii_map):
                line('%r: %r', i, k)


    export(
        'lookup_ascii',     ascii_map.get,
        'unknown_ascii',    Ascii(none, none, none, none),
    )


    del Ascii.__init__
