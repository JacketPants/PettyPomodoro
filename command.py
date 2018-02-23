import sys
# import os
import threading
import time
import pettypomodoro
import getpass

pp = pettypomodoro.PettyPomodoro()

Info = '''
PettyPomodoro - 0.2.23
---------
'''


def Timer():
    isPlayAudio = 0
    while True:
        PrintState()
        if pp.GetState == "RUN" or pp.GetState == "REST":
            isPlayAudio = 1
        elif isPlayAudio == 1:
            PlayAudio()
            isPlayAudio = 0
        time.sleep(0.5)


def PrintInfo():
    print(Info)


def PrintState():
    state = pp.GetState()
    print('\r', state, int(pp.GetTaskTime()) if state !=
          "STOP" else '', end='', flush=True)


def PlayAudio():
    print('\a', end='', flush=True)


if __name__ == "__main__":
    PrintInfo()
    (threading.Thread(target=Timer)).start()
    PlayAudio()
    while True:
        command = getpass.getpass(prompt='')
        if command == 'start' or command == 'next':
            if pp.GetState != "RUN" or pp.GetState != "REST":
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
