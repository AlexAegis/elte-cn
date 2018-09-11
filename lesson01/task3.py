import this


def isWeekend(day):
    return day >= 5 & day <= 6

def alarmClock(day, isVacation):
    if not isVacation:
        return "7:00" if not isWeekend(day) else "10:00"
    else:
        return "10:00" if not isWeekend(day) else "OFF"

print isWeekend(0)
print isWeekend(6)
print alarmClock(0, False)
print alarmClock(6, True)
