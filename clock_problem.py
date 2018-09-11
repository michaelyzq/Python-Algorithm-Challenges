#Clock angle problem
#Caculate clock angle when input a string

import time


def caculate_angle(time_str):
    list = time_str.split(":")
    hour, minute, second = int(list[0]),int(list[1]), int(list[2])
    hour_angle = 0
    minute_angle = 0
    if hour >= 12:
        hour = hour -12
    hour_angle = hour/12.0*360 
    minute_angle = minute/60.0*360
    hour_angle_adjuect = hour_angle+minute_angle/360*(360/12)

    return abs(hour_angle_adjuect - minute_angle)

print caculate_angle('03:15:00')
