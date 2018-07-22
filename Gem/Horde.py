#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.Horde')
def gem():
    require_gem('Gem.Herd')


    #
    #   Horde:  Like a Herd, but has a 'skip' factor
    #


    map__contains = Map.__contains__
    map__lookup   = Map.get
    map__provide  = Map.setdefault
    map__store    = Map.__setitem__


    def increment_skip__horde_many(t, skip = 1):
        assert (1 <= skip <= 2) and (0 <= t.skip <= 1) and (skip + t.skip <= 2)

        t.skip += skip

        return t


    def remove_skip__horde(t, skip = 1):
        assert skip <= t.skip <= 2
        assert 1 <= skip <= 2

        t.skip -= skip

        return t


    class Horde_23(Object):
        __slots__ = ((
            'skip',                     #   Integer { 0 | 1 }
            '_sample',                  #   Absent | Any excluding Absent
            'a',                        #   Any excluding Absent
            'b',                        #   Any excluding Absent
            'c',                        #   Absent | Any excluding Absent
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Vacant | Any
        ))


        herd_estimate = 3
        is_herd       = true
        is_horde      = true
        k1            = absent
        k2            = absent
        k3            = absent
        k4            = absent


        def __repr__(t):
            if t.c is absent:
                return arrange('<Horde_23 %d %r; %r : %r; %r : %r>',
                               t.skip, t._sample, t.a, t.v, t.b, t.w)

            return arrange('<Horde_23 %d %r; %r : %r; %r : %r; %r : %r>',
                           t.skip, t._sample, t.a, t.v, t.b, t.w, t.c, t.x)


        def count_nested(t):
            v = t.v
            w = t.w

            if t.c is absent:
                if v.is_herd:
                    if w.is_herd:
                        return v.count_nested() + w.count_nested()

                    return v.count_nested() + 1

                if w.is_herd:
                    return 1 + w.count_nested()

                return 2

            x = t.x

            if v.is_herd:
                if w.is_herd:
                    if x.is_herd:
                        return v.count_nested() + w.count_nested() + x.count_nested()

                    return v.count_nested() + w.count_nested() + 1

                if x.is_herd:
                    return v.count_nested() + 1 + x.count_nested()

                return v.count_nested() + 2

            if w.is_herd:
                if x.is_herd:
                    return 1 + w.count_nested() + x.count_nested()

                return 2 + w.count_nested()         #  1 + w.count_nested() + 1

            if x.is_herd:
                return 2 + x.count_nested()

            return 3


        def displace(t, k, v):
            assert v is not absent

            if t.a is k:
                t._sample = absent
                t.v       = v
                return

            if t.b is k:
                t.w = v
                return

            assert t.c is k

            t.x = v


        def distribute_triple(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            v    = t.v
            v_k2 = v.k2

            if v_k2 is not k2:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k1, create_herd_2(v_k2, k2, t, r))

                return r

            a = t.a
            if a is k3:     return v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.x

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k3
                t.x = r
                return r

            assert t.skip is 1

            displace(k1, create_horde_many(1, a, b, c, k3, v, t.w, t.x, r))

            return r


        def distribute_triple__312(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            v    = t.v
            v_k1 = v.k1

            if v_k1 is not k1:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k3, create_herd_2(v_k1, k1, t, r))

                return r

            a = t.a
            if a is k2:     return v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k2
                t.x = r
                return r

            displace(k3, create_horde_many(1, a, b, c, k2, v, t.w, t.x, r))

            return r


        def distribute_triple_step2(t, displace, parent, Meta, k1, k2, k3):
            assert t.skip is 0

            a = t.a
            if a is k3:     return t.v

            b = t.b
            if b is k3:     return t.w

            c = t.c
            if c is k3:     return t.w

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k3
                t.x = r
                return r

            if parent.is_herd_many:
                displace(parent, k2, create_herd_4(a, b, c, k3, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4(a, b, c, k3, t.v, t.w, t.x, r))
            return r


        def distribute_triple_step2__312(t, displace, parent, Meta, k1, k2, k3):
            assert t.skip is 0

            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.w

            r = Meta(k1, k2, k3)

            if c is absent:
                t.c = k2
                t.x = r
                return r

            if parent.is_herd_many:
                displace(parent, k1, create_herd_4(a, b, c, k2, t.v, t.w, t.x, r))
                return r

            displace(parent, create_herd_4(a, b, c, k2, t.v, t.w, t.x, r))
            return r


        def glimpse(t, k, d = none):
            if t.a is k: return t.v
            if t.b is k: return t.w
            if t.c is k: return t.x

            assert k is not absent

            return d


        def insert(t, d, y):
            assert (d is not absent) and (t.a is not d) and (t.b is not d) and (t.c is not d) and (y is not absent)

            if t.c is absent:
                t.c = d
                t.x = y
                return t

            if t.skip is 0:
                return create_herd_4(t.a, t.b, t.c, d, t.v, t.w, t.x, y)

            return create_horde_many(t.skip, t.a, t.b, t.c, d, t.v, t.w, t.x, y)


        increment_skip = increment_skip__horde_many


        def items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))
            ka = nub(a)
            kb = nub(b)

            if c is absent:
                if ka < kb:
                    return ((av, bw))

                return ((bw, av))

            cx = ((c, t.x))
            kc = nub(c)

            if ka < kb:
                if kb < kc:
                    return ((av, bw, cx))

                if ka < kc:
                    return ((av, cx, bw))

                return ((cx, av, bw))

            if ka < kc:
                return ((bw, av, cx))

            if kb < kc:
                return ((bw, cx, av))

            return ((cx, bw, av))


        def sample(t):
            sample = t._sample

            if sample is not absent:
                return sample

            sample = t.v

            while sample.is_herd:
                if sample.is_horde:
                    t._sample = sample = sample.sample()
                    return sample

                sample = sample.first

            t._sample = sample

            return sample


        def scrub(t):
            v       = t.v
            v_scrub = v.scrub
            if v_scrub is 0:
                if v is t._sample:
                    #rc = reference_count(v)
                    #my_line('v<%r> is t._sample; rc: %d', v, rc)

                    if reference_count(v) is 4:
                        t._sample = absent
                        v         = 0
                else:
                    if reference_count(v) is 3:
                        v = 0
            else:
                t._sample = absent
                v         = v_scrub()

            w       = t.w
            w_scrub = w.scrub
            if w_scrub is 0:
                if reference_count(w) is 3:
                    w = 0
            else:
                w = w_scrub()

            if t.c is absent:
                if v is 0:
                    if w is 0:
                        return 0

                    w_increment = w.increment_skip
                    return (w   if w_increment is 0 else    w_increment(t.skip + 1))

                if w is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment(t.skip + 1))

                t._sample = absent
                t.v       = v
                t.w       = w
                return t

            x       = t.x
            x_scrub = x.scrub
            if x_scrub is 0:
                if reference_count(x) is 3:
                    x = 0
            else:
                x = x_scrub()

            if v is 0:
                if w is 0:
                    if x is 0:
                        return 0

                    x_increment = x.increment_skip
                    return (x   if x_increment is 0 else    x_increment(t.skip + 1))

                if x is 0:
                    w_increment = w.increment_skip
                    return (w   if w_increment is 0 else    w_increment(t.skip + 1))

                #
                #   scrub .a/.v
                #
                t._sample = absent
                t.a       = t.b
                t.v       = w

                t.b = t.c
                t.w = x

                t.c = absent
                del t.x
                return t

            if w is 0:
                if x is 0:
                    v_increment = v.increment_skip
                    return (v   if v_increment is 0 else    v_increment(t.skip + 1))

                #
                #   scrub .b/.w
                #
                if t.v is not v:
                    t._sample = absent
                    t.v       = v

                t.b = t.c
                t.w = x

                t.c = absent
                del t.x
                return t

            if t.v is not v:
                t._sample = absent
                t.v       = v

            t.w = w

            if x is 0:
                #
                #   scrub .c/.x
                #
                t.c = absent
                del t.x
            else:
                t.x = x

            return t


        remove_skip = remove_skip__horde


    class Horde_Many(Map):
        __slots__ = ((
            'skip',                     #   Integer { 0 | 1 }
            '_sample',                  #   Absent | Any excluding Absent
        ))


        herd_estimate = 8
        is_herd       = true
        is_horde      = true
        k1            = absent
        k2            = absent
        k3            = absent
        k4            = absent


        def __repr__(t):
            return arrange('<Horde_Many %d %r; %s>',
                           t.skip,
                           t._sample,
                           '; '.join(arrange('%r : %r', k, v)   for [k, v] in t.items_sorted_by_key()))


        count_nested = count_nested__map
        disperse     = disperse__herd_many


        if __debug__:
            def displace(t, k, v):
                assert (map__contains(t, k)) and (k is not absent) and (v is not absent)

                t._sample = absent
                t[k]      = v
        else:
            displace = map__store


        def distribute_triple(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            sample_k2 = t.sample().k2

            if sample_k2 is not k2:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k1, create_herd_2(sample_k2, k2, t, r))

                return r

            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


        def distribute_triple__312(t, displace, Meta, k1, k2, k3):
            assert t.skip is 1

            sample_k1 = t.sample().k1

            if sample_k1 is not k1:
                t.skip = 0
                r      = Meta(k1, k2, k3)

                displace(k3, create_herd_2(sample_k1, k1, t, r))

                return r

            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2, k3)))


        def distribute_triple_step2(t, _displace, _parent, Meta, k1, k2, k3):
            assert t.skip is 0

            return (map__lookup(t, k3)) or (map__provide(t, k3, Meta(k1, k2, k3)))


        def distribute_triple_step2__312(t, _displace, _parent, Meta, k1, k2, k3):
            assert t.skip is 0

            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2, k3)))


        increment_skip = increment_skip__horde_many
        glimpse        = map__lookup


        def inject(t, k, v):
            assert (map__lookup(t, k) is none) and (k is not absent) and (v is not absent)

            map__store(t, k, v)
            return t


        insert              = inject
        items_sorted_by_key = items_sorted_by_key__herd_many


        remove_skip = remove_skip__horde


        if is_python_2:
            def sample(t):
                sample = t._sample

                if sample is not absent:
                    return sample

                sample = t.itervalues().next()

                while sample.is_herd:
                    if sample.is_horde:
                        t._sample = sample = sample.sample()
                        return sample

                    sample = sample.first

                t._sample = sample

                return sample
        else:
            def sample(t):
                sample = t._sample

                if sample is not absent:
                    return sample

                sample = iterate(t.values()).__next__()

                while sample.is_herd:
                    if sample.is_horde:
                        t._sample = sample = sample.sample()
                        return sample

                    sample = sample.first

                t._sample = sample

                return sample


        def scrub(t):
            append_remove = 0
            value         = t.__getitem__
            store         = t.__setitem__

            t._sample = absent

            for k in t.keys():
                v       = value(k)
                v_scrub = v.scrub

                if v_scrub is 0:
                    if reference_count(v) is not 3:
                        continue

                    if append_remove is 0:
                        remove_many = [k]
                        append_remove = remove_many.append
                        continue

                    append_remove(k)
                    continue


                v = v_scrub()

                if v is 0:
                    if append_remove is 0:
                        remove_many = [k]
                        append_remove = remove_many.append
                        continue

                    append_remove(k)
                    continue

                store(k, v)

            if append_remove is 0:
                return t

            if length(remove_many) == length(t):
                return 0

            zap = t.__delitem__

            for k in remove_many:
                zap(k)

            if length(t) is 1:
                if is_python_2:
                    v = t.itervalues().next()
                else:
                    v = iterate(t.values()).__next__()

                v_increment = v.increment_skip
                return (v   if v_increment is 0 else    v_increment(t.skip))

            return t


    new_Horde_23   = Method(Object.__new__, Horde_23)
    new_Horde_Many = Method(Map   .__new__, Horde_Many)


    @export
    def create_horde_2(skip, a, b, v, w):
        assert (1 <= skip <= 2) and (a is not absent) and (a is not b) and (b is not absent)
        assert (v is not absent) and (w is not absent)

        t = new_Horde_23()

        t.skip    = skip
        t._sample = absent
        t.a       = a
        t.b       = b
        t.c       = absent
        t.v       = v
        t.w       = w

        return t


    @share
    def create_horde_3(skip, a, b, c, v, w, x):
        assert 1 <= skip <= 2
        assert (a is not absent) and (a is not b) and (a is not c)
        assert (b is not absent) and (b is not c)
        assert c is not absent
        assert (v is not absent) and (w is not absent) and (x is not absent)

        t = new_Horde_23()

        t.skip    = skip
        t._sample = absent
        t.a       = a
        t.b       = b
        t.c       = c
        t.v       = v
        t.w       = w
        t.x       = x

        return t


    @export
    def create_horde_many(skip, a, b, c, d, v, w, x, y):
        assert 1 <= skip <= 2
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert d is not absent
        assert (v is not absent) and (w is not absent) and (x is not absent) and (y is not absent)

        t = new_Horde_Many()

        t.skip    = skip
        t._sample = v
        t[a]      = v
        t[b]      = w
        t[c]      = x
        t[d]      = y

        return t
