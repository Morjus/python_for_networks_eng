import subprocess as sub

def ping_ip_addresses(ip_list):
    reach = []
    unreach = []
    for ip in ip_list:
        ping = sub.run('ping {} -c 2'.format(ip),
        shell = True,
        stdout = sub.PIPE,
        stderr = sub.PIPE,
        encoding = 'utf-8')
        if ping.returncode == 0:
            reach.append(ip)
        else:
            unreach.append(ip)
    return reach,unreach

if __name__ == '__main__':
    ips = ['192.168.111.1','a','192.168.111.33','192.168.111.34','192.168.111.86']
    s = ping_ip_addresses(ips)
    print(s)
