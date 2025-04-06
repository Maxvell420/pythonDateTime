from .date import Date


class Interval:
    def __init__(self, date_1: Date, date_2: Date):
        self.date_1: Date = date_1
        self.date_2: Date = date_2

    def get_dates_interval(self) -> int:
        return abs(self.date_1.get_cur_point() - self.date_2.get_cur_point())
