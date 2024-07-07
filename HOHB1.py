#FOR CLEARING HOH B1
#Orientation : Landscape, Right as Top

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Establishing connection to device..."
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
print "Connection established, initializing..."

count = 0

while (count < 30):
	count += 1

	# Presses the fight button	
	MonkeyRunner.sleep(3)
	device.touch(1645, 775, MonkeyDevice.DOWN_AND_UP)
	print "Start!"
	
	#sleep time for auto-fight to be done
	MonkeyRunner.sleep(280)
	
	#get clear victory, TOUCH SCREEN ONCE TO ACTIVATE replay / SHOW CHEST
	print "Victory..."
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	
	# 2ND TOUCH TO OPEN CHEST / replay
	MonkeyRunner.sleep(3)
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	
	#got chest, 3RD TO CLEAR REWARD.
	MonkeyRunner.sleep(3)
	device.touch(960, 825, MonkeyDevice.DOWN_AND_UP)

	#last replay
	MonkeyRunner.sleep(3)
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	print "Looped %d times..." % count

print "Completed... \(^~^)/"

# Takes a screenshot
#result = device.takeSnapshot()

# Writes the screenshot to a file
#result.writeToFile('C:\Users\user\Desktop\screen4.png','png')