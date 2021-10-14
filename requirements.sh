dependencies() {

	clear
	printf "\e[1;97mInstalling dependencies\e[0m\n"
	printf "\n\e[1;91mPIP3\e[0m\n"
	sudo apt install python3-pip
	printf "\n\e[1;91mFtplib\e[0m\n"
	pip install pyftpdlib
	printf "\n\e[1;91mParamiko\e[0m\n"
	pip install paramiko

}

dependencies