import sys
import time
import os
import subprocess

selected_ip_file = open(ip_file, 'r')
selected_ip_file.seek(0)
ip_list = selected_ip_file.readlines()
selected_ip_file.close()    
check2 = False
           
while True:
     for ip in ip_list:
         ping_reply = subprocess.call(['ping', '-c', '2', '-w', '2', '-q', '-n', ip])
                    
         if ping_reply == 0:
             check2 = True
             continue
                    
         elif ping_reply == 2:
             print "\n* No response from device %s." % ip
             check2 = False
             break
                    
         else:
             print "\n* Ping to the following device has FAILED:", ip
             check2 = False
             break
               

            
