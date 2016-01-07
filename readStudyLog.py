import sys


def printHelp():
	scriptname = sys.argv[0].replace('./', '').replace('.\\', '')
	print("Usage: " + scriptname + " <option> [arguments]")
	print("This script parses the study logfile for human readability.")
	print()
	print("Options:")
	print("    -f, --filter <tag>  Prints out all the lines in the logfile of type <tag>.")

needHelp = True
if len(sys.argv) > 2:
	option = sys.argv[1]
	if (option == '-f' or option == '--filter') and len(sys.argv) >= 3:
		tag = sys.argv[2]
		filteredLines = []
		if len(tag) > 0:
			logfile = open('studylog.txt', 'r')
			lines = logfile.readlines()
			for line in lines:
				if tag.find(line[1]) != -1:
					line = line.replace('\n', '')
					filteredLines.append(line)

	if len(filteredLines) > 0:
		for line in filteredLines:
			print(line)
		needHelp = False
	else:
		print("No lines of type [" + tag + "] exist.")
		needHelp = False

if needHelp:
	printHelp()
