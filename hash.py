import hashlib
import time
from colorama import init
from termcolor import colored
import sys
import os
import webbrowser

hash = ""

init()

print(colored('''
███╗░░░███╗██████╗░███████╗  ██╗░░██╗░█████╗░░██████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝  ██║░░██║██╔══██╗██╔════╝██║░░██║
██╔████╔██║██║░░██║██████╗░  ███████║███████║╚█████╗░███████║
██║╚██╔╝██║██║░░██║╚════██╗  ██╔══██║██╔══██║░╚═══██╗██╔══██║
██║░╚═╝░██║██████╔╝██████╔╝  ██║░░██║██║░░██║██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
=========================================================================
|Telegram:https://t.me/VENOM_ITx                                        | 
|YouTube:VENOM IT ✪                                                     |
=========================================================================
''', 'green', 'on_red'))
webbrowser.open("https://www.youtube.com/channel/UChgCgpoarzvdEEeitoa_cZw")
hash =input("Type a name to create your word series: ")
time.sleep(3.0)
print(">>>>>>>>>>")
time.sleep(1.0)
print(">>>>>>>>>")
time.sleep(1.0)
print(">>>>>>>")
time.sleep(1.0)
print(">>>>>>")
time.sleep(1.0)
print(">>>>>>>>")
time.sleep(1.0)
print(">>>>>>>>>>")
time.sleep(1.0)
print(">>>>>>>")
time.sleep(1.0)
print(">>>>>>>>>")
time.sleep(1.0)
print(">>>>>>>>>>")
time.sleep(1.0)
result = hashlib.md5(hash.encode())
print("The work was done: ",end="")
print(result.hexdigest())


