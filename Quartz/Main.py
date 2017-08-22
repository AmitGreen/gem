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


@gem('Quartz.Main')
def gem():
    require_gem('Quartz.Core')
    require_gem('Quartz.Pattern')


    @share
    def main():
        create_quartz_match()

        require_gem('Quartz.Parse1')                            #   Must be after 'create_quartz_match'

        parse1_mysql_from_path('test.sql')