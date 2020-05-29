#! python 3
#The Evening prompt of my 5 min journal ripoff. 
import csv, os
os.chdir(r'C:\Users\Matthew\Documents\GitHub\Python-Projects\ripoff_journal')
print('What 3 things made today great?:')
q1_1 = input()
q1_2 = input()
q1_3 = input()
print('How could I have made today better?: ')
q2 = input()
logFile = open('weeklyLogPM.csv', 'a', newline='') 
outputWriter = csv.writer(logFile)
outputWriter.writerow([q1_1, q1_2, q1_3, q2])
logFile.close()
