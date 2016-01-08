import time
import winsound
import sys

studyTime = 20 * 60
pauseTime = 5 * 60


def timeStr():
	return time.strftime("%H:%M:%S")


def writeToLog(p, t, c):
	logfile = open('studylog.txt', 'a')
	logfile.write(p + ' ' + t + ' ' + c + '\n')
	logfile.close()


def pause():
	print("paus! " + str(pauseTime / 60) + " min")
	writeToLog('[f]', timeStr(), 'pause started')
	time.sleep(pauseTime)
	winsound.Beep(500, 550)
	input("återgå till plugget?")
	writeToLog('[t]', timeStr(), 'pause ended')

studying = False


def main():
	global studying
	intialPause = False

	if len(sys.argv) > 1:
		option = sys.argv[1]

		if option == '-p':
			intialPause = True
		elif option == '-h' or '--help':
			print("Implement: write help statement.")
			return

	writeToLog('[s]', timeStr(), 'session started')
	if intialPause:
		pause()
	while True:
		# start studying
		print(timeStr() + " plugga! " + str(studyTime / 60) + " min")
		writeToLog('[d]', timeStr(), 'studying started')
		studying = True
		winsound.Beep(600, 550)
		time.sleep(studyTime)
		winsound.Beep(400, 1000)
		comment = input("i de senaste " + str(studyTime / 60) + " min har jag: ")
		writeToLog('[r]', timeStr(), comment)
		studying = False

		# take break
		pause()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		comment = ''
		if studying:
			comment = input("plugg avslutas i förtid, vad har gjorts hittils?: ")
			writeToLog('[r]', timeStr(), comment)
		print("plugg avslutat!")
		writeToLog('[e]', timeStr(), 'session ended')
		sys.exit()
