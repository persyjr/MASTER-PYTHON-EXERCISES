#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    hour_init=hr1*3600
    min_init=min1*60
    sec_init=sec1
    hour_end=hr2*3600
    min_end=min2*60
    sec_end=sec2
    result=(hour_end-hour_init)+(min_end-min_init)+(sec_end-sec_init)
    return result


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))