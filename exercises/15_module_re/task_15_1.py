import re
from pprint import pprint

def get_ip_from_cfg(filename):
    with open(filename) as f:
        text = f.read()
    res = []
    regex = r'ip address ((?:\d+\.){3}\d) ((?:\d+\.){3}\d+)'
    match = re.finditer(regex, text, re.DOTALL)
    for m in match:
        res.append(m.groups())
    return res
    
fin_tuple = get_ip_from_cfg('config_r1.txt')
pprint(fin_tuple)
