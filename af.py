import os
import time

os.system("clear")

print("Android ADB and FASTBOOT Installer")
print("script by freetheorange905 0.1")
print("")
print("[1]Insatll ADB and FASTBOOT")
print("[2]Uninstall ADB and FASTBOOT")
print("")
choice = input("Choice:")
if choice == "1":
	os.system("apt update > /dev/null 2>&1 && apt --assume-yes install wget > /dev/null 2>&1 && wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh -q && bash InstallTools.sh")
elif choice == "2":
	os.system("apt update > /dev/null 2>&1 && apt --assume-yes install wget > /dev/null 2>&1 && wget https://github.com/MasterDevX/Termux-ADB/raw/master/RemoveTools.sh -q && bash RemoveTools.sh")

