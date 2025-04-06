class Date:
    def __init__(self, date: str):
        [year, month, day] = self._parse_date(date=date)
        self._validate_year(year=year)
        self._validate_month(month=month)
        is_high_year = self._is_high_year(year=year)
        self._validate_day(month=month, days=day, high_year=is_high_year)
        self.year = 1
        self.month = 1
        self.day = 1
        self.point = 1
        self._calc_cur_point(year, month, day)

    def _calc_cur_point(self, year: int, month: int, day: int) -> list:
        if self.year < year:
            self.add_years(year - self.year)

        if self.month < month:
            self.add_months(month - self.month)

        if self.day < day:
            self.add_days(day - self.day)

    def add_years(self, years: int) -> None:
        while years:
            self.add_year()
            years -= 1

    def remove_years(self, years: int) -> None:
        while years:
            self.remove_year()
            years -= 1

    def add_year(self) -> None:
        self.add_months(12)

    def remove_year(self) -> None:
        self.remove_months(12)

    def add_months(self, months: int) -> None:
        while months:
            self.add_month()
            months -= 1

    def remove_months(self, months: int) -> None:
        while months:
            self.remove_month()
            months -= 1

    def remove_month(self) -> None:
        is_high_year = self._is_high_year(self.year)
        days = self._get_month_days(self.month, is_high_year)
        self.remove_days(days)

    def add_month(self) -> None:
        is_high_year = self._is_high_year(self.year)
        days = self._get_month_days(self.month, is_high_year)
        self.add_days(days)

    def add_days(self, days: int) -> None:
        point_days = self.day + days
        self.point += days
        is_high_year = self._is_high_year(self.year)
        cur_month_days = self._get_month_days(self.month, is_high_year)
        while point_days > cur_month_days:
            days -= cur_month_days
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
            is_high_year = self._is_high_year(self.year)
            cur_month_days = self._get_month_days(self.month, is_high_year)
            point_days -= cur_month_days
        self.day += days

    def remove_days(self, days: int) -> None:
        point_days = self.day - days
        self.point -= days
        is_high_year = self._is_high_year(self.year)
        cur_month_days = self._get_month_days(self.month, is_high_year)
        while point_days < 0:
            days -= cur_month_days
            self.month -= 1
            if self.month < 1:
                self.month = 12
                self.year -= 1
            is_high_year = self._is_high_year(self.year)
            cur_month_days = self._get_month_days(self.month, is_high_year)
            point_days += cur_month_days
        self.day -= days

    def get_cur_point(self) -> int:
        return self.point

    def _parse_date(self, date: str) -> list[int]:
        try:
            year = int(date.split("-")[0])
            month = int(date.split("-")[1])
            days = int(date.split("-")[2])
        except:
            raise TypeError("Не верный формат даты!")

        return [year, month, days]

    def _get_years_days(self, year: int) -> int:
        return 366 if self._is_high_year(year=year) else 365

    def _get_month_days(self, month: int, high_year: bool) -> int:
        days = {
            1: 31,
            2: 29 if high_year else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        return days[month]

    def _is_high_year(self, year: int) -> bool:
        if year // 400 == 0:
            return True
        elif year / 4 * 10 % 10 == 0:
            return True
        else:
            return False

    def _validate_year(self, year: int) -> None:
        if not (0 < year < 10000):
            raise ValueError("Месяц не входит в допустимые границы")

    def _validate_month(self, month: int) -> None:
        if not (0 < month < 13):
            raise ValueError("Месяц не входит в допустимые границы")

    def _validate_day(self, month: int, days: int, high_year: bool) -> None:
        cur_month_days = self._get_month_days(month=month, high_year=high_year)

        if not (0 < days < cur_month_days):
            raise ValueError("День не входит в допустимые границы")
