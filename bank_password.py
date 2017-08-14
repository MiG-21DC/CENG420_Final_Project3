import csv
from random import Random



def random_num(randomlength=6):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

def random_date(randomlength=6):
    strdate = ''
    # chars = '0123456789'
    # length = len(chars) - 1
    # random = Random()
    # for i in range(randomlength):
    #     str += chars[random.randint(0, length)]
    random = Random()
    year = str(random.randint(0, 99))
    if len(year) == 1:
        year = '0' + year
    month = str(random.randint(1, 12))
    if len(month) == 1:
        month = '0' + month
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        day = str(random.randint(1, 31))
        if len(day) == 1:
            day = '0' + day
    elif month == '02':
        day = str(random.randint(1, 28))
        if len(day) == 1:
            day = '0' + day
    else:
        day = str(random.randint(1, 30))
        if len(day) == 1:
            day = '0' + day
    strdate = year + month + day
    return strdate



for i in range(100):
    print(random_date())

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(2000):
        a = random_date()
        # acode = ed.decode(a)
        # writer.writerow([a, acode, get_score(a), key])
        writer.writerow([a, 0])
    for i in range(8000):
        if i == 1000:
            key = 1
        a = random_str()
        acode = ed.decode(a)
        writer.writerow([a, acode, get_score(a), key])
