# -*- coding: utf-8 -*-
'''
Задание 18.2

Для заданий 18 раздела нет тестов!

В этом задании необходимо создать скрипт get_data.py.

Скрипту могут передаваться аргументы и, в зависимости от аргументов, надо выводить разную информацию.
Если скрипт вызван:
* без аргументов, вывести всё содержимое таблицы dhcp
* с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
* с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов

Файл БД можно скопировать из задания 18.1.

Примеры вывода для разного количества и значений аргументов:

$ python get_data.py
В таблице dhcp такие записи:
-----------------  ---------------  --  ----------------  ---
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2
-----------------  ---------------  --  ----------------  ---

$ python get_data.py vlan 10

Информация об устройствах с такими параметрами: vlan 10
-----------------  ----------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2
-----------------  ----------  --  ---------------  ---

$ python get_data.py ip 10.1.10.2

Информация об устройствах с такими параметрами: ip 10.1.10.2
-----------------  ---------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2  10  FastEthernet0/1  sw1
-----------------  ---------  --  ---------------  ---

$ python get_data.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

$ python get_data.py ip vlan 10
Пожалуйста, введите два или ноль аргументов

'''

import sqlite3
import os
import sys
from pprint import pprint
from tabulate import tabulate

def connect_db(db_name):
    return sqlite3.connect(db_name)

def key_maker():
    try:
        if len(sys.argv)==3:
            key, value = sys.argv[1:]
            keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
            if key in keys:
                keys.remove(key)
                return key,value
            else:
                print('Данный параметр не поддерживается.\nДопустимые значения параметров: mac, ip, vlan, interface, switch')
        elif len(sys.argv)==1:
            print('Без аргументов.')
            
            return True
        else:
            print('Пожалуйста, введите два или ноль аргументов')
    except:
        print('Some error')

def db_grab(connection, query, key, value, keys):
    if keys == None:
        result = [row for row in connection.execute(query)]
        print(tabulate(result))
    else:
        connection.row_factory = sqlite3.Row
        print('\nИнформация для хостов, где', key, '=', value)
        result = connection.execute(query,(value, ))
        print(tabulate(result))

if __name__ == '__main__':
    try:
        if len(sys.argv)>2:
            key, value = key_maker()
            query_for_dhcp = 'select * from dhcp where {} = ?'.format(key)
            con = connect_db('dhcp_snooping.db')
            keys = ['mac', 'ip', 'interface', 'switch']
            db_grab(con, query_for_dhcp, key, value, keys)
        else:

            query = 'select * from dhcp'
            con = connect_db('dhcp_snooping.db')
            db_grab(con, query, key=None, value=None, keys=None)
    except:
        print('Final error')
            
    
    
