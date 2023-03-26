import datetime

''' Написать функцию, которая находит ближайшую пятницу 13-е '''

def add_one_month(when): # instead of ... + datetime.timedelta(months=1)
    new_year = when.year
    new_month = when.month + 1
    if new_month > 12:
        new_year += 1
        new_month -= 12
    return datetime.date(new_year, new_month, 1)

def get_next_Fr13(when):
    if when.day >= 13:
        when = add_one_month(when)
    new_date = datetime.date(when.year, when.month, 1)
    if (new_date.weekday() == 6):
        return datetime.date(when.year, when.month, 13)
    else:
        new_date = add_one_month(when)
        return get_next_Fr13(new_date)

def inp():
    print('Введите дату:')
    yr, m, d = int(input('год ')), int(input('месяц ')), int(input('день '))
    dateobj = datetime.date(yr, m, d)
    return dateobj
dateobj = inp()
if datetime.date.today() > dateobj:
    print('Введите дату, не более позднюю, чем сегодня.')
    inp()

print('Ближайшая пятница 13-е наступит', end=' ')
print(get_next_Fr13(dateobj))
