import sys


def printHelp():
	scriptname = sys.argv[0].replace('./', '').replace('.\\', '')
	print("Usage: " + scriptname + " <option> [arguments]")
	print("This script parses the study logfile for human readability.")
	print("                                ")
	print("Options:")
	print("    -v, --view [tag] [filter]   Prints out all the lines in the "
							+ "logfile of type <tag>. If [filter] is "
							+ "provided, only prints the fields corresponding "
							+ "to the lettes in [filter].")
	print("    -h, --help                  Prints this help text.")


def checkTagsValid(tags):
	for c in tags:
		if validTags.find(c) == -1:
			return False
	return True


def checkFiltersValid(filters):
	for c in filters:
		if validFilters.find(c) == -1:
			return False
	return True


def printView(tags, filters=''):
	filteredLines = []
	if len(tags) > 0:
		logfile = open('studylog.txt', 'r')
		lines = logfile.readlines()
		for line in lines:
			if tags.find(line[1]) != -1:
				line = line.replace('\n', '')
				filteredLines.append(line)
	if len(filters) > 0:
		refilteredLines = []
		for line in filteredLines:
			lineList = line.split(' ')
			tag = lineList[0]
			timeStr = lineList[1]
			comment = ''
			for i in range(2, len(lineList)):
				comment += lineList[i] + ' '
			comment.strip()
			newLine = ''
			if filters.find('T') != -1:
				newLine += tag + ' '
			if filters.find('t') != -1:
				newLine += timeStr + ' '
			if filters.find('c') != -1:
				newLine += comment
			refilteredLines.append(newLine)
		filteredLines = refilteredLines

	for line in filteredLines:
		print(line)


validTags = 'sedrft'
validFilters = 'Ttc'
tags = ''
filters = ''
viewLog = False
needHelp = False
if len(sys.argv) > 1:
	option = sys.argv[1]
	if (option == '-v' or option == '--view'):
		tagsAreValid = False
		filtersAreValid = False
		if len(sys.argv) >= 4:
			tags = sys.argv[2]
			filters = sys.argv[3]
			tagsAreValid = checkTagsValid(tags)
			filtersAreValid = checkFiltersValid(filters)
			if tagsAreValid and filtersAreValid:
				printView(tags, filters)
			else:
				needHelp = True		# invalid tags or filters
		elif len(sys.argv) >= 3:
			tags = sys.argv[2]
			if checkTagsValid(tags):
				printView(tags)
			else:
				needHelp = True		# invalid tags
		else:
			printView(validTags)
	else:
		needHelp = True		# option is either '-h', '--help', or invalid
else:
	needHelp = True		# option missing

if needHelp:
	printHelp()
