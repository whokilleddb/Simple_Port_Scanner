#!/usr/bin/python3

import socket
import os
import time
import sys
#import waiting


ip = 1
port = 1
start_port = 1
end_port = 1
response1 = 1

"""
	I have took this for enabling the use of global Variables.
	Above variables do not have any resemblance/meaning related to the concept or building this port scanner!!!
"""

print("\r\n")

os.system("figlet By  Reveng ... | lolcat -a -p -d 4 -s 50")

time.sleep(2)

os.system("clear")

print("\r\n" + "<"+ "-"*50 +">")
os.system("figlet Simple Port Scanner | lolcat")
print("\r\n" + "<"+ "-"*50 + ">")
print("\r\n" + "Welcome,this is a simple python3 port scanner tool by ---> Reveng " + "\r\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def defining_ip_port():

	global ip
	global port
	global start_port
	global end_port
	global response1

	ip = input("Enter ip: ")

	# input validation -> for IP excludes only space from string
	ip = ip.strip()
	
	no_of_port = input("[response1] Enter 1 port or range of ports ?? [1/range] : " + "\r\n" + "Choose Option: ")

	response1 = no_of_port

	print("[+] Your selected Option: ", no_of_port )

	if(response1 == '1'):
		port = input("Enter port no.: ")

		# input validation -> for PORT excludes only space from string
		port = port.strip()

		# input validation -> for PORT throws error message when port inputed have datatype of string, which can't be converted to integer
		try:
			port = int(port)
			"""
				previously it was taken as string for validating input.
				Now it is converted to string
			"""
		except ValueError:
			print("[-] Error!!!, Unable to find that port :(")
			print("[-] Your port number should be within 0-65,535 and should not be string")
			print("\nPlease Try again: " + "\r\n")
			defining_ip_port()

	if(no_of_port == 'range'):
		start_port = input("Enter starting port no.: ")
		end_port = input("Enter ending port no.: ")

		# input validation -> for PORT excludes only space from string
		start_port = start_port.strip()
		end_port = end_port.strip()

		# input validation -> for PORT throws error message when port inputed have datatype of string, which can't be converted to integer
		try:
			start_port = int(start_port)
			end_port = int(end_port)

			"""
				previously it was taken as string for validating input.
				Now it is converted to string
			"""
		except ValueError:
			print("[-] Error!!!, Unable to find that port :(")
			print("[-] Your port number should be within 0-65,535 and should not be string")
			print("\nPlease Try again: " + "\r\n")
			defining_ip_port()


		

defining_ip_port()

#input validation -> for PORT : Throws error message if port number gets exceeded from number 65,535
if (port >= 65535) or (port == '') or (start_port >= 65535) or (start_port == '') or (end_port >= 65535) or (end_port == ''):
	print("[-] Error!!!, Unable to find that port :(")
	print("[-] Your port number should be within 0-65,535 and should not be string")
	print("\nPlease Try again: " + "\r\n")
	defining_ip_port()

"""

input validation for ip is needed

"""


response2 = input("""[response2] Enter the mode of operation:

1. PortScanner
2. BannerGrabbing\n""" + "\r\n" + "Choose Option: ")

print("[+] Your selected Option: " , response2)


# PORT SCANNER OPTIONS:

# For Single port mode as well as Port Scanner mode:
if(response1 == '1') and (response2 == '1'):
	
	response3 = input("""[response3] Enter type of Port Scanner you intend to use: 

1. Scan_with_ping_single_port
2. Scan_with_TCP_single_port\n""" + "\r\n" + "Choose options: ")


	print("[+] Your selected Option: ", response3 )

	# For Single port mode as well as Port Scanner ping mode to perform host discovery and port status :
	def Scan_with_ping_single_port():

		print("[-] Sorry!!! NUll, Still need to be upgraded")
		pass
		sock.settimeout(10) # unit = sec


	# For Single port mode as well as Port Scanner TCP mode to know only port status, it doesn't perform host discovery :
	def Scan_with_TCP_single_port():
		
		#Though in TCP scan mode ping method is used to check whether host is up or not
		response_for_ping = os.system("ping -c 1 " + ip)

		start_time = time.time()

		sock.settimeout(5)

		if (response_for_ping == 0):
			print("\r\n" +"[+] Destination Host is Up!!")

			
			if sock.connect_ex((ip,port)):

				# Upto this point, it is running and then hanging up when port is filtered , after sometime it shows port is closed 
				"""
					But I want it to wait for 5 seconds for the reply ans then raise an appropiate message
				"""

				print("[-] But!!, Port", port,"is Closed :( ")
			else:
				print("[+] Port", port,"is Open :) ")
		else:
			print("[-] Destination Host is Down !! ")

		end_time = time.time()
		print('\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")

		print("\r\n")

		# asking if user need to scan port again or not
		again = input("Do you want to scan port again ?? [yes/no] : ")
		if(again == 'yes'):
			print("\r\n")
			defining_ip_port()
		else:
			print("\r\n¡¡Okay!! adiós, nos vemos...")
			sys.exit()


	if(response1 == '1') and (response2 == '1') and (response3 == '1'):
		Scan_with_ping_single_port()

	if (response1 == '1') and (response2 == '1') and (response3 == '2'):
		Scan_with_TCP_single_port()



# For multiple port mode and Port Scanner mode:
if(response1 == 'range') and (response2 == '1'):
	
	response3 = input("""[response3] Enter type of Port Scanner you intend to use: 

1. Scan_with_ping_multiple_ports
2. Scan_with_TCP_multi_ports\n""" + "\r\n" + "Choose options: ")

	print("[+] Your selected Option: ", response3 )

	# For Multiple port mode as well as Port Scanner ping mode to perform host discovery and port status :
	def Scan_with_ping_multiple_ports():
		print("[-] Sorry!!! NUll, Still need to be upgraded")
		pass
		sock.settimeout(10) # unit = sec


	# For Multiple port mode as well as Port Scanner TCP mode to know only the OPEN ports NOT the CLOSED/FILTERED one, it perform host discovery :
	def Scan_with_TCP_multiple_ports():
		
		#Though in TCP scan mode ping method is used to check whether host is up or not
		response_for_ping = os.system("ping -c 1 " + ip)

		start_time = time.time()
		
		if (response_for_ping == 0):
			print("\r\n" +"[+] Destination Host is Up!!" + "\r\n")
		

			for port in range(start_port, end_port+1):

				print("Scanning port: ", port)

				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(5)

				conn = sock.connect_ex((ip, port))

				if(not conn):
					print("[+] Port {} <-------------------- OPEN Port".format(port))
				else:
					print("Present Port is closed or filtered !?")
				sock.close()
				
		else:
			print("[-] Destination Host is Down !! ")

		end_time = time.time()
		print('\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")

		print("\r\n")

		# asking if user need to scan port again or not
		again = input("Do you want to scan port again ?? [yes/no] : ")
		if(again == 'yes'):
			print("\r\n")
			defining_ip_port()
		else:
			print("\r\n¡¡Okay!! adiós, nos vemos...")
			sys.exit()

	if(response1 == 'range') and (response2 == '1') and (response3 == '1'):
		Scan_with_ping_multiple_ports()

	if (response1 == 'range') and (response2 == '1') and (response3 == '2'):
		Scan_with_TCP_multiple_ports()



# BANNER GRABBING OPTIONS:

# Disclaimer --> These Banner Grabbing sections are checked only with ports : 20 to 25 . It need upgradation. Unable to banner grab on port 23 telnet

# Via netcat also, I was unable to grab banner from port 23 telnet

# For single port mode and Banner Grabbing mode, it will  perform host discovery:
if(response1 == '1') and (response2 == '2'):
	
	def banner_grab_single_port():
		
		#ping method is used to check whether host is up or not
		response_for_ping = os.system("ping -c 1 " + ip)

		#In case Host is Down
		start_time = time.time()

		if (response_for_ping == 0):
			
			print("\r\n" +"[+] Destination Host is Up!!")

			start_time = time.time()

			print(port)

			try:
				
				sock.connect((ip,port))

				if(port == 23):
					
					os.system('telnet {0} {1}'.format(ip,port))

					end_time = time.time()
					print('\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")

				else:
					
					print("[+] Service running: ", str(sock.recv(1024)).strip('b'))

					end_time = time.time()
					print('\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")
			
			except ConnectionRefusedError:

				print("[-] Connection Refused as port {} is closed :(".format(port))

				end_time = time.time()
				print("\nTime taken by Simple Port Scanner to scan:", end_time - start_time,"sec")

			except OSError:

				print("[-] Unable to Grab Banner, Banner Grabbing is prohibited or simply can't be done on this port  !! ")

				end_time = time.time()
				print("\nTime taken by Simple Port Scanner to scan:", end_time - start_time,"sec")

		else:

			print("[-] Destination Host is Down !! ")
			
			end_time = time.time()
			print("\nTime taken by Simple Port Scanner to scan:", end_time - start_time,"sec")
			

	banner_grab_single_port()

	print("\r\n")

	# asking if user need to scan port again or not
	again = input("Do you want to scan port again ?? [yes/no] : ")
	if(again == 'yes'):
		print("\r\n")
		defining_ip_port()
	else:
		print("\r\n¡¡Okay!! adiós, nos vemos...")
		sys.exit()


# For Multiple port mode and Banner Grabbing mode, it will perform host discovery:
if(response1 == 'range') and (response2 == '2'):
	
	def banner_grab_multiple_ports():

		#ping method is used to check whether host is up or not
		response_for_ping = os.system("ping -c 1 " + ip)

		#In case Host is Down
		start_time = time.time()

		if (response_for_ping == 0):
			
			print("\r\n" +"[+] Destination Host is Up!!")

	
			for port in range(start_port, end_port+1):

				print("\r\n" + "[+] Grabbing Banner of : ", port, "\r\n")

				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				
				start_time = time.time()

				sock.settimeout(5)

		
				#try:
				#sock.connect((ip,port))

				if(port == 23):

					os.system('telnet {0} {1}'.format(ip,port))

					end_time = time.time()
					print('\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")

				else:

					try:

						sock.connect((ip,port))

						print("[+] Service running on port{} : -------> Got It!! ".format(port) , str(sock.recv(1024)).strip('b'))

						end_time = time.time()
						print('\r\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")

					
					# This line actually helped to distinguise between filtered and prohibited ports for banner grabbing  but it has some bugs that's why commented this.....
					
					# 1stly, Among all originally filtered ports, some are shown here as filtered but some are not, for eg. : port 22 is originally filtered but this code shows it as port which has 
					# been prohibited to perform banner grabbing.
					
					# 2ndly, smtp port 25 which is originally open is treated as port which has been prohibited to perform banner grabbing.

					#except socket.timeout:

					#	print("[-] Unable to Grab Banner, as the port is filtered !!")

					#	end_time = time.time()
					#	print("\nTime taken by Simple Port Scanner to scan:", end_time - start_time,"sec")
			
								
					except OSError:

						print("[-] Unable to Grab Banner,Banner Grabbing is prohibited or simply can't be done on this port  !! ")

						end_time = time.time()
						print("\nTime taken by Simple Port Scanner to scan:", end_time - start_time,"sec")

										
					except ConnectionRefusedError:

						print("[-] Connection Refused as port {} is closed :( ".format(port))

						end_time = time.time()
						print("\nTime taken by Simple Port Scanner to scan:", end_time - start_time,"sec")
					
					continue

		else:

			print("[-] Destination Host is Down !! ")

			end_time = time.time()
			print('\nTime taken by Simple Port Scanner to scan:', end_time - start_time,"sec")

		print("\r\n")


	banner_grab_multiple_ports()	
		
		
	print("\r\n")

	# asking if user need to scan port again or not
	again = input("Do you want to scan port again ?? [yes/no] : ")
	if(again == 'yes'):
		print("\r\n")
		defining_ip_port()
	else:
		print("\r\n¡¡Okay!! adiós, nos vemos...")
		sys.exit()
