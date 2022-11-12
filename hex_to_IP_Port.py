def get_ip(hexed_ip):
    lst = []
    for i in range(0, len(hexed_ip), 2):
        lst.append(str(int(hexed_ip[i:i + 2], 16)))
    lst.reverse()
    print(".".join(lst))


def get_port(hexed_port):
    port = hexed_port[2:4] + hexed_port[0:2]
    print(int(port, 16))


if __name__ == "__main__":
    ip_hex = "1DCBA8C0"
    port_hex = "4334"

    get_ip(ip_hex)
    get_port(port_hex)
