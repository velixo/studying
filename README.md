# studying

A simple Python3 script (in swedish) for studying.

## Prerequisites
[pyAudio](http://people.csail.mit.edu/hubert/pyaudio/#downloads)

## TODO:

### High Prio

- Add "free" mode, starts with `py study.py -F, --free`:
  - Study session lasts until actively stopped by user. Pause lasts ([until user ends pause] or [5 min, then prompts if studying should recommence])
- Ability to input shownotes during study session and display them when pause has been initiated
- Add timestamp to pause start
- Ability to skip and accumulate pause time

### Low Prio

- Shorten 600 Hz sound
- Add filter option to show seconds in readLog.py -f
- Add date to logging timestamp
- Add option -o, --overview to readLog.py that display the amount of time studied and paused, in time (hours?) and percentages of study session
- Clear console when script started
- Add desktop notifications?
	- Detect OS
