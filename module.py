# from fn import factorial
# num=5
# fac=factorial(num)
# print(fac)
from datetime import datetime,timedelta

today=datetime.now()
print(today)

yesterday=datetime.now()-timedelta(days=1)
print(yesterday)