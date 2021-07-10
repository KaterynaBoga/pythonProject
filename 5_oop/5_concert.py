class Concert:
    max_visitor_num = 0

    def __init__(self):
        self.count = 0

    @property
    def visitors_count(self):
        return self.count

    @visitors_count.setter
    def visitors_count(self, value):
        self.count = Concert.max_visitor_num if value > Concert.max_visitor_num else value


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)  # 50

