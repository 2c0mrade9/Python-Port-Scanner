# scripting-files
Most often as a pentester you will want to check the ports of a particular web address to find out if its really open

To make life really simple, this python script has been written with the simple Python Programming Techniques to aid users in this direction.

In using the file obvious you will have to download it first and then move it to a directory where you want to run it from.

Change direction to that directory and open a cmd on windows or terminal on linux systems.

usage: python port_scanner.py [options]
example: python port_scanner.py http://mywebsite.com

[options] - this is the name of the website address that you want to check.

[webaddress standard] - http://mywebsite.com

That is the accepted standard for the webaddress.

After all has been done, sit back and relax and the system checks the porst as listed in the listing_ports array.

If you want to scan more ports, feel free and edit the listing_ports array line to add more.

#set the timeout else there will be delays
sock.settimeout(10)

You can also change this to increase or decrease the waiting time in checking out on a port.

Thank you.
