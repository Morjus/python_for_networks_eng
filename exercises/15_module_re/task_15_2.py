import re
from pprint import pprint 
'''
Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]


'''
def parse_sh_ip_int_br(filename):
    with open(filename, 'r') as f:
        text = f.read()
    regex = (r'(\S+) +([\d.]+|\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)')
    return [match.groups() for match in re.finditer(regex, text)]
    
s = parse_sh_ip_int_br('sh_ip_int_br.txt')
pprint(s)
