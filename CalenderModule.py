import calendar
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
m, d, y = input().split()
print(days[calendar.weekday(int(y), int(m), int(d))])
