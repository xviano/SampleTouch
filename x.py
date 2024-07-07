# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
print "Establishing connection to device..."

# Connects to the current device, returning a MonkeyDevice object
#timeout = 10
#name = "192.168.56.100:5555"
device = MonkeyRunner.waitForConnection()
#device = MonkeyRunner.waitForConnection(timeout, "cf9fe6a7")
print "Connection established, initializing..."

# Starts Stage X-3
device.touch(455, 1525, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(3)

# Starts Stage X-6
#device.touch(455, 725, MonkeyDevice.DOWN_AND_UP)
#MonkeyRunner.sleep(3)

# Stage Start
MonkeyRunner.sleep(3)
device.touch(880, 1820, MonkeyDevice.DOWN_AND_UP)

count = 0

# loops number of times
while (count < 311):
	count += 1
	
	MonkeyRunner.sleep(94)
	# Gets Monsters
	device.touch(550, 1775, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)

	# Repeat Button
	device.touch(550, 1325, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)
	print "Looped %d times..." % count

print "Completed %d times... \(^~^)/" % count
