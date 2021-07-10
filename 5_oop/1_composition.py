class Laptop:
    def __init__(self):
        battery = Battery('Battery capacity is 5200')
        self.battery = battery


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


laptop = Laptop()
