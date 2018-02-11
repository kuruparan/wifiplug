
import paho.mqtt.client as mqtt
import os

def on_message(client, userdata,msg):
        chk=0;
        print(msg.topic+" "+str(msg.payload))
        deviceType,deviceID,action =str(msg.payload).split('_')
#        print deviceType + ' ' +deviceID + ' ' +action
        if deviceType=="Wifiplug":
                os.system('/home/pi/Desktop/DataGather/kuru/scandev.sh')
                with open("/home/pi/Desktop/DataGather/kuru/device_list.txt") as file:
                        line=file.readline()
                        #print line 
                        if (os.stat("/home/pi/Desktop/DataGather/kuru/device_list.txt").st_size)> 1:
                                ip = line.split(" ")
                                print ip

                                for i in ip:
                                        for k in range(1,len(ip)/2,1):
                                                ip.remove(ip[2*k-1])


                                ip.pop()
                                print ip
                                ipaddr=""
                                for n in range(1,len(ip)+1,1):

                                        if deviceID ==str(n):
                                                ipaddr=ip[n-1]
                                                print ipaddr,str(n)
                                                chk=1
                                                os.system('/home/pi/Desktop/DataGather/kuru/Wifiplug.sh ' + ipaddr + ' 9999 ' + action)
                                if chk==0:
                                        print("device id not registered")
                        else:
                                print ("no device  connected")

client=mqtt.Client()
client.username_pw_set(username="username",password="password")
client.connect("192.168.1.253")
#client.loop_start()
#os.system('./nmaping.sh')
client.subscribe("g1")
print "subscribing"
client.on_message=on_message
client.loop_forever()



