#FOR CLEARING HOH B1
#Orientation : Landscape, Right as Top

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Establishing connection to device..."
# Connects to the current device, returning a MonkeyDevice object

timeout = 10
#device = "cf9fe6a7"
device = "127.0.0.1:62001"
device = MonkeyRunner.waitForConnection(timeout, device)
print "Connection established, initializing..."

count = 0
print "Start!"

while (count < 25):
	count += 1

	# Presses the fight button	
	MonkeyRunner.sleep(3)
	device.touch(1645, 775, MonkeyDevice.DOWN_AND_UP)

	#sleep time for auto-fight to be done
	MonkeyRunner.sleep(180)
	
	#get clear victory, TOUCH SCREEN ONCE TO SHOW CHEST
	#print "Victory..."
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	
	# 2ND TOUCH TO OPEN CHEST / replay
	MonkeyRunner.sleep(3)
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	
	#OK for SD Pieces
	MonkeyRunner.sleep(3)
	device.touch(970, 830, MonkeyDevice.DOWN_AND_UP)

	#last replay
	MonkeyRunner.sleep(3)
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	print "Looped %d times..." % count

print "Completed... \(^~^)/"

# Takes a screenshot
#result = device.takeSnapshot()

# Writes the screenshot to a file
#result.writeToFile('C:\Users\user\Desktop\screen4.png','png')