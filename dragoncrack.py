#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from banner.banner import *


def menu():
	banner()

	print("""\n\033[1;37m[\033[0;31m1\033[1;37m]\033[0m FTP CRACK
\033[1;37m[\033[0;31m2\033[1;37m]\033[0m SSH CRACK
""")

menu()

option = int(input("\033[1;31m=>\033[0m "))

if option == 1:
	os.system("cd protocols && python3 ftp.py")
	

elif option == 2:
	os.system("cd protocols && python3 ssh.py")
    
	




	

			


