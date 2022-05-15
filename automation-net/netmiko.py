import netmiko

connection= netmiko.ConnectHandler(ip="192.168.73.131", device_type="cisco_ios", username="cisco", password="cisco")

print(connection.send_command("sh ip int br"))
connection.disconnect()