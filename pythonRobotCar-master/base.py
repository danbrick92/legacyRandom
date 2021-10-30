#WIP - need to have timer enter correct input as well as time out correctly. need to depricate signal.alarm
# This is the base file for the robot car
import signal

# Called when alarm times out
def interrupted(signum, frame):
    print("0")

signal.signal(signal.SIGALRM, interrupted)


def main():
    print("Running Remote Control Car program...")
    keepRunning = True
    count = 1
    while keepRunning == True:
        keepRunning = update()
        count+= 1
        if count > 10:
            keepRunning = False
    print("Ending Remote Control Car program...")

def update():
    keepRunning = True
    timeout = .01
    signal.setitimer(signal.ITIMER_REAL,timeout)
    command = getUserInput()
    if command.lower() == 'q':
        keepRunning = False
    return keepRunning

def getUserInput():
    command = ""
    try:
        command = input("Type instructions. Type q to exit.")
        signal.alarm(0) 
    except:
        print("Did not receive input. Assuming no action to be taken")
        #signal.getitimer(self.itimer) == (0.0, 0.0)
    return command

# Calls main
if __name__ == "__main__":
    main()