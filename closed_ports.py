#!/usr/bin/python

from bs4 import BeautifulSoup
import argparse

#Define list which we'll use to write to file
output = []

try:
	#Get file to parse from the command line
	parser = argparse.ArgumentParser()
	parser.add_argument("--xmlfile", help="nmap xml file you want to parse", type=str, required=True)
	#Add option to be able to output result to csv file
	parser.add_argument("--output", help="save output to csv file", type=str, default="", required=False)
	args = parser.parse_args()

	#Display banner
	print("\n[*] Nmap XML Scanner for Closed Ports")
	print("[*] Richard Davy, ECSC plc- 2020\n")

	#Read in file to parse
	with open(args.xmlfile, 'r') as f:
		contents = f.read()
		#Give it to Beautiful Soup
		soup = BeautifulSoup(contents, 'lxml')

	#If we're not outputing to file display results to screen
	if args.output=="":
		print("IP Protocol Port")
	
	#Add titles to our list
	output.append("IP,Protocol,Port")

	#Find all instances of host
	for td in soup.find_all('host'):
		#Iterate all instances of host
		for i in td :
			#Pass each instance of host to beautiful soup
			soup1 = BeautifulSoup(str(i),'lxml')
			#Get all instances of address
			add = soup1.find_all('address')
			for ad in add:
				#There should only be one instance of address, store the value in a variable
				#<address addr="10.37.66.5" addrtype="ipv4"/>
				address=ad.get('addr')

			#Find all instances of port
			#<port protocol="tcp" portid="22"><state state="closed" reason="syn-ack" reason_ttl="0"/><service name="ssh" method="table" conf="3"/></port>
			sp_port = soup1.find_all('port')
			for pt in sp_port:
				#If the word closed is found, print address, protocol and port number
				if "closed" in str(pt):
					#If we're not outputing to file display results to screen
					if args.output=="":
						print(address + " " + pt.get('protocol') + " " + pt.get('portid'))
					#Add results to our list
					output.append(address + "," + pt.get('protocol') + "," + pt.get('portid'))

	#See if we're outputting to file
	if args.output!="":
		try:
			#Open file handler
			with open(args.output,'w') as result_file:
				#Iterate our list
				for r in output:
					#Write line
					result_file.write(r + "\n")
				#Close file handle
				result_file.close()
				#Print msg to screen
				print("[*] Output has been written to "+ args.output)
		#Friendly Error Handler code
		except Exception as e:
			print("[!] Doh... Well that didn't work as expected!")
			print("[!] type error: " + str(e))
#Friendly Error Handler code
except Exception as e:
	print("[!] Doh... Well that didn't work as expected!")
	print("[!] type error: " + str(e))