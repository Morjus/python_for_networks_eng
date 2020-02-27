import re
from pprint import pprint
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''

def get_ints_without_description(filename):
    regex = r'interface (?P<intf>\S+)\s+(?description)'
    res = []
    with open(filename) as f:
        text = f.read()
    temp = [match.groupdict() for match in re.finditer(r'interface (?P<intf>\S+/*\d)\s+(?P<des>description)*', text)]
    for item in temp:
        if item['des'] == None:
            res.append(item['intf'])
    return res
    
if __name__ == '__main__':
    s = get_ints_without_description('config_r1.txt')
    pprint(s)
