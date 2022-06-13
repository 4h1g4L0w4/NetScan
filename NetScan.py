from scapy.all import *
import sys
import socket

print("""
  _  _             _       ___                           
 | \| |    ___    | |_    / __|    __     __ _    _ _    
 | .` |   / -_)   |  _|   \__ \   / _|   / _` |  | ' \   
 |_|\_|   \___|   _\__|   |___/   \__|_  \__,_|  |_||_|  
	""")


menu_options = {

    1: 'Network IP Scanner',
    2: 'Port Scanner',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
	print("Simple Netowrk Scanner by 4h1g4L0w4")
	network_interface = input("Set Network Interface: ")
	ip_range = input("Set IP Range (example: 192.168.1.1/24): ")
	broadcast_mac = "ff:ff:ff:ff:ff:ff"
	packet = Ether(dst=broadcast_mac)/ARP(pdst = ip_range)
	ans, unans = srp(packet, timeout=5, iface=network_interface, inter=0.1)
	for send,receive in ans:
		print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

def option2():
	print("Port Scanner by 4h1g4L0w4")
	ip = input("Set IP: ")
	open_ports =[]
	a = int(input("Set Port Range (example: 1, 65535)"))
	ports = range(a)
	def probe_port(ip, port, result = 1):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.6)
			r = sock.connect_ex((ip, port))
			if r == 0:
				result = r
			sock.close()
		except Exception as e:
			print("Something went wrong")
			pass
		return result

	for port in ports:
		sys.stdout.flush()
		response = probe_port(ip, port)
		if response == 0:
			open_ports.append(port)

		if open_ports:
			print("Open Ports are: ")
			print(sorted(open_ports))
		else:
			print("no open ports")


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            print('See You Soon')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
