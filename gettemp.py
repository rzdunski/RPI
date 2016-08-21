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
        temp_read = 999
        data.close()
        print temp_read

#print "Temperatura zew:",tmp_read(id_outside),u'\xb0'+'C'
#print "Temperatura wew:",tmp_read(id_inside),u'\xb0'+'C'

#below some old test for using this function
"""
index = 2
while index!=0:
    id_inside = '28-000001cbe681'
    id_outside = '10-000800ba9da0'
    print "TMP OUT:", gettemp(id_outside)
    print "TMP IN:", gettemp(id_inside)
    index -= 1
"""
