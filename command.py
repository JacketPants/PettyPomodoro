import sys
import pettypomodoro

PP = pettypomodoro.PettyPomodoro()

Info = '''
PettyPomodoro - 0.1.1
---------
'''


def PrintInfo():
    print(Info)


if __name__ == "__main__":
    PrintInfo()
    while True:
        command = input().lower()
        if command == 'start' or command == 'next':
            pass
        elif command == 'stop' or command == 'pause':
            pass
        elif command == 'exit':
            break
        elif command == 'help':
            pass
        else:
            pass
    sys.exit()
