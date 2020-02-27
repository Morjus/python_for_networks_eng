import os

def parse_cdp_neighbors(command_output):
    command_output = command_output.strip().split('\n')
    cdp = {}
    cdp_final = {}
    if 'show cdp neighbors' in command_output[0]:
        prename = command_output[0].split(' ')
        prename.remove('cdp')
        prename.remove('neighbors')
        prename = prename[0].split('>')
        name = prename[0]
        for line in command_output:
            if 'Eth' in line:
                empty = [] 
                final = []
                intf_list = []
                name_list = []
                value_list = []
                intf_0_list = [] 
                empty = line.split(' ')
                for item in empty:
                    if item != '':
                        final.append(item)
                intf = final[1]+final[2]
                intf_list.append(intf)
                name_list.append(name)
                wow = list(zip(list_name, intf_list))
                value = final[0]
                intf_0 = final[8] + final[9]
                value_list.append(value)
                intf_0_list.append(intf_0)
                wow_1 = list(zip(value_list,intf_0_list))
                cdp = dict(zip(wow, wow_1))
                cdp_final.update(cdp)
    print(cdp_final)
    return cdp_final
                        
                        
if __name__ == "__main__":
    with open ('sh_cdp_n_sw1.txt', 'r') as f:
        command = f.read()
        parse_cdp_neighbors(command)
        result = parse_cdp_neighbors(command)


