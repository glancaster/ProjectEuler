st = 1901
end = 2000

# 1901 starts on a tuesday
# so i could use mod on the days 
# [0,1,2,3,4,5,6] -> Days of the Week SMTWThFSt

day = 2

sundays = 0
y = [31,28,31,30,31,30,31,31,30,31,30,31]
ly = [31,29,31,30,31,30,31,31,30,31,30,31]

for year in range(st,end+1):
    n = 0
    if year % 4 == 0:
        n = 1
        if year % 1000 == 0:
            n = 0
            if year % 400:
                n = 1
    
    if n == 0:
        year = y
    else: 
        year = ly
    for month in year:
        if day == 0:
            sundays +=1
        day = (month + day) % 7
        # print(day)
        
print(sundays)
        