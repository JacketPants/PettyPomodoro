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
        self.__myThread = threading.Thread(target=self.__Thread)
        self.__myThread.start()

    def __SetState(self, command):
        self.__state = command

    def __SetTime(self):
        self.__timeList.append(time.time())

    def __Thread(self):
        while True:
            state = self.GetState()
            if state == "RUN" or state == "REST":
                if time.time() > self.__endTime:
                    self.__SetState("END" if state == "RUN" else "START")
            time.sleep(self.__timer)

    def GetPomodoro(self):
        return [self.__pomodoroTime, self.__restTime, self.__restTimeLong, self.__timer]

    def GetState(self):
        return self.__state

    def GetTimeList(self):
        return self.__timeList

    def GetTaskTime(self):
        return self.__endTime-time.time()

    def Stop(self):
        self.__SetState("STOP")
        self.SetPomodoro()

    def SetPomodoro(self, pomodoroTime=-1, restTime=-1, restTimeLong=-1, timer=-1):
        self.__SetState("STOP")
        self.__timeList = []
        if pomodoroTime != -1:
            self.__pomodoroTime = pomodoroTime
        if restTime != -1:
            self.__restTime = restTime
        if restTimeLong != -1:
            self.__restTimeLong = restTimeLong
        if timer != -1:
            self.__timer = timer

    def StartNext(self):
        state = self.GetState()
        if state == "START" or state == "STOP":
            self.__SetTime()
            self.__SetState("RUN")
            self.__endTime = self.__timeList[len(
                self.__timeList)-1] + self.__pomodoroTime
        elif state == "END":
            self.__SetTime()
            self.__SetState("REST")
            self.__endTime = self.__timeList[len(self.__timeList)-1] + (
                self.__restTimeLong if len(
                    self.__timeList) % 8 == 0 else self.__restTime)
        else:
            return False
        return True


# The Test Code
if __name__ == "__main__":
    pp = PettyPomodoro(25, 5, 15)
    print("Petty Pomodoro Test")
    while True:
        command = input()
        if command == "e":
            break
        elif command == "n":
            pp.StartNext()
        elif command == "p":
            print("State:"+str(pp.GetState()))
            print("TaskTime:"+str(pp.GetTaskTime()))
            print("Pomodoro:"+str(pp.GetPomodoro()))
            print("TimeList:"+str(pp.GetTimeList()))
        elif command == "s":
            pp.Stop()
        else:
            print("Please Input Right Command")
    sys.exit()
