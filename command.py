import getpass
import sys
import threading
import time

import PettyPomodoro

pp = PettyPomodoro.PettyPomodoro()

Info = '''PettyPomodoro - 0.3.34
---------
Command order:
next\\ENTER - enter next state of Pomodoro
stop\\pause - stop Pomodoro and restart
help       - get help
exit       - exit the program

You can get more information at https://github.com/JacketPants/PettyPomodoro
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
    print("State:", state,
          'Time lift: '+str(pp.GetTaskTime()) + 's'
          if state == "RUN" or state == "REST" else '',
          end='\t\r', flush=True)


if __name__ == "__main__":
    isExit = False
    PrintInfo()
    PrintTime()
    print('\tOPEN')
    (threading.Thread(target=Timer)).start()
    while not isExit:
        command = getpass.getpass(prompt='')
        PrintTime()
        if command == 'start' or command == 'next' or command == '':
            command = 'NEXT'
            pp.StartNext()
        elif command == 'stop' or command == 'pause':
            command = 'STOP'
            pp.Stop()
        elif command == 'help':
            command = 'HELP'
            pass
        elif command == 'exit':
            command = 'EXIT'
            isExit = True
        else:
            command = 'ERROR COMMAND'
            pass
        print('\t', command.upper(), sep='')
    else:
        pass
    sys.exit()
