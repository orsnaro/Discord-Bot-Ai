import re
from subprocess import Popen, PIPE

async def ping (host,ping_count):

		ip = host
		data = ""
		avg_ping = 10000000000 
		output = Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

		for line in output.stdout:
			start_indx = line.find("Average =")
   
			if start_indx != -1 :
				print(start_indx)
				ping_line = line[start_indx + 9 : ].strip()
				avg_ping =  int(ping_line[: -2])
				print("TESTING" , avg_ping)
				
			data = data + line
			ping_test = re.findall("TTL", data)
   
   
		if ping_test:
			return avg_ping
		else:
			return False

nodes = ["8.8.8.8", "20.20.20.50", "facebook.com", "192.168.1.20"]
