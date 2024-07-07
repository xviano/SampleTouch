# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
#timeout = 10
#name = "192.168.56.101:5555"


timeout = 10
device = "127.0.0.1:62001"
device = MonkeyRunner.waitForConnection(timeout, device)
#device = MonkeyRunner.waitForConnection()

# Takes a screenshot
result = device.takeSnapshot()

# Writes the screenshot to a file
result.writeToFile('C:\Users\user\Desktop\photo.png','png')