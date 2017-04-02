#
#   Copyright (c) 2017 Amit Green.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    module_path.insert(1, path_absolute(path_join(module_path[0], '..')))


    import Gem


@gem('Topaz.Main')
def gem():
    require_gem('Topaz.Path')
    require_gem('Topaz.Pattern')
    require_gem('Topaz.PortrayString')
    require_gem('Topaz.StringOutput')


    @share
    def main():
        test_pattern()
        test_portray_raw_string()
        test_string_output()
        test_remove_path()
        test_rename_path()