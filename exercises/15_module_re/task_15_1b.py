import re
from pprint import pprint

def get_ip_from_cfg(filename):
    with open(filename) as f:
        text = f.read()
    res = {}
    
    regex = (r'interface (?P<intf>Ethernet0/\d|Loopback\d)\s*.*\s*.*\s*'
    r'|ip address (?P<ip>(?:\d+\.){3}\d) (?P<mask>(?:\d+\.){3}\d+)'
    r'|ip address (?P<sec>(?:\d+\.){3}\d) (?P<secmask>(?:\d+\.){3}\d+)\s+secondary')
    list_of_tuple = []
    match = re.finditer(regex, text)
    for m in match:
        if m.lastgroup == 'intf':
            print('wow')
        ip = []
        ip.append(m.group(2))
        ip.append(m.group(3))
        res[m.group('intf')]= [tuple(ip)]
    return res
    
fin_tuple = get_ip_from_cfg('config_r2.txt')
pprint(fin_tuple)
