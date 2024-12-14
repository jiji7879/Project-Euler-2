MONTH_DAY_COUNT = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year_check(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0


def count_sundays_after_1900(beginning_year: int, ending_year: int) -> int:
    # not implemented
    if beginning_year < 1900 or ending_year < 1900 or ending_year < beginning_year:
        return -1
    count = 0
    local_month = 1
    local_year = 1900
    local_day_of_week = 1
    while local_year <= ending_year:
        # find the day of the week of the next month's first day
        local_day_of_week += MONTH_DAY_COUNT[local_month]
        if local_month == 2 and leap_year_check(local_year):
            local_day_of_week += 1
        local_day_of_week = local_day_of_week % 7

        # sunday is local_day_of_week == 0
        if local_day_of_week == 0 and beginning_year <= local_year <= ending_year:
            count += 1

        # increment time
        if local_month < 12:
            local_month += 1
        else:
            local_month = 1
            local_year += 1
    return count


def p19solution1() -> int:
    return count_sundays_after_1900(1901, 2000)


if __name__ == "__main__":
    print(p19solution1())
