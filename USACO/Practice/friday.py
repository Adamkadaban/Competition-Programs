"""
ID: adamkad1
LANG: PYTHON3
TASK: friday
"""
def year(day, date, set):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if date % 400 == 0:
        months[1] = 29
    elif date % 100 != 0 and (date % 100) % 4 == 0:
        months[1] = 29

    week = set
    for time in range(12):
        week = (week + 13) % 7
        day[week] += 1
        week = (week + (months[time] - 13)) % 7
    return day, week

f1 = open('friday.in')
f2 = open('friday.out', 'w')

years = int(f1.read())

days = [0, 0, 0, 0, 0, 0, 0]
start = 1

for time in range(1900, years + 1900, 1):
    days, start = year(days, time, start)

for steps in range(6):
    f2.write(str(days[steps]) + " ")
f2.write(str(days[6]) + "\n")














