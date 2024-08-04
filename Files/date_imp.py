from datetime import datetime

today = datetime.today()

# print(today.day)
# print(today.hour)
# print(today.time())
# print(today.weekday())
# print(today.microsecond)
# print(today.tzinfo)

from datetime import timedelta
# delta = timedelta(
#     days= 59,
#     weeks= 2,
#     seconds= 28,
#     microseconds= 29000,
#     hours= 2,
#     minutes=29

# )
# print(delta)

# print(today + timedelta(days=1))

# birthdate = '12-07-2005'
# def changedate():
#     temp = datetime.strptime(birthdate,'%d-%m-%Y')
#     new_birthdate = datetime.strftime(temp + timedelta(days=365) , '%d-%m-%Y-%A')
#     print(new_birthdate)

# changedate()

from pytz import timezone

utc = datetime.now(timezone('UTC'))

now = utc.astimezone(timezone('Asia/Kolkata'))
print(now)
