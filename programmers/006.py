import datetime
def solution(a, b):
    daylist = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return daylist[datetime.date(2016,a,b).weekday()]


print(solution(5,24))