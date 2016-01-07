import time
import winsound
import sys


def timeStr():
	return time.strftime("%H:%M:%S")


def writeToLog(p, t, c):
	logfile = open('studylog.txt', 'a')
	logfile.write(p + ' ' + t + ' ' + c + '\n')
	logfile.close()


def main():
	pluggtid = 20 * 60
	paustid = 5 * 60
	writeToLog('[s]', timeStr(), 'session started')
	while True:
		# start studying
		print(timeStr() + " plugga! " + str(pluggtid / 60) + " min")
		writeToLog('[d]', timeStr(), 'studying started')
		winsound.Beep(600, 550)
		time.sleep(pluggtid)
		winsound.Beep(400, 1000)
		comment = input("i de senaste " + str(pluggtid / 60) + " min har jag: ")
		writeToLog('[r]', timeStr(), comment)

		# take break
		print("paus! " + str(paustid / 60) + " min")
		writeToLog('[f]', timeStr(), 'pause started')
		time.sleep(paustid)
		winsound.Beep(500, 550)
		input("återgå till plugget?")
		writeToLog('[t]', timeStr(), 'pause ended')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("plugg avslutat!")
		writeToLog('[e]', timeStr(), 'session ended')
		sys.exit()
