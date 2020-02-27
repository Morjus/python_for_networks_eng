# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

#$ python cfg_gen.py d_link_1228_templates/d_link_1228_template.txt d_link_1228_data/ip_model_port_pvid.yml
template_dir, template_file = os.path.split(sys.argv[1])

vars_file = sys.argv[2]
ip = '10.246.100.10'
env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template(template_file)

with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)

print(template.render(vars_dict))
