echo $(arp-scan --interface=eth0 --localnet  |grep  50:c7:bf:30| cut -f 2,4 -d " " | sed -e 's/[;,()'\''Unknown,D,S,P]/ /g;s/  */ /g')> /home/pi/Desktop/DataGather/kuru/device_list.txt
cat /home/pi/Desktop/DataGather/kuru/device_list.txt





