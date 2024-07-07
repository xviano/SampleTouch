#FOR CLEARING HOH B1
#Orientation : Landscape, Right as Top

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Establishing connection to device..."
# Connects to the current device, returning a MonkeyDevice object

timeout = 10
device = MonkeyRunner.waitForConnection(timeout,"cf9fe6a7")
#device = MonkeyRunner.waitForConnection(timeout,"192.168.1.6:5555")
#device = MonkeyRunner.waitForConnection(timeout)
print "Connection established, initializing..."

count = 0

print "Start!"
	
while (count < 30):
	count += 1

	# Presses the fight button	
	MonkeyRunner.sleep(3)
	device.touch(1645, 775, MonkeyDevice.DOWN_AND_UP)
	#sleep time for auto-fight to be done
	MonkeyRunner.sleep(100)
	
	#get clear victory, TOUCH SCREEN ONCE TO ACTIVATE replay / SHOW CHEST
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	
	#2ND TOUCH TO OPEN CHEST / replay
	MonkeyRunner.sleep(3)
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	
	#Got chest, Sell Rune.
	MonkeyRunner.sleep(3)
	device.touch(875, 820, MonkeyDevice.DOWN_AND_UP)

	#OK for Hellhound / Inugami / Salmander 
	MonkeyRunner.sleep(3)
	device.touch(850, 970, MonkeyDevice.DOWN_AND_UP)
	
	#Replay Button
	MonkeyRunner.sleep(3)
	device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
	print "Looped %d times..." % count

print "Completed... \(^~^)/"