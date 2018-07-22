#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.DumpCache')
def gem():
    require_gem('Gem.Absent')
    require_gem('Gem.Herd')
    require_gem('Gem.Horde')
    require_gem('Gem.LiquidMap')


    @export
    def dump_cache(f, cache, show_sample = true):
        f.line('===  %s  ===', cache.name)

        for [k, v] in cache.items_sorted_by_key():
            if not v.is_herd:
                f.line('%s: %s',
                     (
                        portray_string(k)  if k.__class__ is String  else
                        k                  if k.__class__ is Integer else
                        k.display_token()
                     ),
                     v.display_token())

                continue

            f.line('%s: (%s)',
                 (
                    portray_string(k)  if k.__class__ is String  else
                    k                  if k.__class__ is Integer else
                    k.display_token()
                 ),
                 v.__class__.__name__)

            prefix_1 = '  '

            if v.skip is not 0:
                f.line('%sskip %d; sample: %s',
                       prefix_1,
                       v.skip,
                       (v.sample()   if show_sample else   'not shown on purpose'))

                prefix_1 += ('  ' * v.skip)

            for [k2, w] in v.items_sorted_by_key():
                if not w.is_herd:
                    f.line('%s%s: %s',
                         prefix_1,
                         (
                            portray_string(k2)  if k2.__class__ is String  else
                            k2                  if k2.__class__ is Integer else
                            k2.display_token()
                         ),
                         w.display_token())

                    continue

                f.line('%s%s: (%s)',
                     prefix_1,
                     (
                        portray_string(k2)  if k2.__class__ is String  else
                        k2                  if k2.__class__ is Integer else
                        k2.display_token()
                     ),
                     w.__class__.__name__)

                prefix_2 = prefix_1 + '  '

                if w.skip is not 0:
                    f.line('%sskip %d; sample: %s',
                           prefix_2,
                           w.skip,
                           (w.sample()   if show_sample else   'not shown on purpose'))

                    prefix_2 += ('  ' * w.skip)

                for [k3, x] in w.items_sorted_by_key():
                    if not x.is_herd:
                        f.line('%s%s: %s', prefix_2, k3.display_token(), x.display_token())
                        continue

                    f.line('%s%s: (%s)', prefix_2, k3.display_token(), x.__class__.__name__)

                    prefix_3 = prefix_2 + '  '

                    for [k4, y] in x.items_sorted_by_key():
                        f.line('%s%s:  %s', prefix_3, k4.display_token(), y.display_token())


    @export
    def dump_cache_to_string(cache, show_sample = true):
        with create_StringOutput() as f:
            dump_cache(f, cache, show_sample = show_sample)

        return f.result


    @export
    def print_cache(use_cache = none):
        if use_cache is none:
            line('Total caches: %d', length(cache_names))

            for [name, cache] in cache_names.items_sorted_by_key():
                line('%s: %d', name, cache.count_nested())

            return

        cache = (cache_names[use_cache]   if type(use_cache) is String else  use_cache)

        partial(dump_cache_to_string(cache))
