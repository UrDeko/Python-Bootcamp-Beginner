year = int(input("Enter year: "))
month = int(input("Enter month: "))

def is_leap(year):
    """Check if year is leap"""
    result = False

    if year % 4 == 0 and year % 100 != 0:
        result = True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        result = True

    return result

def days_in_month(year, month):
    """Return the number of days in given month"""
    month_days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = month_days[month]

    if is_leap(year) and month == 2:
        days += 1

    return days

print(is_leap(year))
print(days_in_month(year, 2))