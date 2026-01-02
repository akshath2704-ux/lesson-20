import random
import time
def getrandomdate(startdate,enddate):
    print("printing random date between",startdate,"and",enddate)
    randomgenerator=random.random()
    dateformat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate,dateformat))
    print(starttime)
    endtime=time.mktime(time.strptime(enddate,dateformat))
    print(endtime)
    randomtime=starttime+randomgenerator * (endtime-starttime)                                             
    print(randomtime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("random date=",getrandomdate("1/1/2020","12/12/2024"))