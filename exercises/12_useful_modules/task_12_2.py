from ipaddress import ip_address

def convert_ranges_to_ip_list(ip_list):
    res = []
    for ip in ip_list:
        try:
            if ip_address(ip):
                res.append(ip)
        except ValueError:
            range_list = ip.split('-')
            try:
                if ip_address(range_list[0]) and ip_address(range_list[1]):
                    ip1 = range_list[0].split('.')
                    ip2 = range_list[1].split('.')
                    ip_1 = ip1[3]
                    ip_2 = ip2[3]
                    ip1.pop(3)
                    ip2.pop(3)
                    res_ip = '.'.join(ip1)
                    new_list = [res_ip+'.'+str(i) for i in range(int(ip_1),int(ip_2)+1)]
                    res.extend(new_list)
            except ValueError:
                ip1 = range_list[0].split('.')
                ip_2 = range_list[1]
                ip_1 = ip1[3]
                ip1.pop(3)
                res_ip = '.'.join(ip1)
                new_list = [res_ip+'.'+str(i) for i in range(int(ip_1),int(ip_2)+1)]
                res.extend(new_list)
    return res
    
if __name__ == '__main__':
    ips = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    res = convert_ranges_to_ip_list(ips)
    print(res)
