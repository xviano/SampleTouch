# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Connecting"
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
# Presses the Menu button	
print "Running"
#OK for SD Pieces
#MonkeyRunner.sleep(3)
print "Press"
device.touch(970, 830, MonkeyDevice.DOWN_AND_UP)