import re
from pprint import pprint

def get_ip_from_cfg(filename):
    with open(filename) as f:
        text = f.read()
    res = {}
    
    regex = (r'interface (Ethernet0/\d|Loopback\d)\s*.*\s*.*\s*'
    r'ip address ((?:\d+\.){3}\d) ((?:\d+\.){3}\d+)')
    match = re.finditer(regex, text)
    for m in match:
        ip = []
        ip.append(m.group(2))
        ip.append(m.group(3))
        res[m.group(1)]= tuple(ip)
    return res
    
fin_tuple = get_ip_from_cfg('config_r2.txt')
pprint(fin_tuple)
