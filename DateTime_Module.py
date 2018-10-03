
import datetime
import pytz

print(datetime.date.today())     #Deal only with days
print(datetime.datetime(2017,4,17,2,50,30,1000))

print('Current time in Local',datetime.datetime.now())
print(datetime.datetime.now().strftime('%B %d, %Y'))

'''
dt_str = 'Apr 17, 2017'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
'''
print('Current time in UTC',datetime.datetime.now(tz=pytz.UTC))

#strftime = Datetime to String
#strptime = string to Datetime