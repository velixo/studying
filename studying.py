import time
import winsound


def timeStr():
	return time.strftime("%H:%M:%S")


def writeToLog(p, t, c):
	logfile = open('studylog.txt', 'a')
	logfile.write(p + ' ' + t + ' ' + c + '\n')
	logfile.close()

pluggtid = 20 * 60
paustid = 5 * 60
start = timeStr()
print(start + " börja plugga! " + str(pluggtid / 60) + " min")
writeToLog('[s]', start, '')
while True:
	# start studying
	winsound.Beep(600, 550)
	time.sleep(pluggtid)
	winsound.Beep(400, 1000)
	comment = input("i de senaste " + str(pluggtid / 60) + " min har jag: ")
	writeToLog('[c]', timeStr(), comment)

	# take break
	print("paus i " + str(paustid / 60) + " min")
	time.sleep(paustid)
	winsound.Beep(500, 550)
	input("börja plugga?")
