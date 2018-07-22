#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('Gem.System')
def gem():
    #
    #   Functions
    #
    python_frame = PythonSystem._getframe


    #
    #   Functions with bound parameters
    #
    caller_frame_0 = Method(python_frame, 0)
    caller_frame_1 = Method(python_frame, 1)


    @export
    def my_name():
        return caller_frame_1().f_code.co_name


    @built_in
    def my_line(format = none, *arguments):
        if format is none:
            assert length(arguments) is 0

            write_standard_output(caller_frame_1().f_code.co_name + '\n')
        else:
            write_standard_output(
                    (
                          caller_frame_1().f_code.co_name
                        + ': '
                        + (format % arguments   if arguments else   format)
                        + '\n'
                    ),
                )

        flush_standard_output()


    export(
        'caller_frame_1',           caller_frame_1,
        'change_check_interval',    PythonSystem.setcheckinterval,
        'fetch_check_interval',     PythonSystem.getcheckinterval,
        'module_path',              PythonSystem.path,
        'program_exit',             PythonSystem.exit,
        'python_frame',             PythonSystem._getframe,
        'python_version',           PythonSystem.version,
        'reference_count',          PythonSystem.getrefcount,
        'slice_all',                Slice(none, none),
    )
