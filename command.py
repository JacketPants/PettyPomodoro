import getpass
import sys
import threading
import time

import pettypomodoro

pp = pettypomodoro.PettyPomodoro()

Info = '''
PettyPomodoro - 0.3.31
---------
'''


def Timer():
    isPlayAudio = 0
    while True:
        state = pp.GetState()
        if state == "STOP":
            isPlayAudio = 0
        if state == "RUN" or state == "REST":
            isPlayAudio = 1
        elif isPlayAudio == 1:
            print()
            PlayAudio()
            isPlayAudio = 0
        PrintState()
        time.sleep(0.5)


def PlayAudio():
    print('\a', end='', flush=True)


def PrintInfo():
    print(Info)


def PrintTime():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), end='')


def PrintState():
    state = pp.GetState()
    print('\r', state, int(pp.GetTaskTime()) if state == "RUN" or state ==
          "REST" else '', end='\t', flush=True)


if __name__ == "__main__":
    PrintInfo()
    PrintTime()
    (threading.Thread(target=Timer)).start()
    while True:
        command = getpass.getpass(prompt='')
        PrintTime()
        print('\t', command.upper())
        if command == 'start' or command == 'next' or command == '':
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
