import hashlib
import time
hash = ""
print('''
███╗░░░███╗██████╗░███████╗  ██╗░░██╗░█████╗░░██████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝  ██║░░██║██╔══██╗██╔════╝██║░░██║
██╔████╔██║██║░░██║██████╗░  ███████║███████║╚█████╗░███████║
██║╚██╔╝██║██║░░██║╚════██╗  ██╔══██║██╔══██║░╚═══██╗██╔══██║
██║░╚═╝░██║██████╔╝██████╔╝  ██║░░██║██║░░██║██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
code by VENOM IT''')
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


