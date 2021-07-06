class City():
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def check_popuation(self):
        if self.population > 1500:
            return f"The population of the city {self.name} is {self.population}"
        else:
            return "Your city is too small"


lugansk = City('Lugansk', 200000)
dnipro = City('Dnipro', 1000000)
pokrov = City('Pokrov', 1000)

for population in (lugansk, dnipro, pokrov):
    print(population.check_popuation())



class OverrideAdd:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        if self.x > 10 or y.x > 10:
            return self.x * y.x
        else:
            return self.x + y.x


class CallMethod:
    def __call__(self, x, y):
        result = x + y
        return result


class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        len_my_str = len(self.cart)
        return len_my_str > 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))