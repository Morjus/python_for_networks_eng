import os
from parse_v2 import parse_cdp_neighbors as parse 
from draw_network_graph import *

file_list = [
'sh_cdp_n_sw1.txt', 
'sh_cdp_n_r1.txt', 
'sh_cdp_n_r2.txt',
'sh_cdp_n_r3.txt'
]

def create_network_map(filenames):
    res = {}
    for item in filenames:
        with open (item, 'r') as f:
            command = f.read()
            result = parse(command)
            res.update(result)
    return res


if __name__ == "__main__":
    network = create_network_map(file_list)
    print(network)
    draw_topology(network)

