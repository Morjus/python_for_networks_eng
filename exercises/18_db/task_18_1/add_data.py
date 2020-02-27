import sqlite3
import os
import re
import glob
from pprint import pprint
import yaml
from create_db import create_connection

def write_data_to_db(conection,query,data,verbose=True):
    for row in data:
        try:
            with conection:
                conection.execute(query,row)
        except sqlite3.IntegrityError as e:
            if verbose:
                print("При записи данных '{}' возникла ошибка".format(', '.join(row), e))
        else:
            if verbose:
                print("Запись данных '{}' прошла успешно".format(', '.join(row)))


def data_reader_dhcp(data_list):
    res = []
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    for data_filename in data_list:
        with open(data_filename, 'r') as f:
            for line in f:
                match = regex.search(line)
                if match:
                    temp_res = []
                    temp_res = list(match.groups())
                    temp_res.append(re.search('(sw\d)',data_filename).group())
                    res.append(tuple(temp_res))
    return res
    
def data_reader_yaml(yaml_file):
    res = []
    if '.yml' in yaml_file:
        with open(yaml_file) as f:
            hostnames = yaml.safe_load(f)
            hosts = tuple([host for host in hostnames['switches'].keys()]) 
            locations = tuple([host for host in hostnames['switches'].values()])
            res = list(zip(hosts,locations)) 
            return res
    else:
        return None
        
if __name__ == '__main__':
    res = []
    
    list_of_datas = sorted(glob.glob('*_dhcp_snooping.txt'))
    switches = data_reader_yaml('switches.yml')
    dhcp = data_reader_dhcp(list_of_datas)
    
    db_exists = os.path.exists('dhcp_snooping.db')
    con = create_connection('dhcp_snooping.db')
    
    if db_exists:
        query_for_dhcp = 'insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'
        query_for_switches = 'INSERT into switches values (?, ?)'
        print('Добавляю данные в таблицу switches...')
        write_data_to_db(con,query_for_switches,switches)
        print('Добавляю данные в таблицу dhcp...')
        write_data_to_db(con,query_for_dhcp,dhcp)
    else:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
