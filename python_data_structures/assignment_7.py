'''
Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and 
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.
'''

# f = input('enter file: ')
# fopen = open(f)
fopen = open('coursera_classes/python_data_structures/mbox-short.txt')
tot = dict()
for line in fopen:
    if 'From ' in line:
        words = line.split()
        time = words[5]
        timeSplit = time.split(':')
        day = timeSplit[0]
        tot[day] = tot.get(day, 0) + 1

for k,v in sorted(tot.items()):
    print(k,v)

