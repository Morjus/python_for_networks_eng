import re
from pprint import pprint
'''
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
'''

def generate_description_from_cdp(filename):
    res = {}
    with open(filename) as f:
        text = f.read()
    temp = [match.groupdict() for match in re.finditer(r'(?P<dev>R\S+)\s+(?P<local>\S+\s+\S+).+(?P<port>Eth\s+\S+)', text)]
    for item in temp:
        des = 'description Connected to {} port {}'.format(item['dev'],item['port'])
        res[item['local']] = des
    return res

    
    
if __name__ == '__main__':
    s = generate_description_from_cdp('sh_cdp_n_sw1.txt')
    pprint(s)
    
