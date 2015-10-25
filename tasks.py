# -*- coding: utf-8 -*-

import os
import sys
import yaml
from invoke import run, task
from basalt.tasks import *

@task()
def clean(*args, **kwargs):
    """\
    Remove all build files, configs and packages."
    """
    run("rm -rf ./build")
    run("rm -rf ./build_configs")
    run("rm -f *.deb")


@task("clean", "prepare_paths", "config_duply_config", "config_post", "config_pre", "config_exclude", "config_cron_job")
def build(config):
    """\
    Prepares the build and generates the package.
    """
    # get values from config
    stream = file(config, 'r')
    config_values = yaml.load(stream)

    build_path_config = "./build" + config_values['build-vars']['config_path']

    # copy configs and scripts
    run("cp ./build_configs/conf %s/." % (build_path_config, ))
    run("cp ./build_configs/exclude %s/." % (build_path_config, ))
    run("cp ./build_configs/post %s/." % (build_path_config, ))
    run("cp ./build_configs/pre %s/." % (build_path_config, ))

    # copy cron job to /etc/cron.d/
    run("cp ./build_configs/lxc_backup_%s ./build/etc/cron.d/" % (config_values['build-vars']['container_name'], ))
    run("chmod 644 ./build/etc/cron.d/lxc_backup_%s" % (config_values['build-vars']['container_name'], ))

    
    # generate version number
    version = "%(major)s.%(minor)s" % \
        {
            'major': get_major_version(), 
            'minor': get_minor_version()
        }

    package(config, {'version': version})
    

@task()
def prepare_paths(config):
    """\
    Prepare folder structure.
    """
  
    # get values from config
    stream = file(config, 'r')
    config_values = yaml.load(stream)

    mkdirp("./build_configs")
    
    # mkdir config folder for duply
    mkdirp("./build%s" % ( config_values['build-vars']['config_path']))

    # create folger for cron job
    mkdirp("./build/etc/cron.d/")


@task
def config_duply_config(config):
    """\
    Generate duply config from template.
    """
    generate_config("conf",
                    config,
                    os.path.join("build_configs", "conf"))


@task
def config_post(config):
    """\
    Generate post backup execution script from template.
    """
    generate_config("post",
                    config,
                    os.path.join("build_configs", "post"))


@task
def config_pre(config):
    """\
    Generate pre backup execution script from template.
    """
    generate_config("pre",
                    config,
                    os.path.join("build_configs", "pre"))


@task
def config_exclude(config):
    """\
    Generate exclude config from template.
    """
    generate_config("exclude",
                    config,
                    os.path.join("build_configs", "exclude"))


@task
def config_cron_job(config):
    """\
    Generate cron job from template.
    """
    # get values from config
    stream = file(config, 'r')
    config_values = yaml.load(stream)

    generate_config("cron_job",
                    config,
                    os.path.join("build_configs", "lxc_backup_%s" % (config_values['build-vars']['container_name'])))
