import netmiko
import csv
import datetime

nodenum = 1
f=open('C:/Users/mmart/automation-practice/automation-net/nodeips.csv', 'r')
c=f.readlines()
print(c)

with open('C:/Users/mmart/automation-practice/automation-net/nativevlans.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(['Hostname', 'IP Address', 'Trunks'])

    for i in c :
        print('Node', nodenum, '-Checking IP Address ', i)
        try:
            connection = netmiko.ConnectHandler(ip=i, device_type="cisco_ios", username="cisco", password="cisco")
        except:
            try:
                print("Cannot connect via SSH, trying Telnet")
                connection = netmiko.ConnectHandler(ip=i, device_type="cisco_ios_telnet", username="cisco", password="cisco")
                
            except:
                print('Cannot connect via SSH or Telnet, node may be down or not using standard credentials, logging to error.log')
                print('')
                now = str(datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S"))
                nodenum = nodenum +1
                logf = open('C:/Users/mmart/automation-practice/automation-net/error.log', 'a')
                logf.write(now)
                logf.write(' - Cannot connect via SSH or Telent to ')
                logf.write(i)
                logf.close()
                continue

        hostname = (connection.send_command("show run | include hostname"))
        trunk = (connection.send_command("show interface trunk"))
        connection.disconnect()

        print(hostname)
        print(trunk)

        write.writerow([hostname, i, trunk])
        print ("\n\n")
        nodenum = nodenum + 1
    f.close()

