import os
import re
import time
import os
import subprocess

url = 'http://192.168.1.18:5000'

def watchdog(url):
    cmd = os.system('wget -t 1 -T 5 --delete-after ' + url)
    #print "cmd result: %d" % cmd
    #print "url:" , url
    if cmd != 0:
        pidlist = subprocess.check_output(['pidof','python','remote_control.py'])
	#print "pidlist:" , pidlist.rsplit()
	#print "os.getpid():" , os.getpid()
        for pid in range(len(pidlist.rsplit())):
            #print "pidlist.rsplit()[pid]:%s" % pidlist.rsplit()[pid]
	    #print "pid:%s" % str(pid)
            if int(pidlist.rsplit()[pid]) == os.getpid():
	        #print "os.getpid()%s:" % os.getpid()
		continue
	    else:
	        subprocess.call(['sudo','kill',pidlist.rsplit()[pid]])
	        time.sleep(2)
	subprocess.Popen(['nohup','sudo','python','remote_control.py','&'])
	            
        time.sleep(3)
	
if __name__ == "__main__":
    watchdog(url)
    
