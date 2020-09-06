# closedports

Simple Python3 script which will parse nmap xml output for closed ports, with option to output result to csv file

https://nmap.org/book/man-port-scanning-basics.html

closed
A closed port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it. They can be helpful in showing that a host is up on an IP address (host discovery, or ping scanning), and as part of OS detection. Because closed ports are reachable, it may be worth scanning later in case some open up. Administrators may want to consider blocking such ports with a firewall. Then they would appear in the filtered state, discussed next.
