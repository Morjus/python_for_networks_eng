# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint

def parse_sh_cdp_neighbors(command_output):
    regex_for_host = r'(?P<switch>\S+)>show.+'
    hostname = re.search(regex_for_host, command_output).group('switch')
    regex = r'(?P<device>\w+\d) +(?P<loc_int>\w+\s\S+) +.+(?P<port_id>Eth\s\S+)'
    res = {hostname: {match.group('loc_int'): {match.group('device'):match.group('port_id')} for match in re.finditer(regex, command_output)} for match in re.finditer(regex, command_output)}
    
    return res
    
if __name__ == '__main__':
    with open ('sh_cdp_n_sw1.txt', 'r') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))
    
