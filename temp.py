# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

#import the urlretrieve library
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
#This retrieves the log data, input your file path to the log copy on your local machine.
#This part of the script counts the total requests in the log.
FILE_NAME = 'local_copy.log'
count = 0
for line in open(FILE_NAME):
    count = count + 1
print('The number of total requests was' ,count)
#Opensthe log and counts instances of requests occuring in the last year.
openedfile = open(FILE_NAME)
readfile = openedfile.read()
count2 = 0
for line in readfile.split('1995'):
    count2 = count2 + 1
print('The total number of requests in 1995 was' ,count2)
count3 = 0
# number of requests on each day of each month, due to python not allowing place holding zeros, the for loop for each month was split into two sections
# each day in Oct
for i in range(24,32):
    string = str(i) + '/Oct/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
# each day in Nov
for i in range(0,9):
    string ='0' + str(i) + '/Nov/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,31):
    string =str(i) + '/Nov/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
#each day in Dec
for i in range(0,9):
    string ='0' + str(i) + '/Dec/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,32):
    string =str(i) + '/Dec/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
# each day in Jan
for i in range(0,9):
    string ='0' + str(i) + '/Jan/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,32):
    string =str(i) + '/Jan/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Feb/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,29):
    string =str(i) + '/Feb/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Mar/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,32):
    string =str(i) + '/Mar/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Apr/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,31):
    string =str(i) + '/Apr/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/May/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,32):
    string =str(i) + '/May/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Jun/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,31):
    string =str(i) + '/Jun/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Jul/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,32):
    string =str(i) + '/Jul/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Aug/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,32):
    string =str(i) + '/Aug/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Sep/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,31):
    string =str(i) + '/Sep/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0
for i in range(0,9):
    string ='0' + str(i) + '/Oct/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
for i in range(10,12):
    string =str(i) + '/Oct/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The number of requests on ' + str(string) + ' was', count3)
    count3 = 0

# of requests each week
day = 24
for i in range (0,2):
    string = str(day) + '/Oct/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7

    day = 7
for i in range (0,4):
    string = str(day) + '/Nov/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 5
for i in range (0,4):
    string = str(day) + '/Dec/1994'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
    day = 2
for i in range (0,5):
    string = str(day) + '/Jan/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 6
for i in range (0,4):
    string = str(day) + '/Feb/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 6
for i in range (0,4):
    string = str(day) + '/Mar/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 3
for i in range (0,4):
    string = str(day) + '/Apr/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 1
for i in range (0,5):
    day = 1
    string = str(day) + '/May/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 6
for i in range (0,4):
    string = str(day) + '/Jun/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 3
for i in range (0,5):
    string = str(day) + '/Jul/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 7
for i in range (0,4):
    string = str(day) + '/Aug/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + 'was', count3)
    count3 = 0
    day = day + 7
day = 4
for i in range (0,4):
    string = str(day) + '/Sep/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in the week of ' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
day = 2
for i in range (0,2):
    string = str(day) + '/Oct/1995'
    for line in readfile.split(string):
            count3 = count3 + 1
    print('The total requests in week of' + str(string) + ' was', count3)
    count3 = 0
    day = day + 7
# of requests each month
count3 = 0
for line in readfile.split('Oct/1994'):
            count3 = count3 + 1
print('The total requests in Oct/1994 was', count3)
count3 = 0
for line in readfile.split('Nov/1994'):
           count3 = count3 + 1
print('The total requests in Nov/1994 was', count3)
count3 = 0
for line in readfile.split('Dec/1994'):
            count3 = count3 + 1
print('The total requests in Dec/1994 was', count3)
count3 = 0
for line in readfile.split('Jan/1995'):
            count3 = count3 + 1
print('The total requests in Jan/1995 was', count3)
count3 = 0
for line in readfile.split('Feb/1995'):
            count3 = count3 + 1
print('The total requests in Feb/1995 was', count3)
count3 = 0
for line in readfile.split('Mar/1995'):
            count3 = count3 + 1
print('The total requests in Mar/1995 was', count3)
count3 = 0
for line in readfile.split('Apr/1995'):
            count3 = count3 + 1
print('The total requests in Apr/1995 was', count3)
count3 = 0
for line in readfile.split('May/1995'):
            count3 = count3 + 1
print('The total requests in May/1995 was', count3)
count3 = 0
for line in readfile.split('Jun/1995'):
            count3 = count3 + 1
print('The total requests in Jun/1995 was', count3)
count3 = 0
for line in readfile.split('Jul/1995'):
            count3 = count3 + 1
print('The total requests in Jul/1995 was', count3)
count3 = 0
for line in readfile.split('Aug/1995'):
            count3 = count3 + 1
print('The total requests in Aug/1995 was', count3)
count3 = 0
for line in readfile.split('Sep/1995'):
            count3 = count3 + 1
print('The total requests in Sep/1995 was', count3)
count3 = 0
for line in readfile.split('Oct/1995'):
            count3 = count3 + 1
print('The total requests in Oct/1995 was', count3)
count3 = 0
# number of bad requests
for i in range(0, 51):
    string2 = '40' + str(i) + " -"
    for line in readfile.split(string2):
            count3 = count3 + 1
print('The total bad requests were', count3)
#number of redirected requests
count3 = 0
for i in range(0, 8):
    string2 = '30' + str(i) + " -"
    for line in readfile.split(string2):
            count3 = count3 + 1
print('The total redirected requests were', count3)

# 12 month file split

for line in open(FILE_NAME):
    if "Oct" in line:
        open("Oct.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "Nov" in line:
        open("Nov.txt", "a").writelines(line)
       
for line in open(FILE_NAME):
    if "Dec" in line:
        open("Dec.txt", "a").writelines(line)

for line in open(FILE_NAME):
    if "Jan" in line:
        open("Jan.txt", "a").writelines(line)

for line in open(FILE_NAME):
    if "Feb" in line:
        open("Feb.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "Mar" in line:
        open("Mar.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "Apr" in line:
        open("Apr.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "May" in line:
        open("May.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "Jun" in line:
        open("Jun.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "Jul" in line:
        open("Jul.txt", "a").writelines(line)
        
for line in open(FILE_NAME):
    if "Aug" in line:
        open("Aug.txt", "a").writelines(line)

for line in open(FILE_NAME):
    if "Sep" in line:
        open("Sep.txt", "a").writelines(line)