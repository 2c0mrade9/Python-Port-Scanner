#!/usr/bin/env python
import socket
import time, sys
from datetime import datetime
from tld import get_tld

#assign variables
host = ''
min_port = 20
max_port = 30

# This dictionary contains the most popular ports used
# You can add ports here. 
# The key is the port number and the values is the service used by that port
common_ports = {

	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'389': 'LDAP',
	'443': 'HTTPS',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'2082': 'CPANEL',
	'2083': 'CPANEL',
	'3306': 'MYSQL',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}

listing_ports = [21, 22, 23, 25, 53, 69, 80, 109, 110, 143, 156, 156, 443, 546, 547, 995, 993, 2086, 2087, 3306, 8443, 10000]

#function to print out the usage
def printUsage():
    # print out how to use the programe
    print ("""
          Usage:
             python filename topleveldomainname
             eg.
               python port_scanner.py google.com
         """)

#initial information to display to the user
def initializing():
    #print out some information
    print("[*] PORT SCANNING SCRIPT BY EMMALLEN NETWORKS")
    print("[*] For educational purposes only [*]")
    print("*" * 70)

#call the the very first function
initializing()

#check if the user submitted an argument in the command line
if len(sys.argv) == 2:
    host = sys.argv[1]
else:
    #request the user to enter domain name
    host = input("[*] Enter a Remote Host to scan: ")

#get the top level domain name
try:
    host = get_tld(host)
except:
    #print out error message
    print("Sorry! You entered an invalid Remote Host Address [Please enter only the top level domain name]")
    #call the usage function
    printUsage()
    #exit the application
    sys.exit(1)
    
#get the real ip address of the domain name entered by the user
try:
    ipaddress  = socket.gethostbyname(host)
except:
    #print out error message
    print("Sorry! You entered an invalid Remote Host Address [Please enter only the top level domain name]")
    #call the usage function
    printUsage()
    #exit the application
    sys.exit(1)
    
#get the starting time
t1 = time.time()

# Print a nice banner with information on which host we are about to scan
print("[*]", "-" * 60, "[*]")
print("[*] Remote Host: %s IP Address: %s" % (host, ipaddress))
print("[*] Scanning started at %s TIME: %s" % (host, time.strftime("%I:%M:%S %p")))
print("[*]", "-" * 60, "[*]\n")

#function to fetch the name of a port
def port_opened(port):
    # converts the int to string
    port = str(port)
    # check if the port is available in the common ports dictionary
    if port in common_ports:
        # returns the service name if available
        print("[*]", port, ' '*10, common_ports[port], ' '*10, 'Opened', ' '*10)

#function to fetch the name of a port
def port_closed(port):
    # converts the int to string
    port = str(port)
    # check if the port is available in the common ports dictionary
    if port in common_ports:
        # returns the service name if available
        print("[*]", port, ' '*10, common_ports[port], ' '*10, 'Closed', ' '*10)

#using the range function to specify ports to scan
#we also put in some error handling for catching errors
try:

    print("[*] PORT ", ' '*6, " SERVICE", ' '*7, " STATUS ", ' '*5, " VERSION ", ' '*7)
    for port in listing_ports:
        #port : port to scan
        #ipaddress : the ipaddress of the domain name
        #create the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
	#set the timeout else there will be delays
        sock.settimeout(10)
        
	#fetch the connection results
        result = sock.connect_ex((ipaddress, port))
        if result == 0:
            #call the port name function
            port_opened(port)
        else:
            port_closed(port)
        sock.close()
		
except KeyboardInterrupt:
    print("[*] You interrupted the process")
    sys.exit(1)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit(1)
except socket.error:
    print("Couldn't connect to the server")
    sys.exit(1)


#get the time that the system finished checking the ports
t2 = time.time()

#difference
time_spent = t2 - t1

#print out the final information
print("\n[*] Scanning completed at: ", time.strftime("%I:%M:%S %p"))
#time spent calcultion
if time_spent <= 60:
    time_spent = str(round(time_spent, 2))
    print("[*] Scanning Duration: ", time_spent, " seconds")
else:
    time_spent = round((time_spent / 60), 2)
    print("[*] Scanning Duration: ", time_spent, " minutes")

print("*" * 70)
print("""This program is intended for individuals to test their own equipment for weak
security, and the author will take no responsibility if it is put to any other use""")
print("[*] Enjoy your day and have fun!")
print("*" * 70)
