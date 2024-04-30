import time
import socket, threading

e = False
percentage = 1

def print_percent():
    global percentage
    e = True
    while e:
        percentage += 1
        print(f"{percentage}% Done...")
        time.sleep(0.1)
    time.sleep(10)
    e = False




def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''


def scan_ports(ip, delay):

    threads = []
    output = {}

    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    for i in range(10000):
        threads[i].start()

    for i in range(10000):
        threads[i].join()

    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])








def main():
    ip = input("Enter IP To Ping: ")
    print(f"Entered. Verifying IP {ip}.")
    time.sleep(0.86)
    print(f"{ip} Verifyed. Brute-Force Accessing {ip}")
    time.sleep(1.2)
    print(f"Scanning {ip} For Open Ports.")
    delay = 30
    scan_ports(ip, delay)
    time.sleep(30)
    print("Finished Scanning For Open Ports.")
    time.sleep(0.1)
    print(f"$ init connection @Server {ip}")
    time.sleep(0.56)
    print(f"Establishing A Secure Connection To {ip} Through Open Port.")
    time.sleep(2.43)
    print(f"Connected To {ip} Successfully!")
    time.sleep(1.23)
    print("Connecting To Man-In-The-Middle Network...")
    time.sleep(2.46)
    print("Securing LOnion Network...")
    time.sleep(3.72)
    print("LOnion Network Connected!")
    time.sleep(0.76)
    print("Connecting Via LOnion VPN")
    percentage()
    time.sleep(11.58)
    print("Done! Connecting The Following Attacks Via The IP Address: ")
    print("Port Injection")
    print("IP Fragmenting")
    print("DDoS")
    print("MiTM")

if __name__ == '__main__':
    main()
