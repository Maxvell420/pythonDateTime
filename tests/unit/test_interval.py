from dates.date import Date
from dates.interval import Interval


def test_exact_1_days():
    date_1 = Date("2000-01-01")
    date_2 = Date("2000-01-02")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() == 1


def test_exact_5000_days():
    date_1 = Date("2011-07-28")
    date_2 = Date("2025-04-05")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() == 5000


def test_not_1_days():
    date_1 = Date("2011-07-28")
    date_2 = Date("2025-04-05")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() != 1


def test_update_day():
    date_1 = Date("2011-07-28")
    date_2 = Date("2025-04-05")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() == 5000
    date_1.add_days(20)
    assert interval.get_dates_interval() == 4980
    date_1.remove_days(40)
    assert interval.get_dates_interval() == 5020


def test_update_month():
    date_1 = Date("2025-04-06")
    date_2 = Date("2025-04-06")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() == 0
    date_2.remove_months(4)
    assert interval.get_dates_interval() == 120


def test_update_month_big():
    date_1 = Date("2025-04-06")
    date_2 = Date("2025-04-06")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() == 0
    date_2.remove_days(5000)
    assert interval.get_dates_interval() == 5000


def test_update_month_big():
    date_1 = Date("2025-04-06")
    date_2 = Date("2025-04-06")
    interval = Interval(date_1, date_2)
    assert interval.get_dates_interval() == 0
    old = date_2.get_cur_point()
    date_2.remove_months(120)
    new = date_2.get_cur_point()
    assert interval.get_dates_interval() == 3653
    date_1.remove_days(3653)
    assert interval.get_dates_interval() == 0


def test_update_years():
    date_1 = Date("2025-04-06")
    date_2 = Date("2025-04-06")
    interval = Interval(date_1, date_2)
    date_1.remove_years(5)
    assert interval.get_dates_interval() == 1826


def test_check_years():
    date_1 = Date("2020-04-06")
    date_2 = Date("2030-04-06")
    interval = Interval(date_1, date_2)
    date_1.add_years(5)
    date_2.remove_years(5)
    assert interval.get_dates_interval() == 0


def test_check_months():
    date_1 = Date("2025-04-06")
    date_2 = Date("2025-04-06")
    interval = Interval(date_1, date_2)
    date_1.remove_months(5)
    date_1.add_months(5)
    assert interval.get_dates_interval() == 0


def test_check_days():
    date_1 = Date("2025-04-06")
    date_2 = Date("2025-04-06")
    interval = Interval(date_1, date_2)
    date_1.add_days(30)
    date_1.remove_days(30)
    assert interval.get_dates_interval() == 0
