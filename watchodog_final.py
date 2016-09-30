import os
import re
import time
import os
import subprocess

url = 'http://192.168.1.18:5000'

def watchdog(url):
    """function verifing proper work of script named as remote_control.py"""
    cmd = os.system('wget -t 1 -T 5 --delete-after ' + url)
    if cmd != 0:
        pidlist = subprocess.check_output(['pidof','python','remote_control.py'])
	for pid in range(len(pidlist.rsplit())):
            if int(pidlist.rsplit()[pid]) == os.getpid():
	        continue
	    else:
	        subprocess.call(['sudo','kill',pidlist.rsplit()[pid]])
	        time.sleep(2)
	subprocess.Popen(['nohup','sudo','python','remote_control.py','&'])
	            
        time.sleep(3)
	
if __name__ == "__main__":
    watchdog(url)
    
