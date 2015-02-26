#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from sh import fpm


def package(yaml_conf_file, injects=None, builder='fpm'):
    """\
    Generates a package with the information included in the yaml file.
    The builder variable is not yet use, since only fpm is available at
    the moment.
    """
    # todo: check for yaml config file
    # todo: check if there are parameters missing
    stream = file(yaml_conf_file, 'r')
    config = yaml.load(stream)
    gen_config = config
    fpm_args = []

    # merge injects into yaml config
    gen_config.update(injects)

    single_dash_parameter = '-%s "%s"'
    double_dash_parameter = '--%s "%s"'

    # extract all the parameters, that can't be passed
    # to fpm 1:1.
    build_vars = gen_config.pop('build-vars')
    args = gen_config.pop('args')
    input_type = gen_config.pop('input-type')
    output_type = gen_config.pop('pkg-type')
    if gen_config.has_key('chdir'):
        chdir = gen_config.pop('chdir')
        #fpm_args.append(single_dash_parameter % ('C', chdir))
        fpm_args.append("-C")
        fpm_args.append(chdir)
    if gen_config.has_key('config-files'):
        config_files = gen_config.pop('config-files')
        if type(config_files) is str:
            # fpm_args.append(double_dash_parameter % ('config-files', config_files))
            fpm_args.append("--config-files")
            fpm_args.append(config_files)
        elif type(config_files) is list:
            for config_file in config_files:
                # fpm_args.append(double_dash_parameter % ('config-files', config_file))
                fpm_args.append("--config-files")
                fpm_args.append(config_file)
    if gen_config.has_key('dependencies'):
        dependencies = gen_config.pop('dependencies')
        if type(dependencies) is str:
            # fpm_args.append(single_dash_parameter % ('d', dependencies))
            fpm_args.append("-d")
            fpm_args.append(dependencies)
        elif type(dependencies) is list:
            for dependency in dependencies:
                # fpm_args.append(single_dash_parameter % ('d', dependency))
                fpm_args.append("-d")
                fpm_args.append(dependency)

    for key, value in gen_config.items():
        param = ""
        if len(key) > 1:
            # param = double_dash_parameter % (key, value)
            fpm_args.append("--" + key)
        else:
            # param = single_dash_parameter % (key, value)
            fpm_args.append("-" + key)
        # fpm_args.append(param)
        fpm_args.append(value)

    # fpm_args.append(single_dash_parameter % ('s', input_type))
    # fpm_args.append(single_dash_parameter % ('t', output_type))
    fpm_args.append("-s")
    fpm_args.append(input_type)
    fpm_args.append("-t")
    fpm_args.append(output_type)

    if type(args) is str:
        fpm_args.append(args)
    if type(args) is list:
        for arg in args:
            fpm_args.append(arg)


    fpm(*fpm_args)

if __name__ == "__main__":
    package('configs/go.dajool.com.yaml', injects={'version': '0.123'})
