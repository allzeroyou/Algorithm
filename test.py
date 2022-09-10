def get_before_day(string, day):
    date = datetime.strptime(string, '%Y-%m-%d')
    before_one_day = date - timedelta(days=day)  # 유동적인 사용을 위한 숫자를 변수 day로 변경
    if before_one_day.month < 10:
        month = '0' + str(before_one_day.month)
    else:
        month = str(before_one_day.month)

    if before_one_day.day < 10:
        day = '0' + str(before_one_day.day)
    else:
        day = str(before_one_day.day)

    before_day = str(before_one_day.year) + '.' + month + '.' + day
    return before_day

from datetime import datetime, timedelta
data['nas_score'] = 0

for i in range(len(data)):
    day = data.loc[i, 'day']
    temp_day = get_before_day(day, 1)

    temp_day = temp_day.split('.')

    if int(temp_day[1]) < 10 or int(temp_day[2]) < 10:
        temp_day[1] = temp_day[1].replace('0', '')
        temp_day[2] = temp_day[2].replace('0', '')
    temp_day = '.'.join(temp_day)

    print(day, temp_day)
    data.loc[i, 'nas_score'] = nasdaq_score[temp_day]


def get_nasdaq_friday():
    friday_list = []
    for i in nasdaq_days:
        date = i.split('-')

        for j in range(len(date)):
            yyyy = int(date[0])
            mm = int(date[1])
            dd = int(date[2])

        if get_days(yyyy, mm, dd) == '금요일':
            date = '-'.join(date)
            nasdaq_friday = {}

            nasdaq_friday['date'] = date
            nasdaq_friday['ratio'] = nasdaq_score[i]
            # print(f'date: {date} ratio: {nasdaq_score[i]}')

            friday_list.append(nasdaq_friday)
    return friday_list


'''
while문 
금요일에 속하는 수이면, 해당 날짜를 키로 하는 value값을 return
-> 함수 만들어서 호출

ipo_before_day_list가 주말이면 nasdap 지수 없음(주말엔 나스닥 휴장)
'''
import datetime


def get_days(yyyy, mm, dd):
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return days[datetime.date(yyyy, mm, dd).weekday()]


# nasdaq_score :'2009-01-08': 0.011 와 같은 출력형식
nasdaq_days = nasdaq_score.keys()  # date
nasdaq_ratios = nasdaq_score.values()  # ratio


def get_nasdaq_friday():
    friday_list = []
    for i in nasdaq_days:
        date = i.split('-')

        for j in range(len(date)):
            yyyy = int(date[0])
            mm = int(date[1])
            dd = int(date[2])

        if get_days(yyyy, mm, dd) == '금요일':
            date = '-'.join(date)
            nasdaq_friday = {}

            nasdaq_friday['date'] = date
            nasdaq_friday['ratio'] = nasdaq_score[i]
            # print(f'date: {date} ratio: {nasdaq_score[i]}')

            friday_list.append(nasdaq_friday)
    return friday_list




from collections import defaultdict
dic_date , dic_ratio  = nasdaq.to_dict()['date'].values() , nasdaq.to_dict()['ratio'].values()

nasdaq_score = defaultdict(lambda : 'no')


for a,b in zip(dic_date, dic_ratio):
  nasdaq_score[a] = b




nasdaq_friday => list
'''
 {'date': '2021-09-17', 'ratio': -0.009},
 {'date': '2021-09-24', 'ratio': -0.0},
 {'date': '2021-10-01', 'ratio': 0.008},
 {'date': '2021-10-08', 'ratio': -0.005},
 {'date': '2021-10-15', 'ratio': 0.005},
'''


for idx,i in enumerate(nasdaq['date']):
  i=i.split('-')
  print(i)
  if int(i[1])<10 or  int(i[2])<10:
    i[1]=i[1].replace('0','')
    i[2]=i[2].replace('0','')
  i='.'.join(i)











