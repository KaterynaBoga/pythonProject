class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_info(self):
        print(f'Max speed: {self.max_speed}\nMileage: {self.mileage}')


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        Vehicle.__init__(self, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def additional_info(self):
            print(f'Seating capacity: {self.seating_capacity}')


volvo = Bus(180, 75000, 4)
volvo.print_info()
volvo.additional_info()

check = isinstance(volvo, Bus)
check_type = type(volvo)
print(check)
print(check_type)

school_bus = Bus(100, 150000, 25)
check_school_bus = isinstance(school_bus, Vehicle)
print(check_school_bus)


class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_info(self):
        print(f'School number: {self.get_school_id}\nNumber of students: {self.number_of_students}')


school_5 = School(5, 1000)
school_5.school_info()


class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def school_add_info(self):
        print(f'School bus color: {self.bus_school_color}')


school_bus_info = SchoolBus(5, 1000, 100, 5000000, 25, 'yellow')
school_bus_info.school_add_info()


