import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
website_list = [
'www.facebook.com',
'facebook.com',
'www.omeducation.edu.in',
'omeducation.edu.in',
]



while True:
	if dt(dt.now().year, dt.now().month, dt.now().day,11) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,12):
		print("Working Hours")

		# open the hosts file and add the content

		with open(hosts_path, 'r+') as file:
			content = file.read()
			# Check The Website List
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")

	else:
		# Open File To delete those line

		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			# Delete the repeate the content
			file.truncate()		
		print("Fun Time")


	time.sleep(5)