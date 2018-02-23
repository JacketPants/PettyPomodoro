import getpass
import sys
import threading
import time

import pettypomodoro

pp = pettypomodoro.PettyPomodoro(25, 5, 15, 0.5)

Info = '''
PettyPomodoro - 0.2.27
---------
'''


def Timer():
    isPlayAudio = 0
    while True:
        PrintState()
        state = pp.GetState()
        if state == "RUN" or state == "REST":
            isPlayAudio = 1
        elif isPlayAudio == 1:
            PlayAudio()
            isPlayAudio = 0
        time.sleep(0.5)


def PlayAudio():
    print('\a', end='', flush=True)


def PrintInfo():
    print(Info)


def PrintState():
    state = pp.GetState()
    print('\r', state, int(pp.GetTaskTime()) if state ==
          "RUN" or state == "REST" else '', end='\t\t\t', flush=True)


if __name__ == "__main__":
    PrintInfo()
    (threading.Thread(target=Timer)).start()
    while True:
        command = getpass.getpass(prompt='')
        if command == 'start' or command == 'next':
            pp.StartNext()
        elif command == 'stop' or command == 'pause':
            pp.Stop()
        elif command == 'exit':
            break
        elif command == 'help':
            pass
        else:
            pass
    sys.exit()
