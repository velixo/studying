import time
import pyaudio
import wave
import sys

studyTime = 20 * 60
# pauseTime = 5 * 60


def timeStr():
	return time.strftime("%H:%M:%S")


def writeToLog(p, t, c):
	logfile = open('studylog.txt', 'a')
	logfile.write(p + ' ' + t + ' ' + c + '\n')
	logfile.close()


def playSound(sound):
	wf = ''
	if sound == '600':
		wf = wave.open('res/600.wav', 'rb')
	elif sound == '500':
		wf = wave.open('res/500.wav', 'rb')
	elif sound == '400':
		wf = wave.open('res/400.wav', 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)
	data = wf.readframes(1024)
	while data != '':
		stream.write(data)
		data = wf.readframes(1024)
	stream.stop_stream()
	stream.close()
	p.terminate()


def parseInt(input):
	try:
		num = int(input.strip())
		return num
	except ValueError:
		return 0


def pause(pauseTime=(5 * 60)):
	print("paus! " + str(pauseTime / 60) + " min")
	writeToLog('[f]', timeStr(), 'pause started')
	breakLeft = True
	while breakLeft:
		time.sleep(pauseTime)
		playSound('500')
		breakLeft = False
		pauseTime = parseInt(input("återgå till plugget?")) * 60
		if pauseTime > 0:
			breakLeft = True
	writeToLog('[t]', timeStr(), 'pause ended')

studying = False


def main():
	global studying
	intialPause = False
	initPauseLen = 5 * 60

	if len(sys.argv) > 1:
		option = sys.argv[1]

		if option == '-p' or option == '--pause':
			intialPause = True
			if len(sys.argv) > 2:
				initPauseLen = parseInt(sys.argv[2]) * 60
		elif option == '-h' or '--help':
			print("Implement: write help statement.")
			return

	writeToLog('[s]', timeStr(), 'session started')
	if intialPause:
		pause(initPauseLen)
	while True:
		# start studying
		print(timeStr() + " plugga! " + str(studyTime / 60) + " min")
		writeToLog('[d]', timeStr(), 'studying started')
		studying = True
		playSound('600')
		time.sleep(studyTime)
		playSound('400')
		comment = input("under pluggpasset har jag: ")
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
