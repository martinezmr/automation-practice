# model - component that stores the data
# view - component that displays the data
# controller - handles logic glow, user interactions, and directs models and views

#stores the data below
class Device:

    ipAddress = ""
    port = ""

    #static method not required (hard coding them in for this example)
    @staticmethod
    def findDevices():
        devices = []

        d = Device()
        d.ipAddress = "192.168.1.1"
        d.port = "2001"

        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.1.50"
        d.port = "7091"

        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.1.100"
        d.port = "80"

        devices.append(d)

        return devices

#Displays the data
class DevicesView:

    def showDevices(self,devices):
        for d in devices:
            print("-------")
            print("IP Address: " + d.ipAddress)
            print("Port: " + str(d.port))
            print("-------")

#Does the magic using the stored data to display it 
class DevicesController:

    def __init__(self):
        devices = Device.findDevices()

        v = DevicesView()
        v.showDevices(devices)

c = DevicesController()