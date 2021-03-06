import sys


def printHelp():
	scriptname = sys.argv[0].replace('./', '').replace('.\\', '')
	helpText = "Usage: " + scriptname + """ <option> [arguments]

Options:
    -f, --filter [tag] [field]  Prints the contents of the logfile. If [tag]
                                is provided, only prints log statements of
                                type [tag]. If [field] is provided, only prints
                                the fields corresponding to the letters in
                                [field].
        Valid [tag] arguments:
            s                    Start of session.
            e                    End of session.
            d                    Studying started.
            r                    Studying ended.
            f                    Pause started.
            t                    Pause ended.
        Valid [field] arguments:
            T                    Displays the log statement tag.
            t                    Displays the time of the log statement.
            c                    Displays the log statement comment.

    -h, --help                   Prints this help text."""

	print(helpText)


def checkTagsValid(tags):
	for c in tags:
		if validTags.find(c) == -1:
			return False
	return True


def checkFieldsValid(fields):
	for c in fields:
		if validFields.find(c) == -1:
			return False
	return True


def printView(tags, fields=''):
	filteredLines = []
	if len(tags) > 0:
		logfile = open('studylog.txt', 'r')
		lines = logfile.readlines()
		for line in lines:
			if tags.find(line[1]) != -1:
				line = line.replace('\n', '')
				filteredLines.append(line)
	if len(fields) > 0:
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
			if fields.find('T') != -1:
				newLine += tag + ' '
			if fields.find('t') != -1:
				newLine += timeStr + ' '
			if fields.find('c') != -1:
				newLine += comment
			refilteredLines.append(newLine)
		filteredLines = refilteredLines

	for line in filteredLines:
		print(line)


validTags = 'sedrft'
validFields = 'Ttc'
tags = ''
fields = ''
viewLog = False
needHelp = False
if len(sys.argv) > 1:
	option = sys.argv[1]
	if (option == '-f' or option == '--filter'):
		tagsAreValid = False
		fieldsAreValid = False
		if len(sys.argv) >= 4:
			tags = sys.argv[2]
			fields = sys.argv[3]
			tagsAreValid = checkTagsValid(tags)
			fieldsAreValid = checkFieldsValid(fields)
			if tagsAreValid and fieldsAreValid:
				printView(tags, fields)
			else:
				needHelp = True		# invalid tags or fields
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
