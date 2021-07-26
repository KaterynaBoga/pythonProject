import random
import time


class Cleaner:
    batteryStep = 2
    waterStep = 10
    maxGarbage = 100

    def __init__(self, battery, garbage, water):
        self.battery = battery
        self.garbage = garbage
        self.water = water
        self.stopping = False
        self.canWash = True

    def move(self):
        while True:
            time.sleep(1)
            self.wash()
            self.vacuum_cleaner()
            print("move")
            self.battery -= self.batteryStep
            self.water -= self.waterStep
            self.garbage += random.randrange(0, 10)
            if self.battery < 20 and not self.stopping:
                raise LowBattery
            if self.battery <= 0:
                raise EmptyBattery
            if self.water <= 0:
                raise NoWater
            if self.garbage > self.maxGarbage:
                raise FullGarbage

    def wash(self):
        if self.canWash:
            print('wash')

    def vacuum_cleaner(self):
        print('vacuum cleaner')

    def workingCondition(self):
        try:
            self.move()
        except LowBattery:
            self.stopping = True
            self.move()
            self.move()
            print("Stop")
        except NoWater:
            self.canWash = False
        except EmptyBattery:
            print("CHARGE MEEEEEEEE")
        except FullGarbage:
            print("Clean Me")


class LowBattery(Exception):
    pass


class EmptyBattery(Exception):
    pass


class NoWater(Exception):
    pass


class FullGarbage(Exception):
    pass


cleaner = Cleaner(100, 0, 100)
cleaner.workingCondition()