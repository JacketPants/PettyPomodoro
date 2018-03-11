import getpass
import sys
import threading
import time

import pettypomodoro

pp = pettypomodoro.PettyPomodoro()
# pp = pettypomodoro.PettyPomodoro(25, 5, 25, 0.5)

Ver = "1.0.1"

Info = '''PettyPomodoro - %s
---------
Input Command:
next\\ENTER - enter next state of Pomodoro
stop\\pause - stop Pomodoro and restart
help       - get help
exit       - exit the program

You can get more information at https://github.com/JacketPants/PettyPomodoro
---------
''' % Ver

Help = '''
Input Command：
next\\ENTER - enter next state of Pomodoro
stop\\pause - stop Pomodoro and restart
help       - get help
exit       - exit the program

Output：
在每次输入指令后，都会输出一个时间戳
时间戳的格式为：年-月-日 分:时:秒 收到的指令
在每个刷新时间内，都会输出当前的Pomodoro状态
输出的格式为：State: 状态 (该状态的剩余时间)

Pomodoro State:
START - after work
RUN - working
END - end work and after rest
REST - resting
STOP - restart the Pomodoro
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


def PrintHelp():
    print(Help)


if __name__ == "__main__":
    isExit = False
    PrintInfo()
    PrintTime()
    print('\tOPEN')
    (threading.Thread(target=Timer)).start()
    while not isExit:
        command = getpass.getpass(prompt='')
        if command == 'start' or command == 'next' or command == '':
            command = 'NEXT'
            pp.StartNext()
        elif command == 'stop' or command == 'pause':
            command = 'STOP'
            pp.Stop()
        elif command == 'help':
            command = 'HELP'
            PrintHelp()
        elif command == 'exit':
            command = 'EXIT'
            isExit = True
        else:
            command = 'ERROR COMMAND'
        PrintTime()
        print('\t', command.upper(), sep='')
    else:
        time.sleep(0.5)
        print()
    sys.exit()
