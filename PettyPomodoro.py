#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import threading
import time


class PettyPomodoro():
    def __init__(self, pomodoroTime=25*60, restTime=5*60, restTimeLong=15*60, timer=0.5):
        # pomodoro state
        self.__state = "START"
        # every time after the PP start the 0 is start time
        self.__timeList = []
        # the runing task's end time
        self.__endTime = 0
        self.__pomodoroTime = pomodoroTime
        self.__restTime = restTime
        self.__restTimeLong = restTimeLong
        self.__timer = timer

    def GetPomodoro(self):
        return [self.__pomodoroTime, self.__restTime, self.__restTimeLong, self.__timer]

    def GetState(self):
        return self.__state

    def GetTimeList(self):
        return self.__timeList

    def GetTaskTime(self):
        return self.__endTime-time.time()

    def SetPomodoro(self, pomodoroTime=-1, restTime=-1, restTimeLong=-1, timer=-1):
        if pomodoroTime != -1:
            self.__pomodoroTime = pomodoroTime
        if restTime != -1:
            self.__restTime = restTime
        if restTimeLong != -1:
            self.__restTimeLong = restTimeLong
        if timer != -1:
            self.__timer = timer

    def StartNext(self):
        myThread = threading.Thread(target=self.__Thread)
        if self.GetState() == "START":
            self.__SetTime()
            self.__SetState("RUN")
            self.__endTime = self.__timeList[len(
                self.__timeList)-1] + self.pomodoroTime
        elif self.GetState() == "END":
            self.__SetTime()
            self.__SetState("REST")
            self.__endTime = self.__timeList[len(self.__timeList)-1] + (
                self.restTimeLong if len(
                    self.__timeList) % 8 == 0 else self.restTime)
        elif self.GetState() == "STOP":
            self.__init__()
            self.__SetTime()
            self.__SetState("RUN")
            self.__endTime = self.__timeList[len(
                self.__timeList)-1] + self.pomodoroTime
        else:
            return False
        myThread.start()
        return True

    def __SetState(self, command):
        self.__state = command

    def __SetTime(self):
        self.__timeList.append(time.time())

    def __Thread(self):
        while time.time() <= self.__endTime:
            if self.GetState == "STOP":
                break
            else:
                self.PrintPomodoro()
                time.sleep(0.2)
        else:
            self.__SetState("END" if self.GetState() == "RUN" else "START")


if __name__ == "__main__":
    pp = PettyPomodoro(5, 2, 3)
    print("Petty Pomodoro Command")
    while True:
        command = input()
        if command == "exit":
            break
        elif command == "next":
            pp.StartNext()
        elif command == "print":
            pp.PrintPomodoro()
        else:
            print("Please Input Right Command")
    else:
        sys.exit()