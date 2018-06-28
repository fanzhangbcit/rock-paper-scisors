### Parse sample log and calculate statistics of streaming rate

# In sample_log.txt file, the snapshot of streaming rate are logged, e.g. "Old=22.686(MBps) New=20.032(MBps)".
# Please parse the log file and get all the samples, and calculate the average streaming rate and
# maximum/minimum/middle values and what time the maximum/minimum/middle occure.
# Author: Fan Zhang

import re
import numpy as np


with open('./sample_log.txt') as fd:

    text = fd.read()
    #Pattern for extract date and time from 2018-03-08T22:55:19.444Z LVL:2
    regexTime= re.compile('(\d{4}-\d{2}-\d{2}[T]\d{2}:\d{2}:\d{2}.\d{3}[Z])\sLVL:2')
    #Pattern for extract speed Old=1.463(MBps)
    regex_speed_old=re.compile('Old=(\d*.\d{3})')
    #Pattern for extract speed New=2.120(MBps)
    regex_speed_new=re.compile('New=(\d*.\d{3})')

    # list of old speed and new speed
    matches_list_speed_old=(regex_speed_old.findall(text))
    matches_list_speed_new=(regex_speed_new.findall(text))
    # list of DateTime
    matchesDate=regexTime.findall(text)

    lDates=matchesDate
    lSpeedOld=[]
    lSpeedNew=[]
    lSpeedAverage=[]

    #convert string to float
    for i in matches_list_speed_old:
         lSpeedOld.append(float(i))
    #convert string to float
    for i in matches_list_speed_new:
         lSpeedNew.append(float(i))

    #generate list of average speed
    lSpeedAverage=[(x + y)/2 for x, y in zip(lSpeedOld, lSpeedNew)]

    ## Use the speed index to find date
    def find_date(speedIndex):
        return lDates[speedIndex]

    # Use numpy to calculate max, min and middle
    # keep 3 decimals for the result, same as in the sample log.
    minSpeed=np.min(lSpeedAverage)
    min_speed_time=find_date(lSpeedAverage.index(minSpeed))
    print("\n***Minimum speed is " + f'{minSpeed:.3f}'+"MBps. And it happened at "+ min_speed_time)

    maxSpeed=np.max(lSpeedAverage)
    max_speed_time=find_date(lSpeedAverage.index(maxSpeed))
    print("\n***Maximum speed is " + f'{maxSpeed:.3f}'+"MBps. And it happened at "+ max_speed_time)

    ## Function to find median speed and time occured
    def find_median(listIn):

        medianSpeed=np.median(listIn)

        #List is even
        if len(listIn)%2 == 0:
            newlist=sorted(listIn)
            #print(newlist)
            #print(len(listIn)/2-1)
            dateFound1=find_date(listIn.index(newlist[int(len(listIn)/2-1)]))
            dateFound2=find_date(listIn.index(newlist[int(len(listIn)/2)]))
            print("\n***Middle speed is " + f'{medianSpeed:.3f}' + "MBps. Since our list is even we have two results:")
            print(dateFound1 + " and " + dateFound2)

        #List is Odd
        else:
            dateFound=find_date(listIn.index(np.median(listIn)))
            print("\n***Middle speed is " + f'{medianSpeed:.3f}' + "MBps. And it happened at "+ dateFound)
    
    find_median(lSpeedAverage)



