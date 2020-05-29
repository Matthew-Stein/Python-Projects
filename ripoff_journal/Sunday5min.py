#! Python3
#The sunday overview for my 5 min journal ripoff. 
import csv,os,datetime,shutil
os.chdir(r'C:\Users\Matthew\Documents\GitHub\Python-Projects\ripoff_journal')

#Review AM entries:
print('This week you were greatful for: ')
input("Press Enter to continue...")
prompt1 = []
amFile = open('weeklyLogAM.csv', 'r')
amread = csv.reader(amFile)
for row in amread:
    prompt1.append(row[0:3])
for x in range(len(prompt1)): 
    print(prompt1[x])    
input("Press Enter to continue...")
print('This week you tried your best to: ')
input("Press Enter to continue...")
prompt2 = []
amFile = open('weeklyLogAM.csv', 'r')
amread = csv.reader(amFile)
for row in amread:
    prompt2.append(row[3:6])
for x in range(len(prompt2)): 
    print(prompt2[x]) 
input("Press Enter to continue...")

print('This week you remembered:')
input("Press Enter to continue...")
prompt3 = []
amFile = open('weeklyLogAM.csv', 'r')
amread = csv.reader(amFile)
for row in amread:
    prompt3.append(row[6])
for x in range(len(prompt3)): 
    print(prompt3[x]) 
input("Press Enter to continue...")

#Review PM entries:
print('All these great things happened this week: ')
input("Press Enter to continue...")
prompt4 = []
pmFile = open('weeklyLogPM.csv', 'r')
pmread = csv.reader(pmFile)
for row in pmread:
    prompt4.append(row[0:3])
for x in range(len(prompt4)): 
    print(prompt4[x]) 
input("Press Enter to continue...")

print('This week you could have tried better to:')
input("Press Enter to continue...")
prompt5 = []
pmFile = open('weeklyLogPM.csv', 'r')
pmread = csv.reader(pmFile)
for row in pmread:
    prompt5.append(row[3])
for x in range(len(prompt5)): 
    print(prompt5[x]) 
input("Press Enter to continue...")
#Finish Reviewing
amFile.close()
pmFile.close()
#Merge the AM and PM entries:
savePMResponses = open('weeklyLogPM.csv', 'r')
PMResponses = savePMResponses.read()
saveAMResponses = open('weeklyLogAM.csv', 'a')
saveAMResponses.write('\n')
saveAMResponses.write(PMResponses)
#Close the Files.
savePMResponses.close()
saveAMResponses.close()
#archive the responses in new directory. 
today = datetime.date.today()
shutil.copy('weeklyLogAM.csv', '.\\journal_archive\\%s.csv' % (today))
print('Inputs saved to \journal_archive\%s.csv' % (today))
print('On to a great week ahead!')
#delete the weekly temp files.
os.remove('weeklyLogAM.csv')
os.remove('weeklyLogPM.csv')
