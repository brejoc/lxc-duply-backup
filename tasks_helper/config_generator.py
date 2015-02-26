import yaml

from jinja2 import Template, Environment, FileSystemLoader
from dict_config_parser import DictConfigParser

env = Environment(loader=FileSystemLoader('templates'))

def generate_config(template_name, config, outputfile, section="build-vars"):
    """\
    Generates a config from a template and with values from the ini config.
    """
    stream = file(config)
    config_vars = yaml.load(stream)
    script_template = env.get_template(template_name)
    with open(outputfile, "wb") as fh:
        fh.write(script_template.render(config_vars[section]))
