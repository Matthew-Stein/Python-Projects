#! python3
# The Morning prompt of my 5 min journal ripoff. 
import csv, os
os.chdir(r'C:\Users\Matthew\Documents\GitHub\Python-Projects\ripoff_journal')
print('3 Things I am greatful for: ')
q1_1 = input()
q1_2 = input()
q1_3 = input()
print('What 3 things would make today great?: ')
q2_1 = input()
q2_2 = input()
q2_3 = input()
print('Daily Affirmation: ')
q3 = input()
logFile = open('weeklyLogAM.csv', 'a', newline='') 
outputWriter = csv.writer(logFile)
outputWriter.writerow([q1_1, q1_2, q1_3, q2_1, q2_2, q2_3, q3])
logFile.close()
