import os

def gettemp(id):
    """function fetching data from sensor""" 
    os.chdir('/sys/bus/w1/devices/'+id)
    try:
        data = open('w1_slave')
        temp = data.read()
        index = temp.find('t=')
        temp_read = temp[index+2:-1]
        tmp_read = round(float(temp[67+2:-1])/1000, 1)
        data.close()
	return tmp_read
    
    except:
        temp_read = 9999
        data.close()
        print temp_read

